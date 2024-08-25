from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Leap-CV',
    version='0.3',
    author="10 Academy",
    packages=find_packages(),
    description="Cv Generation Package",
    long_description=long_description,  # This is where the project description goes
    long_description_content_type="text/markdown",  # Type of the long description
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'leap=leap.leap:main',  # Ensure this matches your module and function
        ],
    },
    package_data={
        'leap': ['templates/*/*' ,# Include all .cls files in the templates directory
                'fonts/*',  # Include all files in the fonts directory
                ],
    },
    include_package_data=True,
)