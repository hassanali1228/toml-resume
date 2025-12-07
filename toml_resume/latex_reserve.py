metadata = r"""\documentclass[12pt]{article}
\usepackage[cm]{fullpage}
\usepackage{hyperref}
\usepackage{fontawesome}
\usepackage{amssymb}
\usepackage[b4paper, paperwidth=9in, paperheight=12.2in, margin=0.3in]{geometry}
\usepackage{lmodern}
\usepackage[usenames,dvipsnames]{color}
\usepackage{enumitem}

\hypersetup{breaklinks=true,%
pagecolor=white,%
colorlinks=true,%
linkcolor=cyan,%
urlcolor=MyLinkColor}

\definecolor{MyDarkBlue}{rgb}{0,0.0,0.45}
\definecolor{MyLinkColor}{rgb}{0,0.208,0.459}
\renewcommand{\familydefault}{\sfdefault}

%%%%%%%%%%%%%%%%%%%%%%%%%%
% Formatting parameters  %
%%%%%%%%%%%%%%%%%%%%%%%%%%

\newlength{\tabin}
\setlength{\tabin}{1em}
\newlength{\secsep}
\setlength{\secsep}{0.1cm}

\setlength{\parindent}{0in}
\setlength{\parskip}{0in}
\setlength{\itemsep}{0in}
\setlength{\topsep}{0in}
\setlength{\tabcolsep}{0in}

\definecolor{contactgray}{gray}{0.3}

\pagestyle{empty}

%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Template Definitions  %
%%%%%%%%%%%%%%%%%%%%%%%%%%
\newcommand{\lineunder}{\vspace*{-8pt} \\ \hspace*{-6pt} \hrulefill \\ \vspace*{-15pt}}
\newcommand{\name}[1]{\begin{center}\textsc{\color{darkblue}\Huge#1}\end{center}}
\newcommand{\program}[1]{\begin{center}\textsc{#1}\end{center}}
\newcommand{\contact}[1]{\begin{center}{\small#1}\end{center}}
\newcommand{\smallfont}{\fontsize{11.5}{13}\selectfont}

\newenvironment{tabbedsection}[1]{
  \begin{list}{}{
      \setlength{\itemsep}{0pt}
      \setlength{\labelsep}{0pt}
      \setlength{\labelwidth}{0pt}
      \setlength{\leftmargin}{3pt}
      \setlength{\rightmargin}{5pt}
      \setlength{\listparindent}{0pt}
      \setlength{\parsep}{0pt}
      \setlength{\parskip}{0pt}
      \setlength{\partopsep}{0pt}
      \setlength{\topsep}{#1}
    }
  \item[]
}{\end{list}}

\newenvironment{nospacetabbing}{\begin{tabbing}}
{\end{tabbing}\vspace{-1.2em}}

\newenvironment{resume_header}{}{\vspace{2pt}}
"""

resume_section_colored_template = r"""
\newenvironment{resume_section}[1]{
  \filbreak
  \vspace{2\secsep}
  \textbf{\color{YellowOrange}\Large#1 \hrulefill } \textcolor{white}{\lineunder} 
  \vspace{-7pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}
"""

resume_section_greyscale_template = r"""
\newenvironment{resume_section}[1]{
  \filbreak
  \vspace{2\secsep}
  \textsc{\large#1}
  \lineunder
  \vspace{-2pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}
"""

resume_subsection_template = r"""
\newenvironment{resume_subsection}[2][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\small #1} %\hspace{2em}
  \vspace{2 pt}
  \begin{tabbedsection}{0.5\secsep}
}{\end{tabbedsection}}
"""

resume_education_template = r"""
\newenvironment{education}[3][]{
  \vspace{\secsep}
  \textbf{#2} \hfill {\hspace{-2pt} #3}\\
  \vspace{-13pt}
  \begin{tabbedsection}{\secsep}
}{\end{tabbedsection}}
"""

resume_subitems_template = r"""
\newenvironment{subitems}{
  \renewcommand{\labelitemi}{-}
  \begin{itemize}
      \setlength{\labelsep}{1em}
      \smallfont
}{\end{itemize}}
"""

resume_nobulletsubitems_template = r"""
\newenvironment{nobulletsubitems}{
  \renewcommand{\labelitemi}{} % Remove bullet point
  \begin{itemize}[leftmargin=*]
    \smallfont
}{\end{itemize}}
"""

resume_employer_colored_template = r"""
\newenvironment{resume_employer}[4]{
  \vspace{\secsep}
  \textbf{#1} \hfill  {\color{YellowOrange} \footnotesize#3 \vspace{1 pt}}\\ 
  \normalsize{\it #2} \hfill { \footnotesize {#4}} \\
  \vspace{-16 pt} 
  \begin{tabbedsection}{0pt}
  \vspace{1.5pt}
  \begin{subitems}
}{\end{subitems}\end{tabbedsection} \vspace{4pt}}
"""

resume_employer_greyscale_template = r"""
\newenvironment{resume_employer}[4]{
  \vspace{\secsep}
  \textbf{#1} \hfill  {\color{YellowOrange} \footnotesize#3 \vspace{1 pt}}\\ 
  \normalsize{#2} \hfill { \footnotesize {#4}} \\
  \vspace{-16 pt} 
  \begin{tabbedsection}{0pt}
  \vspace{1.5pt}
  \begin{subitems}
}{\end{subitems}\end{tabbedsection} \vspace{2pt}}
"""


colored_start = r"""
\definecolor{darkblue}{rgb}{0.0, 0.0, 0.55}

\begin{document}
"""

grayscale_start = r"""
\definecolor{darkblue}{rgb}{0.0, 0.0, 0.00}
\definecolor{YellowOrange}{rgb}{0.0, 0.0, 0.00}

\begin{document}
"""

end = r"\end{document}"
