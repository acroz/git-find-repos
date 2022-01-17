from typing import Iterable
import argparse
import os
import os.path


def is_git_repo(path: str) -> bool:
    return os.path.isdir(os.path.join(path, ".git"))


def find_repos(path: str) -> Iterable[str]:
    for child in os.scandir(path):
        if child.is_dir():
            if is_git_repo(child):
                yield child
            else:
                yield from find_repos(child)


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()

    for repo_path in find_repos(args.path):
        print(os.path.relpath(repo_path, start=args.path))
