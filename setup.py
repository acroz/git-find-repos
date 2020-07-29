from pathlib import Path
from setuptools import setup


SOURCE_ROOT = Path(__file__).parent
README = SOURCE_ROOT / "README.rst"


setup(
    name="git-find-repos",
    description="CLI tool to find git repositories.",
    long_description=README.read_text(),
    author="Andrew Crozier",
    author_email="wacrozier@gmail.com",
    url="https://github.com/acroz/git-find-repos",
    project_urls={"GitHub": "https://github.com/acroz/git-find-repos"},
    license="MIT",
    py_modules=["git_find_repos"],
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["git-find-repos=git_find_repos:main"]},
)
