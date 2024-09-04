import subprocess
import requests
import os
import sys
import time
from pathlib import Path
from shutil import copytree
import sys
import platform



sys.path.append(os.path.dirname(__file__))
from latex_ops import generate_tex_file
#sys.path.append('C:/Users/HP/Desktop/Leap/for users/Leap_CV-_Package/leap')
import json



def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print(f"Downloaded {filename}")

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
    if process.returncode != 0:
        raise Exception(f"Command '{command}' failed with exit code {process.returncode}")

def is_package_installed(package):
    try:
        # Check if the package is already installed
        result = subprocess.run(['mpm', '--list'], capture_output=True, text=True)
        return package in result.stdout
    except subprocess.CalledProcessError:
        return False

def install_latex_packages():
    # List of the packages required
    packages = ['raleway', 'moresize', 'fancyhdr', 'multirow']
    
    for package in packages:
        if is_package_installed(package):
            print(f"{package} is already installed. Skipping installation.")
        else:
            try:
                print(f"Installing {package}...")
                subprocess.check_call(['mpm', '--install=' + package])
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}. Please check if MiKTeX is installed and accessible.")
                sys.exit(1)

def check_file_exists(filename):
    return os.path.isfile(filename)

def check_miktex_installed():
    try:
        result = subprocess.run(['pdflatex', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def set_path():
    miktex_path = r"C:\Program Files\MiKTeX\miktex\bin\x64"
    if miktex_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + miktex_path
        subprocess.call(f'setx PATH "%PATH%;{miktex_path}"', shell=True)
        print(f"PATH updated to include {miktex_path}")
    else:
        print(f"PATH already includes {miktex_path}")

def wait_for_miktex_installation(installer_filename, timeout=300):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if check_miktex_installed():
            print("MiKTeX installation detected.")
            return True
        print("Waiting for MiKTeX installation to complete...")
        time.sleep(10)
    print("Timeout waiting for MiKTeX installation.")
    return False


def install_linux_dependencies():
    try:
        # Update the package list
        # Run all the commands in one go using shell=True
        subprocess.check_call(
            "sudo apt-get install -y \
            texlive-latex-base \
            texlive-fonts-recommended \
            texlive-latex-extra \
            texlive-fonts-extra\
            texlive-xetex \
            && sudo apt-get clean",
            shell=True
        )
        subprocess.check_call([sys.executable, "-m", "pip", "install", "jinja2"])
        print("All packages installed successfully.")

        # Clean up the package list
        

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
        raise

def is_texlive_installed():
    try:
        # Run `tex --version` to check if TeX Live is installed
        result = subprocess.run(["tex", "--version"], capture_output=True, text=True)
        # Check if the command executed successfully
        if result.returncode == 0:
            print("TeX Live is already installed.")
            return True
    except FileNotFoundError:
        # `tex` command not found, TeX Live is not installed
        print("TeX Live is not installed.")
    return False

def install_jinja2():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "jinja2"])
        print("Jinja2 installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing Jinja2: {e}")
        raise


def compile_latex(json_file, template_name):
    
    install_jinja2()
    current_os = platform.system()
    if current_os == "Linux":
        if not is_texlive_installed():
            install_linux_dependencies()
        else:
            print("Skipping Texlive installation")
    else: 

        installer_filename = "basic-miktex-24.1-x64.exe"
        miktex_url = "https://miktex.org/download/ctan/systems/win32/miktex/setup/windows-x64/basic-miktex-24.1-x64.exe"
        
        if not check_file_exists(installer_filename):
            if not check_miktex_installed():
                print("MiKTeX installer not found. Downloading...")
                download_file(miktex_url, installer_filename)
        else:
            print("MiKTeX installer already downloaded.")

        # Step 2: Install MiKTeX if not already installed
        if not check_miktex_installed():
            print("MiKTeX not found. Installing...")
            install_process = subprocess.Popen(installer_filename, shell=True)
            print("Installation started. Waiting for it to complete...")
            if wait_for_miktex_installation(installer_filename):
                print("MiKTeX installation completed.")
            else:
                print("MiKTeX installation failed or timed out.")
                sys.exit(1)
        else:
            print("MiKTeX already installed.")
        
        # Step 3: Set PATH for Environment Variable
        set_path()
        
        # Wait a bit to ensure the environment variable is updated
        time.sleep(5)
        
        # Step 4: Automate Package Management
        run_command('initexmf --mkmaps')
        run_command('initexmf --update-fndb')
        run_command('pip install jinja2')
        install_latex_packages()


    #finding path of the json
    json_file_path = Path(json_file)

    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_resume = json.load(f)

    # Path to the templates directory within the package
    template_dir = Path(__file__).resolve().parent / 'templates'
    dstn_path = Path(json_file).parent
    design_source_dir = template_dir  / f"{template_name}"
    design_dstn_dir = Path(json_file).parent / f"{template_name}"

    # Copy the fonts directory to the location of the latex_file
    if not design_dstn_dir.exists():
        copytree(design_source_dir, design_dstn_dir)
        print(f"template directory copied to {design_dstn_dir}")
    else:
        print(f"template directory already exists at {design_dstn_dir}")


    tex_file_path = generate_tex_file(json_resume, design_dstn_dir, design_dstn_dir)
    if tex_file_path:
        print(f".tex file generated at: {tex_file_path}")
    else:
        print("Failed to generate .tex file.")
    
    # Step 5: Compile LaTeX File
    print(f"Compiling resume.tex with template {template_name}.cls...")

    fonts_source_dir = Path(__file__).resolve().parent  / 'fonts'
    fonts_dest_dir = Path(json_file).parent / f"{template_name}" / 'fonts'

    if not fonts_source_dir.is_dir():
        print("Fonts directory not found.")
        sys.exit(1)

     # Copy the fonts directory to the location of the latex_file
    if not fonts_dest_dir.exists():
        copytree(fonts_source_dir, fonts_dest_dir)
        print(f"Fonts directory copied to {fonts_dest_dir}")
    else:
        print(f"Fonts directory already exists at {fonts_dest_dir}")


    resume_tex_path = design_dstn_dir / "resume.tex"

    # Change the current working directory to design_dstn_dir
    os.chdir(design_dstn_dir)

    # Construct the LaTeX command
    if template_name == "minimal":
        latex_command = f"xelatex -interaction=nonstopmode {resume_tex_path.name}"  # Only use the filename
    else:
        latex_command = f"pdflatex -jobname={resume_tex_path.stem} -synctex=1 -interaction=nonstopmode {resume_tex_path.name}"

    # Run the appropriate LaTeX compiler
    run_command(latex_command)

    




def main():
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: latexgen <latex-file> [template-name]")
        sys.exit(1)

    json_file = sys.argv[1]
    template_name = sys.argv[2] if len(sys.argv) == 3 else 'default'

    compile_latex(json_file, template_name)

if __name__ == "__main__":
    main()
