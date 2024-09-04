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
For Windows, Leap_CV will download and start the installation MiKTeX if it is not already installed on your system.

While the package installs Miktex compiler, you will be prompted to choose between installing it "For anyone who uses this computer" or "only For me only" . Please ensure that you select the "For anyone who uses this computer" option to avoid any potential permission issues or access restrictions.

# Installing the package using pip

pip install Leap-CV

# Usage
To generate a CV , use the leap command followed by the json_resume.json file and the desired template name.

cd folder_directory
leap <json_resume.json> [design-name]

# Example 
leap json_resume.json modern
leap json_resume.json classic
leap json_resume.json minimal

## Use the .json file you got from leap with any design (modern, classic and minimal) that you want to generate with
leap json_resume.json modern



