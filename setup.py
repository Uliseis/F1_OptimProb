import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="group08",
    version="1.0.0",
    author="Group08",
    author_email="ui.bertolo@alumnos.upm.es; mihail.neagu@alumnos.upm.es; jose.llopez@alumnos.upm.es",
    description="Heuristic optimization 1st practical work, by Group 08.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
