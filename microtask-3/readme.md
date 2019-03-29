## Microtask #3

- In this microtask, we'll try and understand the meaning of some of the attributes of JSON documents produced by Perceval and its source code.
- Understand which are the common methods of the Perceval backends
- And also in the later half will list and explain some of the `Git` commands used by Perceval backend.

<hr>
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

- The `timestamp` attribute is used to know the datetime when the item was fetched from the data source.
- The corresponding items are fetched using one of the common method of Perceval Backend i.e `.fetch()` method ( used to retrieve data extracted from 30+ tools ).

**Note:** The attribute is represented in [Unix Timestamp](https://en.wikipedia.org/wiki/Unix_time) conversion.

* References:

  1. [setting value of timestamp attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L160)

#### `updated_on` :

- The `updated_on` attribute is used to know the datetime when the item was last updated in the data source.
- It is set via retrieving the `update time` of the Item. ( More like last activity )

**Note:** The attribute is represented in [Unix Timestamp](https://en.wikipedia.org/wiki/Unix_time) conversion.

* References:

  1. [setting value of updated_on attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L163)
  2. [extracting timestamp from update time of item](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L186)

#### `origin` :

- The `origin` attribute is identifier of the data source i.e origin url, from where the data is to be fetched.

- For example
  - In case of Perceval's `GitHub` Backend, the origin is set to the GITHUB_URL + owner + repository .
  - i.e In most cases, I've used : `https://github.com/inishchith/MeetInTheMiddle` as the source of data.

* References:

  - [setting the value of origin attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L95)

#### `category` :

- The `category` attribute is the category of item to be fetched from the origin ( the data source ).

* for example
  - In case of `Git` Backend, the category of item that is available to be fetched is [commit]()
  - In case of `GitHub` Backend, we can fetch information about [issues]() & [pull requests]()

- References:

  - [issue, pull-request & repository in case of github backend](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L40)

#### `uuid` :

- `uuid` attribute is a unique identifier of every item extracted with the help of Perceval.
- The attribute is represented in the form of SHA-1 Hash of the string. A string is our case is formed via concatenation of the values from a list using `:` ( colon symbol ).

- for example

  - `uuid` in case of each commit information fetched via `Git` Backend is SHA-1 Hash of the `<origin>:<commit>`.
  - In case of each item fetched via `GitHub` Backend, the SHA-1 Hash is of the string `<origin>:<id>`.

- References:

  1. [setting value of uuid](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L162)
  2. [concatenation of list and sha-1](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L427)

<hr>

- Which are the common methods of the Perceval backends?
  - fetch()
  - metadata()
    - metadata_id()
    - metadata_updated_on()
    - metadata_category()
  - has_resuming()
  - has_archiving()


#### `fetch()`:

- This method is one of the core methods of `Perceval` Backends and is used to fetch information from the particular tools.
- The method leverages on `fetch_items()` method which is implemented for each of the backend tool available, which iteratively fetches each item's information using some parameters such as
  - `category`
  - `from_data` & `to_date`
  - many more ( some specific to particular backend )

* References:

  - [fetch() method](https://github.com/chaoss/grimoirelab-perceval/blob/1558be17fccfdabfc33d37571bbcc495e8bcb5c1/perceval/backend.py#L106)

#### `metadata()`:

- This method is used to add metadata about when the information was retrieved, category and id.
- The method is executed on every `fetch()` method call in order to have a log of when the item was last updated.
- The method leverages on three other methods which are specific for the backends :
  - `metadata_id()` : extracts identifier from an item
  - `metadata_updated_on()` : extracts the last updated datetime of the item and converts it into a UNIX timestamp format.
  - `metadata_category()` : extracts the category of the item.
- **Note:** for some of the backends this method is overridden

#### `has_resuming()`:

- This method is implemented for each of the backend, returns whether the backend tool supports resuming the fetch process.

#### `has_archiving()`:

- This method is implemented for each of the backend, returns whether the backend tool supports archiving items on the fetch process.


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

  - [`--bare`](https://git-scm.com/docs/git-clone#git-clone---bare) : In a bare repository, git version history is placed in root directory instead of .git directory with no source files.
  - bare repositories are customarily given a .git extension

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

- Note: `-v` flag is used for verbose output.

<hr>
<div align="center">
    <b> This concludes microtask #3 ;) </b>
</div>
