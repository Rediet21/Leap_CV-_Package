# Leap_CV_Package
Leap package to generate CV pdf with latex designs

# LaTeXGen - LaTeX Document Generator

LaTeXGen is a Python package designed to automate the process of generating LaTeX documents using predefined templates. The package is useful for generating resume.It can also automate the installation of required LaTeX packages and tools, ensuring that the necessary dependencies are met.

## Features

- **Template-Based Generation**: Generate LaTeX documents based on a variety of templates.
- **Automated Package Management**: Install necessary LaTeX packages automatically if they are not present.
- **Font Management**: Automatically copy required fonts to the correct locations.


## Installation

### Windows
For Windows, LaTeXGen will download and install MiKTeX if it is not already installed on your system.

# Installing the package using pip

pip install Leap-CV==0.2

# Usage
To generate a LaTeX document, use the latexgen command followed by the .tex file and the desired template name.

leap <latex-file.tex> [design-name]

# Example 
latexgen my_resume.tex modern

## Use the .tex file you got from leap with corresponding design name (3 designs are provided choose the one that correspods with your .tex file)
leap xxx.tex modern
leap xxx.tex classic
leap xxx.tex minimal