%----------------------------------------------------------------------------------------
%	CLASS CONFIGURATION
%----------------------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cvlfoc}[2023/11/10 LFOC CV Class]
\RequirePackage{ifthen}

\newboolean{highlights}
\setboolean{highlights}{false}
\DeclareOption{highlights}{\setboolean{highlights}{true}}

\newboolean{publist}
\setboolean{publist}{false}
\DeclareOption{publist}{\setboolean{publist}{true}}

\newboolean{grants}
\setboolean{grants}{false}
\DeclareOption{grants}{\setboolean{grants}{true}}

\DeclareOption{11pt}{\PassOptionsToClass{11pt}{article}}
\DeclareOption{12pt}{\PassOptionsToClass{12pt}{article}}
\ExecuteOptions{11pt}

\DeclareOption*{
	\PackageWarning{dfgtex}{Unknown option `\CurrentOption'}
}

\ProcessOptions
\LoadClass{article}


%----------------------------------------------------------------------------------------
%	PACKAGES AND CONFIGURATIONS
%----------------------------------------------------------------------------------------
\RequirePackage{calc}
\RequirePackage{graphicx}
\RequirePackage[right]{eurosym}

\RequirePackage{iftex}
\ifpdftex
	\RequirePackage[utf8]{inputenc}
	\RequirePackage[T1]{fontenc}
\fi

% Redefine title macro
\renewcommand*{\title}[2][]{
\def\temp{#1}\ifx\temp\empty
	\gdef\@shorttitle{#2}
\else
	\gdef\@shorttitle{#1}
\fi
\gdef\@title{#2}
}

% Redefine author macro
\renewcommand*{\author}[2][]{
\def\temp{#1}\ifx\temp\empty
	\gdef\@shortauthor{#2}
\else
	\gdef\@shortauthor{#1}
\fi
\gdef\@author{#2}
}

% email
\newcommand{\email}[1]{\gdef\@email{#1}}

% Website
\newcommand{\website}[1]{\gdef\@website{#1}}

% Google scholar url
\newcommand{\gscholar}[1]{\gdef\@gscholar{#1}}

% ORCID number
\newcommand{\orcid}[1]{\gdef\@orcid{#1}}

% Number of publications
\newcommand{\publications}[1]{\gdef\@publications{#1}}

% Number of citations
\newcommand{\citations}[1]{\gdef\@citations{#1}}

% h-index
\newcommand{\hindex}[1]{\gdef\@hindex{#1}}

% Width of right column
\newlength{\rcolwidth}
\settowidth{\rcolwidth}{00/0000--00/0000}
\addtolength{\rcolwidth}{8mm}

% Gap between columns
\newlength{\colgap}
\setlength{\colgap}{4mm}

% Spacing between entries
\newlength{\entrysep}
\setlength{\entrysep}{0.4\baselineskip}


%----------------------------------------------------------------------------------------
%	PAGE LAYOUT
%----------------------------------------------------------------------------------------
\RequirePackage{geometry}
\geometry{
	paper=a4paper,
	top=1.2cm,
	bottom=1.2cm,
	left=1.6cm,
	right=1.6cm,
	includehead,
	headheight=\baselineskip,
	headsep=0.5cm,
%	showframe,
}

\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhead{}
\fancyhead[l]{\normalfont\small\color{another.blue}\MakeUppercase{\@shortauthor\ --- \@shorttitle}}
\fancyhead[c]{}
\fancyhead[r]{\normalfont\small\color{another.blue}\thepage}
\fancyfoot{}
%\renewcommand{\headrulewidth}{0pt}

\RequirePackage{titlesec}
\titleformat*{\section}{\color{stutt.blue}\Large\bfseries\MakeUppercase}
\titlespacing*{\section}{0pt}{*2.3}{*0}

\titleformat*{\subsection}{\color{black}\large\itshape}
\titlespacing*{\subsection}{0pt}{*1}{*0}


%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------
\RequirePackage{fontawesome5}
\RequirePackage[default]{raleway}
\renewcommand*{\familydefault}{\sfdefault}

\RequirePackage{xcolor}
\definecolor{stutt.blue}{RGB}{0,81,158}
\definecolor{another.blue}{RGB}{15,55,149}
\definecolor{link}{RGB}{25,50,179}
\definecolor{stutt.darkblue}{RGB}{0,50,98}
\definecolor{stutt.lightblue}{RGB}{0,190,255}
\definecolor{stutt.gray}{RGB}{62, 68, 76}
\definecolor{normal.text}{RGB}{33, 36, 39}
\color{normal.text}


%----------------------------------------------------------------------------------------
%	STRUCTURE
%----------------------------------------------------------------------------------------
\setlength{\parindent}{0mm} % Suppress paragraph indentation

\RequirePackage{hyperref}
\hypersetup{colorlinks=true, urlcolor=stutt.blue, citecolor=stutt.blue, linkcolor=stutt.blue,%
			pdfstartview=FitV, pageanchor}

\RequirePackage{enumitem}
\setlist[itemize]{nosep, topsep=0pt, itemsep=3pt, left=-1pt .. 9pt,
	label={\color{stutt.lightblue}\raisebox{-0.15em}{\scalebox{1.5}{\textbullet}}}
}

% Title section
\renewcommand{\maketitle}{
	\thispagestyle{empty}

	\begin{spacing}{1}
	{\fontsize{36pt}{0pt}\selectfont\color{another.blue}\bfseries\hspace{-0.12ex}\MakeUppercase{\@author}}

	\vspace{-0.3\baselineskip}{\color{stutt.gray!30}\rule{\textwidth}{1pt}}

	\vspace{0.15\baselineskip}
	\textcolor{stutt.blue}{\faEnvelope}%
	\hspace{1ex}%
	{\small\raisebox{0.6pt}{\href{mailto:\@email}{\textbf{\@email}}}}
	%
	\hfill
	%
	\textcolor{stutt.blue}{\faGlobe}%
	\hspace{1ex}%
	{\small\raisebox{0.6pt}{\href{https://\@website}{\textbf{\@website}}}}%
	\end{spacing}
}


%----------------------------------------------------------------------------------------
%	BIBLIOGRAPHY
%----------------------------------------------------------------------------------------
\RequirePackage[backend=bibtex, maxnames=10, sorting=ydnt, defernumbers=true,%
				style=trad-abbrv]{biblatex}

\DeclareFieldFormat{addendum}{\space\textbf{[#1]}}
\DeclareBibliographyCategory{highlighted}

\defbibenvironment{bibstarred}{%
\list
{\ifcategory{highlighted}{\makebox[0pt][r]{\raisebox{1.7pt}{\tiny\faStar}~}}{}%
\printtext[labelnumberwidth]{\printfield{labelprefix}\printfield{labelnumber}}}
{\setlength{\parskip}{0pt}
\setlength{\itemsep}{3pt}
\setlength{\parsep}{0pt}
\setlength{\labelsep}{0.7\biblabelsep}
}
}{\endlist}
{\item}

\defbibenvironment{bibhighlights}{%
\list
{\printtext[labelnumberwidth]{\printfield{labelprefix}\printfield{labelnumber}}}
{\setlength{\parskip}{0pt}
\setlength{\itemsep}{3pt}
\setlength{\parsep}{0pt}
\setlength{\labelsep}{0.7\biblabelsep}
}
}{\endlist}
{\item\clearfield{url}}


\defbibenvironment{bibliography}{%
\list
{\printtext[labelnumberwidth]{\printfield{labelprefix}\printfield{labelnumber}}}
{\setlength{\parskip}{0pt}
\setlength{\itemsep}{3pt}
\setlength{\parsep}{0pt}
\setlength{\labelsep}{0.7\biblabelsep}
}
}{\endlist}
{\item}


%----------------------------------------------------------------------------------------
%	ENTRY LIST
%----------------------------------------------------------------------------------------
\RequirePackage{paracol} % Required for tables that span multiple pages
\setcolumnwidth{\rcolwidth/\colgap,}
\newcommand{\mystrut}{\rule{0pt}{12pt}}

\newenvironment{entrydate}{%
	\begin{paracol}{2}
}{
	\end{paracol}
}

\newcommand{\entry}[2]{%
	\begingroup
	\raggedleft
	\small #1 \mystrut\par
	\endgroup
	\switchcolumn
	\mystrut#2
	\switchcolumn*
}

\newcommand{\entrydetail}[4]{%
	\begingroup
	\raggedleft
	\small #1\mystrut\par
	\endgroup
	\switchcolumn
	\mystrut\textbf{#2}%
	\hfill%
	#3
	\def\temp{#4}\ifx\temp\empty

	\else
	  \\#4%
	\fi
	\vspace{\entrysep}
	\switchcolumn*
}

\newcommand{\entrylist}[2]{%
	\begingroup
	\raggedleft
	\small #1\mystrut\par
	\endgroup
	\switchcolumn
	\vspace*{-\baselineskip}
	\mystrut\begin{itemize}
	#2
	\end{itemize}
	\vspace{\entrysep}
	\switchcolumn*
}

\newcommand{\citationstat}{
	\vspace{-0.3\baselineskip}{\color{stutt.gray!30}\rule{\textwidth}{1pt}}

	\begingroup
		\small
		Total number: \@publications
		\hfill
		Citations: \@citations
		\hfill
		h-index: \@hindex
	\endgroup
	\hfill
	\vspace{0.5\baselineskip}
	\textcolor{stutt.blue}{\small\faGraduationCap}%
	\hspace{0.65ex}%
	{\small\raisebox{0.1pt}{\href{\@gscholar}{\textbf{Google Scholar}}}}
	\hfill
	\hspace{1pt}%
	\textcolor{stutt.blue}{\small\faOrcid}%
	\hspace{0.92ex}%
	{\footnotesize\raisebox{0.3pt}{\href{https://orcid.org/\@orcid}{\textbf{\@orcid}}}}

	\vspace{-\baselineskip}{\color{stutt.gray!30}\rule{\textwidth}{1pt}}

	\vspace{\baselineskip}
}

\newcommand{\entryhighlights}{%
	\begingroup
	\footnotesize
	Total number: \@publications\mystrut

	Citations: \@citations\mystrut

	h-index: \@hindex\mystrut
	\endgroup

	\vspace{0.5\baselineskip}
	\textcolor{stutt.blue}{\small\faGraduationCap}%
	\hspace{0.65ex}%
	{\footnotesize\raisebox{0.15pt}{\href{\@gscholar}{\textbf{Google Scholar}}}}\mystrut

	\hspace{1pt}%
	\textcolor{stutt.blue}{\small\faOrcid}%
	\hspace{0.92ex}%
	{\scriptsize\raisebox{1.25pt}{\href{https://orcid.org/\@orcid}{\textbf{\@orcid}}}}\mystrut

	\vspace{\baselineskip}
  	{\small See complete list on
  		\hyperlink{page.\getpagerefnumber{S:publist}}{p.~\getpagerefnumber{S:publist}}}
	\switchcolumn
	\mystrut\\
	\vspace{-36.2pt}
  	\printbibliography[env=bibhighlights, heading=none, resetnumbers=true, category=highlighted]
	\switchcolumn*
}

\newcommand{\entrybib}[2]{%
	\begingroup
	\raggedleft
	\textbf{\large #1}\mystrut\par
	\endgroup
	\switchcolumn
	\mystrut\\
	\vspace{-36.2pt}
  	\printbibliography[env=bibstarred, heading=none, resetnumbers=true, keyword=#2]
	\switchcolumn*
}
