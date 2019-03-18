## Microtask #7

- Based on the JSON documents produced by Graal and its source code, try to answer the following questions:

<hr>

### # Which are the common methods of the Graal backends?

#### `fetch()`

- With the help of Perceval's `Git` backend, `fetch()` retrieves from a Git repository a list of commits and supports the inclusion of code analysis information.
- Commits are returned in the same order they were obtained.

**NOTE:** All the below methods which are common across `Graal` backends requires a `Perceval`'s commit object from it's `Git` backend.
<br>

#### `_filter_commit()`:

- This method filters a commit from a local Git repository according to its data (e.g. author, sha, etc.)

#### `_analyze()`:

- This method analyzes a commit and the corresponding checkout version of the repository.
- For example: In case of `CoLic` Backend analysis can be performed on license information with the help of either NOMOS or SCANCODE tool.

#### `_post()`:

- This method performs operation (e.g. removing some attributes from the commit generator) on the Graal item obtained.

<hr>

### # List and explain at least 2 Git commands used by Graal (and not implemented in Perceval)

#### `git worktree`:

- This command helps us create a working tree of the cloned repository with the active branch set to `master` by default.
- With this we're able to perform `checkout` operations on the repository which cannot be performed on a cloned `bare` repository.
- `command`:

```
    # To attach a worktree
    $ git worktree add <worktree_path> <branch_name>

    # When you are done with a linked working tree you can simply prune it.
    $ git worktree prune
```

#### `git checkout`:

- This command helps us checkout all the content of the repository for a given commit hash.
- With this the content at every commit can be individually analyzed.
- `command`:

```
    # to checkout a commit
    $ git checkout <commit_hash>
```

- [Reference](https://github.com/chaoss/grimoirelab-graal/blob/541ce6739f9352f58223b01de1c8a5d9f206957f/graal/graal.py#L316)

<hr>
<div align="center">
    <b> This concludes microtask #7 </b>
</div>
