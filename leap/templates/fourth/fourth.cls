\ProvidesClass{fourth}[2010/07/10 v0.9 Resume class]
\LoadClass[10pt]{article} 
\usepackage{geometry}
\usepackage{fontawesome}
\usepackage{hyperref}
\geometry{left=1.5cm, right=1.5cm, top=2cm, bottom=2cm}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{parskip}
% Fonts and colors
\usepackage{xcolor}
\usepackage{titlesec}

%Fints being used
\renewcommand{\familydefault}{\sfdefault}
%Defining a color
\definecolor{darkblue}{RGB}{0, 102, 204}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=blue,
    urlcolor=blue,
}
% line for the skill section
\newcommand{\boldunderline}[1]{\textbf{\underline{#1}}}





% Define colors
\definecolor{headercolor}{HTML}{1F497D}
\definecolor{accentcolor}{HTML}{003366}


% Define section format: Bold title and a thick line
%\titleformat{\section}{\large\bfseries \color{black}}{}{0em}{}[\rule{0.9\columnwidth}{1.5pt}]


% Define custom section formatting with a larger font
\titleformat{\section} % Section title formatting
  {\fontsize{18}{20}\bfseries \color{black}} % Increase the font size here
  {} % No label
  {0em} % No space between label and title text
  {} % No additional formatting before title
  [\vspace{-0.5em}\rule{0.9\columnwidth}{1.5pt}] % Line (rule) placed immediately after the title with reduced space

% Control the vertical spacing around sections
\titlespacing*{\section}
  {0pt} % No extra indentation
  {0.5em} % Space before the section title
  {0.2em} % Space after the section title

\newenvironment{compactitem}{
  \begin{itemize}
    \setlength{\itemsep}{0pt}  % No space between items
    \setlength{\parskip}{0pt}  % No space between paragraphs
    \setlength{\leftmargini}{0pt}  % Remove left margin (indentation)
    \setlength{\itemindent}{0pt}  % Ensure items start from the left margin
    \setlength{\labelsep}{0.5em}  % Control the space between the bullet and the text
    \renewcommand{\labelitemi}{\raisebox{0.5ex}{\tiny$\bullet$}}  % Use a smaller dot as bullet
  }
  {\end{itemize}}
  
