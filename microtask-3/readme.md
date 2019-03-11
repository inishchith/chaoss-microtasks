## Microtask #3

In this microtask, we'll try and understand the meaning of some of the attributes of JSON documents produced by Perceval and its source code.

And also in the later half will list and explain some of the `Git` commands used by Perceval backend.

Attributes of the JSON documents produced by the Perceval and its source code that we tried executing in the earlier [Microtask : #2](../Microtask-2) are as follows:

```
[
    'backend_name',
    'backend_version',
    'perceval_version',
    'timestamp',
    'origin',
    'uuid',
    'updated_on',
    'category',
    'tag',
    'data'
]
```

Now, we'll understand what each of them mean

<hr>

#### `timestamp` :

- The `timestamp` attribute is a [Unix Timestamp](https://en.wikipedia.org/wiki/Unix_time) conversion of the time when the `.fetch()` method is executed in UTC (Universal Time Coordinated) time scale using one of the Perceval backends.


- References:

    1. [setting value of timestamp attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L160)


#### `updated_on` :

- The `updated_on` attribute is a Unix Timestamp conversion of last update datetime in UTC (Universal Time Coordinated) time scale, set via retrieving the `update time` of the GitHub Item. ( More like last modified time )


- References:

    1. [setting value of updated_on attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L163)
    2. [extracting timestamp from update time of item](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L186)


#### `origin` :

- The `origin` attribute is identifier of the origin url from where the data is to be fetched.

- For example
    - In case of Perceval's `GitHub` Backend, the origin is set to the GITHUB_URL + owner + repository . i.e in my case : `https://github.com/inishchith/MeetInTheMiddle`


- References:

    - [setting the value of origin attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L95)


#### `category` :

- The `category` attribute is the category of item to be fetched from the origin ( the data source )


- for example
    - In case of `Git` Backend, the category of item that is available to be fetched is [commit]()
    - In case of `GitHub` Backend, we can fetch information about [issues]() & [pull requests]()


- References:

    - [issue, pull-request & repository in case of github backend](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L40)


#### `uuid` :

- `uuid` ( uniqure identifier ) attribute is the SHA-1 Hash of the string. A string is our case is formed via concatination of the values from a list using `:` ( colon symbol ).

- for example
    - `uuid` in case of each commit information fetched via `Git` Backend is SHA-1 Hash of the `<origin>:<commit>`.
    - In case of each item fetched via `GitHub` Backend, the SHA-1 Hash is of the string `<origin>:<id>`.

- References:

    1. [setting value of uuid](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L162)
    2. [concatination of list and sha-1](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L427)


<hr>

- Common git commands used by Perceval backend
    - clone
    - log
    - count-objects
    - show
    - fetch
    - prune

#### `git clone`:

- `clone` command is used to make a local copy of the repository which contains
    - A .git subfolder with all the git related revision history of your repo
    - A working tree, or checked out copies of your project files.
- Perceval's `Git backend` uses an additional option `--bare` in order to make a bare copy of the repository.
    - [`--bare`](https://git-scm.com/docs/git-clone#git-clone---bare) : In a bare repository, git version history is placed in root directory instead of .git directory with no source files. bare repositories are customarily given a .git extension

- `command`

```
    $ git clone --bare <repository_url> <local_dir_path>
```

#### `git log`:

- `log` command is used to view the commit history of a git repository
- Perceval's `Git backend` uses two additional option `--reverse` and `--topo-order`.
    - [`--reverse`](https://git-scm.com/docs/git-log#git-log---reverse) shows the commit history in reverse i.e `older to newer` order.
    - [`--topo-order`](https://git-scm.com/docs/git-log#git-log---topo-order) is used to show branch commit in a convenient manner. 

- `command`

```
    $ git log --reverse --topo-order
```

#### `git count-objects`:

- `count-objects` counts the number of unpacked object files and disk space consumed by them, to help you decide when it is a good time to repack.

- `command`

```
    $ git count-objects -v
```

Note: `-v` flag is used for verbose output.

<hr>
<div align="center">
    <b> This concludes microtask #3 ;) </b>
</div>
