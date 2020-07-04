from pathlib import Path
from setuptools import setup


SOURCE_ROOT = Path(__file__).parent
README = SOURCE_ROOT / "README.rst"


setup(
    name="find-git-repos",
    description="CLI tool to find git repositories.",
    long_description=README.read_text(),
    author="Andrew Crozier",
    author_email="wacrozier@gmail.com",
    url="https://github.com/acroz/find-git-repos",
    project_urls={"GitHub": "https://github.com/acroz/find-git-repos"},
    license="MIT",
    py_modules=["find_git_repos"],
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["find-git-repos=find_git_repos:main"]},
)
