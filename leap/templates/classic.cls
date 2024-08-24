\ProvidesClass{classic}[2010/07/10 v0.9 Resume class]

\LoadClass[10pt]{article} % Font size and paper type

\usepackage[parfill]{parskip} % Remove paragraph indentation
\usepackage{array} % Required for boldface (\bf and \bfseries) tabular columns
\usepackage{ifthen} % Required for ifthenelse statements
\usepackage{enumitem} % for customizing lists
\AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment

\pagestyle{empty} % Suppress page numbers

%====
%	HEADINGS COMMANDS: Commands for printing name and address
%====

\def \name#1{\def\@name{#1}} % Defines the \name command to set name
\def \@name {} % Sets \@name to empty by default
\def \addressSep {$\diamond$} % Set default address separator to a diamond

% One, two or three address lines can be specified 
\let \@addressone \relax
\let \@addresstwo \relax
\let \@addressthree \relax

% \address command can be used to set the first, second, and third address (last 2 optional)
\def \address #1{
  \@ifundefined{@addresstwo}{
    \def \@addresstwo {#1}
  }{
  \@ifundefined{@addressthree}{
  \def \@addressthree {#1}
  }{
     \def \@addressone {#1}
  }}
}

% \printaddress is used to style an address line (given as input)
\def \printaddress #1{
  \begingroup
    \def \\ {\addressSep\ }
    \centerline{#1}
  \endgroup
  \par
  \addressskip
}

\newcolumntype{x}[1]{%
>{\raggedleft\hspace{0pt}}p{#1}}%
\usepackage[default]{raleway}


% set font default
\renewcommand*\familydefault{\sfdefault} 	
\usepackage[T1]{fontenc}

% more font size definitions
\usepackage{moresize}		
% change the margins to 2 inches all round	
\usepackage[a4paper, left=2em, right=2em, top=2.5em, bottom= 10em]{geometry}

%use customized header 
\usepackage{fancyhdr}				
%use our custom fancy header definitions


%less space between header and content
\setlength{\headheight}{-5pt}		
\setlength{\parindent}{0mm}



%for layouting tables
\usepackage{multicol}			
\usepackage{multirow}

%extended aligning of tabular cells
\usepackage{array}
\usepackage{tabularx}
\usepackage{color}
\usepackage{hyperref}  % For hyperlinks

%accent color
\definecolor{sectcol}{RGB}{0,150,255}

%dark background color
\definecolor{bgcol}{RGB}{110,110,110}

%light background / accent color
\definecolor{softcol}{RGB}{225,225,225}


\renewcommand{\headrulewidth}{0pt} 

%remove botttom header line
\renewcommand{\footrulewidth}{0pt}	  	

%remove pagenum
\renewcommand{\thepage}{}	

%remove section num		
\renewcommand{\thesection}{}			
\newcommand{\cvsection}[1]
{
	\begin{center}
		\large\textcolor{sectcol}{\textbf{#1}}
	\end{center}
}
\newcommand{\cvsections}[1]
{
	\begin{center}
		\large\textcolor{sectcol}{\textbf{#1}}
	\end{center}
}

\newcommand{\metasection}[1]
{
\hspace*{\fill} \footnotesize{#1}\\[1pt]
}


\newcommand{\cvevent}[3]
{
    \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} @{}p{12cm} p{4.5cm}@{}} 
        \parbox[t]{12cm}{\textbf{#2} - \textcolor{bgcol}{#3}} & \parbox[t]{4.5cm}{\vspace{2.5pt}\textcolor{sectcol}{#1}}
    \end{tabular*}

    \vspace{-8pt}
    \textcolor{softcol}{\hrule}
    \vspace{6pt}
}




% creates a stretched box as 
\newcommand{\cveventmeta}[2]
{
	\mbox{\mystrut \hspace{87pt}\textit{#1}}\\
	#2
}
\newenvironment{highlights}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=0.4 cm
    ]
}{
    \end{itemize}
}
 % new environment for highlights for bullet entries

\newenvironment{onecolentry}{
    \begin{adjustwidth}{
        0.2 cm + 0.00001 cm
    }{
        0.2 cm + 0.00001 cm
    }
}{
    \end{adjustwidth}
} % new environment for one column entries


\newcommand{\mystrut}{\rule[-.3\baselineskip]{0pt}{\baselineskip}}
 % Remove paragraph indentation


	

