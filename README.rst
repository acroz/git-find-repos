find-git-repos
==============

A simple CLI tool for finding git repositories.

Installation
------------

.. code-block:: sh

   pip install find-git-repos

You may wish to install using `pipx <https://pipxproject.github.io/pipx/>`_,
which manages a virtual environment for ``find-git-packages`` for you.

Usage
-----

``find-git-repos`` will search recursively in the current directory for git
repositories when invoked with no arguments:

.. code-block:: sh

   find-git-repos

Alternatively, you can pass a directory to search:

.. code-block:: sh

   find-git-repos ~/src

I created this tool to aid navigating between repositories on my computer. I
organise respostories in subdirectories corresponding to their HTTPS/SSH URLs
on GitHub, Bitbucket and GitLab, e.g.:

* ~/src/github.com/acroz/pylivy
* ~/src/bitbucket.org/acroz/other-repo
* ~/src/gitlab.com/organisation/group/subgroup/repo

To facilitate switching between repos quickly, I define a ``zsh`` function in
my ``.zshrc`` shell configuration file that pipes the output of
``find-git-repos`` to `fzy <https://github.com/jhawthorn/fzy>`_ for fuzzy
matching.

.. code-block:: zsh

   function repo {
       initial_query=$1
       dest=$(find-git-repos ~/src | fzy -q "$initial_query" -l 20) && cd "$HOME/src/$dest"
   }

When I need to switch to a repo, I run ``repo`` in my shell, type enough of the
name to match the repo name, then hit enter to exit ``fzy`` and switch to the
selected repo.
