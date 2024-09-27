import os
import jinja2

import json

# Load the JSON file
#json_file_path = "C:/Users/HP/Desktop/Leap/for users/Leap_CV-_Package/tex/json_resume.json"

# Read the JSON file and load it into a dictionary

def escape_for_latex(data):
    if isinstance(data, dict):
        return {key: escape_for_latex(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [escape_for_latex(item) for item in data]
    elif isinstance(data, str):
        latex_special_chars = {
            "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
            "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\^{}",
            "\\": r"\textbackslash{}", "\n": "\\newline%\n", 
            "\xA0": "~", "[": r"{[}", "]": r"{]}"
        }
        return "".join([latex_special_chars.get(c, c) for c in data])
    return data



def use_template(jinja_env, json_resume):
    try:
        resume_template = jinja_env.get_template("resume.tex.jinja")
        return resume_template.render(json_resume)
    except Exception as e:
        print(f"Error in template rendering: {e}")
        return None

def generate_tex_file(json_resume, dst_path, template_dir):
    try:
        latex_jinja_env = jinja2.Environment(
            block_start_string=r"\BLOCK{", block_end_string="}",
            variable_start_string=r"\VAR{", variable_end_string="}",
            comment_start_string=r"\#{", comment_end_string="}",
            line_statement_prefix="%-", line_comment_prefix="%#",
            trim_blocks=True, autoescape=False,
            loader=jinja2.FileSystemLoader(template_dir),
        )

        escaped_json_resume = escape_for_latex(json_resume)
        resume_latex = use_template(latex_jinja_env, escaped_json_resume)

        tex_temp_path = os.path.join(dst_path, "resume.tex") 

        with open(tex_temp_path, "w") as tex_file:
            tex_file.write(resume_latex)

        return tex_temp_path

    except Exception as e:
        print(f"Error generating .tex file: {e}")
        return None
