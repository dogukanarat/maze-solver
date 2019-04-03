import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maze-solver-dogukanarat",
    version="0.0.1",
    author="Doğukan Fikri Arat",
    author_email="aratdogukan@gmail.com",
    description="A maze solver package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ieee-uv-project/maze-solver",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
