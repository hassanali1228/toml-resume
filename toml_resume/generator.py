import toml
from toml_resume.latex_reserve import *


class ResumeWriter:
    def __init__(self) -> None:
        self.latex_str = ""
        self.dent = 0

    def add_line(self, line: str) -> None:
        self.latex_str += "  " * self.dent + line + "\n"

    def indent(self, value: int = 1) -> None:
        self.dent += value

    def dedent(self, value: int = 1) -> None:
        self.dent -= value


def add_profile(writer: ResumeWriter, profile: dict[str, str | dict[str, str]]) -> None:
    writer.add_line("\\begin{resume_header}")
    writer.add_line(f"\\name{{{profile['name']}}} \\vspace{{0.02in}}")
    writer.add_line("\\contact{")
    writer.indent()

    for idx, link in enumerate(profile["links"]):
        if "url" in link:
            line = f"\\fa{link['favicon']}\enspace \href{{{link['url']}}}{{{link['display']}}}"
        else:
            line = f"\\fa{link['favicon']}\enspace {link['display']}"

        if idx != len(profile["links"]) - 1:
            line += " \hspace{0.25in} \\"
        else:
            line += " \\"

        writer.add_line(line)

    writer.dedent()
    writer.add_line("}")
    writer.add_line("\\end{resume_header}")


def add_skills(writer: ResumeWriter, skills: dict[str, list[str]]) -> None:
    writer.add_line("\\begin{resume_section}{Skills}")
    writer.indent()
    writer.add_line("\\begin{nospacetabbing}")
    for idx, (category, skill_list) in enumerate(skills.items()):
        skill_str = f"\\textbf{{\\color{{darkblue}}{category}:}} \= "
        skill_str += ", ".join(skill_list)
        if idx != len(skills) - 1:
            skill_str += " \\\\[1pt]"
        else:
            skill_str += " \\\\*"
        writer.add_line(skill_str)

    writer.add_line("\\vspace{2pt}")
    writer.add_line("\\end{nospacetabbing}")
    writer.dedent()

    writer.add_line("\\end{resume_section}")


def parse_role_table(table: dict) -> dict:
    role_table = {}
    for role, val in table.items():
        if isinstance(val, str) and val in table.keys():
            role_table[role] = table[val]
        else:
            role_table[role] = val
    return role_table


def add_work_experience(
    writer: ResumeWriter,
    include_mission: bool,
    experience: dict[str, str | list[str] | dict[str, list[int]]],
    role: str,
) -> None:
    title_table = parse_role_table(experience["title"])

    writer.add_line("\\begin{resume_employer}")
    writer.indent()
    line = f"{{\\color{{darkblue}} {experience['company']}"
    line += f" - \\normalfont {experience['mission']}}}" if include_mission else "}"
    writer.add_line(line)

    writer.add_line(f"{{{title_table[role]}}}")
    writer.add_line(
        f"{{\\bf {experience['location']}}} {{{experience['date_range']}}} \\vspace{{3.2 pt}}"
    )

    order_table = parse_role_table(experience["order"])
    for idx in order_table[role]:
        try:
            writer.add_line(f"\\item {experience['content'][idx]}")
        except IndexError: 
            pass # allows for easy design re-iterations without breaking the code

    writer.dedent()
    writer.add_line("\\end{resume_employer}")


def add_project(writer: ResumeWriter, project: dict[str, list[str]]) -> None:
    line = "\\begin{resume_subsection} "
    tool_list = ", ".join(project["tools"])
    if "url" not in project:
        line += f"{{\\textcolor{{darkblue}} {{{project['name']}}} "
        line += f"\color{{black}} - {tool_list}}}"
    else:
        line += (
            f"{{\href{{{project['url']}}}{{\\textcolor{{darkblue}}{{{project['name']}}}"
            f"\color{{black}} - {tool_list} \\faicon{{{project['favicon']}}}}}}}"
        )
    writer.add_line(line)

    writer.indent()
    writer.add_line("\\begin{subitems}")
    for item in project["content"]:
        writer.add_line(f"\\item {item}")
    writer.dedent()
    writer.add_line("\\end{subitems}")
    writer.add_line("\\end{resume_subsection}")


def add_education(writer: ResumeWriter, education: dict[str, str]) -> None:
    writer.add_line("\\begin{resume_section}{Education}")
    writer.indent()
    writer.add_line("\\begin{education}")
    writer.indent()

    writer.add_line(
        f"{{\\textcolor{{darkblue}}{{{education['school']}}} - \\normalfont {education['degree']}}}{{{education['date_range']}}}"
    )

    writer.add_line("")
    writer.add_line("\\begin{nobulletsubitems}")
    writer.add_line("\setlength{\itemindent}{0.25em}")
    writer.indent()

    for item in education["content"]:
        key, val = item.values()
        writer.add_line(f"\\item {{\\textcolor{{darkblue}}{{{key}}}}}: {val}")

    writer.dedent()
    writer.add_line("\end{nobulletsubitems}")

    writer.dedent()
    writer.add_line("\\end{education}")
    writer.dedent()
    writer.add_line("\\end{resume_section}")


def add_work_experiences(
    writer: ResumeWriter, include_mission: bool, role: str, work_experiences: list[dict],
):
    writer.add_line("\\begin{resume_section}{Work Experience}")
    writer.add_line("")
    writer.indent()

    for work_experience in work_experiences:
        add_work_experience(writer, include_mission, work_experience, role)
        writer.add_line("")

    writer.dedent()
    writer.add_line("\\end{resume_section}")


def add_projects(writer: ResumeWriter, projects: list[dict]) -> None:
    writer.add_line("\\begin{resume_section}{Personal Projects}")
    writer.add_line("")
    writer.indent()

    for project in projects:
        add_project(writer, project)
        writer.add_line("")

    writer.dedent()
    writer.add_line("\\end{resume_section}")


def generator(
    toml_dict: dict,
    colored_resume: bool,
    include_mission: bool,
    role: str,
) -> str:
    resume_writer = ResumeWriter()

    section_parser_mapping = {
        "profile": (add_profile, resume_writer,),
        "skills": (add_skills, resume_writer,),
        "education": (add_education, resume_writer,),
        "work_experiences": (add_work_experiences, resume_writer, include_mission, role),
        "projects": (add_projects, resume_writer,),
    }

    resume_writer.latex_str = (
        metadata +
        (resume_section_colored_template if colored_resume else resume_section_greyscale_template) +
        resume_subsection_template +
        resume_education_template +
        resume_subitems_template +
        resume_nobulletsubitems_template +
        (resume_employer_colored_template if colored_resume else resume_employer_greyscale_template) +
        (colored_start if colored_resume else grayscale_start)
    )

    resume_writer.add_line("")

    for section, content in toml_dict.items():
        if section not in section_parser_mapping: continue
        (method, *params) = section_parser_mapping[section] # assign input variables needed for each fxn

        # call each section's parser
        method(*params, content)
        resume_writer.add_line("")

    resume_writer.latex_str += end

    return resume_writer.latex_str


if __name__ == "__main__":
    toml_dict = toml.load("resume.toml")
    config = toml_dict["config"]
    del toml_dict["config"]

    print(generator(toml_dict, **config))
