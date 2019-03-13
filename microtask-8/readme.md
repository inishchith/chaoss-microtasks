## Microtask #8

- In this microtask, given a commit SHA and a Git repository, we'll create a Python script to execute flake8 for a given commit of any Git repository.

<hr>

- We'll be using the `subprocess` module to perform `git` related operations on the repository.
- Then after checking out to the specific commit, we can execute `flake8 .` on the repository
- [Jupyter notebook](./flake8_checks.ipynb) | [Script](./flake8_checks.py)
- Alternatively, we can use [ GraalRepository ](https://github.com/chaoss/grimoirelab-graal/blob/8b286c19e6a9d7e0c89fa67035546e3b81d9afb3/graal/graal.py#L260) which provides `git` operations such as checkout, worktree, delete and more.
