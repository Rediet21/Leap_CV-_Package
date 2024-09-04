\ProvidesClass{minimal}[2010/07/10 v0.9 Resume class]

\LoadClass[10pt]{article} % Font size and paper type

\usepackage[a4paper, left=2em, right=2em, top=2.5em, bottom=5.0em]{geometry}
\usepackage{multicol}
\setlength{\columnsep}{0cm}
\usepackage{xcolor}
\usepackage{fontspec}
\usepackage{setspace}
\usepackage{lipsum}
\usepackage[none]{hyphenat}
\usepackage{changepage}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,      % Ensure links are colored
    linkcolor=blue,       % Internal links (e.g., Table of Contents)
    urlcolor=blue,        % URLs (like your project and certificate links)
    citecolor=blue        % Citations
}
\usepackage{xcolor}
\newcommand{\xhrulefill}[2]{\leavevmode\leaders\hrule height #2 \hfill\kern0pt\relax}
\usepackage{iftex}
\usepackage[parfill]{parskip} % Remove paragraph indentation
\usepackage{array} % Required for boldface (\bf and \bfseries) tabular columns
\usepackage{ifthen} % Required for ifthenelse statements

\pagestyle{empty} % Suppress page numbers

\defaultfontfeatures{LetterSpace=2.5}


% new command for external links:
%\renewcommand{\href}[2]{\hrefWithoutArrow{#1}{\ifthenelse{\equal{#2}{}}{ }{#2 }\raisebox{.15ex}{\footnotesize \faExternalLink*}}}


\setmainfont{Raleway}[
    Path= ./fonts/,
    Extension = .ttf,
    UprightFont=*-Light,
    BoldFont=*-Medium,
    ItalicFont=*-Italic,
    ItalicFeatures={
        SmallCapsFont=*-Italic,
    },
    BoldFeatures={
        SmallCapsFont=*-Medium,  
    },
    SmallCapsFont=*-Medium,
    ]

\definecolor{flashyGreen}{RGB}{245, 34, 45} % Adjust the RGB values as needed
\definecolor{lavenderBlue}{RGB}{245, 34, 45} % Adjust the RGB values as needed

% \printname is used to print the name as a page header
\def \printname {
  \begingroup
    \hfil{\MakeUppercase{\namesize\bf \@name}}\hfil
    \nameskip\break
  \endgroup
}



% The below commands define the whitespace after certain things in the document - they can be \smallskip, \medskip or \bigskip
\def\namesize{\Large} % Size of the name at the top of the document
\def\addressskip{\smallskip} % The space between the two address (or phone/email) lines
\def\sectionlineskip{\medskip} % The space above the horizontal line for each section 
\def\nameskip{\bigskip} % The space after your name at the top
\def\sectionskip{\medskip} % The space after the heading section




% Load necessary packages
\RequirePackage{multicol}
\RequirePackage{enumitem}
\RequirePackage{xcolor}
\RequirePackage{fontspec}

% Define custom commands
\newcommand{\badge}[2]{\noindent\textcolor{#1}{#2}\par}
\newcommand{\headerSection}[1]{\noindent\textbf{#1}\par}



\newcommand{\cvSection}[1]{
  \vspace{1em}
  {\Large \textbf{#1} \xhrulefill{black}{0.8mm}} % Adjust the thickness as needed
  \vspace{0.5em}
}

% Command to format position and company line
\newcommand{\positionAndCompanyLine}[3]{
  \noindent\textbf{#1}, \emph{#2} \hfill 
  \textcolor{flashyGreen}{#3}\par
}

\newcommand{\project}[2]{\noindent\textbf{#1} \emph{#2}\par}

%\newcommand{\badge}[2]{\colorbox{#1}{#2}}


\newcommand{\cvParagraph}[1]{\noindent#1\par}



