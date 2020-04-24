import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fttlib",
    version="1.1.2",
    author="Bron Davies",
    author_email="bron@brontech.com",
    description="A library of helper methods for your Python project to get mime types and general file category",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brondavies/filetypetranslator",
    keywords=["file", "type", "mime", "mapping", "path", "inspection", "upload", "download", "email", "FTT"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)