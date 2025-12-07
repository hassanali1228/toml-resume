import click
import toml
from pathlib import Path
import subprocess
import os

from .generator import generator

@click.command()
@click.option("--role", default="sre")
@click.option("--color/--no-color", default=True)
@click.option("--mission/--no-mission", default=False)
@click.option(
    "--stdout",
    "-o",
    type=click.Choice(["tex", "pdf"], case_sensitive=False),
    default="tex",
)
@click.option("--i", is_flag=True, default=False, help="interactive mode: open pdf")
@click.argument('toml_path', type=click.Path(exists=True, dir_okay=False))
@click.argument('out_path', type=click.Path(dir_okay=False))
def toml_resume(role: str, color: bool, mission: bool, stdout: list[str], toml_path: Path, out_path: Path, i: bool):
    """Generate a resume from a TOML file.
    """
    toml_path = Path(toml_path)
    out_path = Path(out_path)

    toml_dict = toml.load(toml_path)

    latex_str = generator(toml_dict, colored_resume=color, include_mission=mission, role=role)

    if "tex" in stdout:
        with out_path.open(mode="w") as f:
            f.write(latex_str)

    if "pdf" in stdout:
        tex_path = out_path.with_suffix(".tex")
        with tex_path.open(mode="w") as f:
            f.write(latex_str)
        
        try:
            subprocess.call(['pdflatex', '-interaction=nonstopmode', tex_path])
        except:
            raise ValueError("pdflatex failed to compile the .tex file")
        finally:
            if os.path.exists(tex_path): os.remove(tex_path)
            if os.path.exists(out_path.with_suffix(".log")): os.remove(out_path.with_suffix(".log"))
            if os.path.exists(out_path.with_suffix(".aux")): os.remove(out_path.with_suffix(".aux"))
            if os.path.exists(out_path.with_suffix(".out")): os.remove(out_path.with_suffix(".out"))

        if i:
            # mac os only implementation
            subprocess.call(('open', out_path.with_suffix(".pdf")))
