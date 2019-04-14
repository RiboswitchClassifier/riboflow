import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riboflow",
    version="0.1dev",
    author="Keshav Aditya R.P",
    author_email="keshavaditya26896@gmail.com",
    description="A utility package to classify different Riboswitch Sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KeshavAdityaRP/riboflow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)      