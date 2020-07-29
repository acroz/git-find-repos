from pathlib import Path
from typing import Iterable
import argparse
import sys
import termcolor


def is_git_repo(path: Path) -> bool:
    return (path / ".git").is_dir()


def find_git_repos(path: Path) -> Iterable[Path]:
    for child in path.iterdir():
        if child.is_dir():
            if is_git_repo(child):
                yield child
            else:
                yield from find_git_repos(child)


MESSAGE = """
find-git-repos has been renamed to git-find-repos. Please use it instead.
Find it at: https://github.com/acroz/git-find-repos
""".strip()


def main() -> None:

    print(termcolor.colored(MESSAGE, "yellow"), file=sys.stderr)

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    for repo_path in find_git_repos(args.path):
        print(repo_path.relative_to(args.path))
