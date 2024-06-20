import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()


__version__ = "0.0.0"

REPOSITORY = "Briefly"
AUTHOR_USER_NAME = "AbhinavMangalore16"
SRC_REPO = "Briefly"
AUTHOR_EMAIL = "abhinavm16104@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for NLP Text Summarization",
    long_description=description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPOSITORY}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPOSITORY}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
