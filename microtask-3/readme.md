### Microtask #3

In this microtask, i'll try and explain the meaning of some of the attributes of JSON documents produced by Perceval and its source code.

In short listing & explaining -

#### What is the meaning of the JSON attribute

    - `timestamp`
    - `updated_on`
    - `origin`
    - `category`
    - `uuid`

- And also in the later half will list and explain some of the `Git` commands used by Perceval backend.

<hr>

Attributes of the JSON documents produced by the Perceval and its source code that we tried executing in the earlier [microtask (#2)](../Microtask-2) are as follows:

```
['backend_name', 'backend_version', 'perceval_version', 'timestamp', 'origin', 'uuid', 'updated_on', 'category', 'tag', 'data']
```

<hr>

#### `timestamp` :

- The `timestamp` attriute is a [Unix Timestamp](https://en.wikipedia.org/wiki/Unix_time) conversion of the time when the `.fetch()` method is executed in UTC (Universal Time Coordinated) time scale using one of the Perceval backends.


- References:

- [value of timestamp attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L160)


#### `updated_on` :

- The `updated_on` attribute is a Unix Timestamp conversion of last update datetime in UTC (Universal Time Coordinated) time scale of the GitHub Item set via retrieving the `update time` of the corresponding GitHub Repository. ( More like last modified time )


- References: 

1. [setting value of updated_on attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L163)
2. [extracting timestamp from update time of item](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L186)


#### `origin` :

- The `origin` attribute is identifier is the origin url from where the data is to be fetched and analyzed.

- for example
    - In case of `GitHub` Backend, the origin is set to the GITHUB_URL + owner + repository . i.e in my case : "https://github.com/inishchith/MeetInTheMiddle"


- References: 

- [setting the value of origin attribute](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L95)


#### `category` :

- The `category` attribute is the category of item to be fetched from the origin ( the data source )


- for example
    - In case of `Git` Backend, the category of item that is available to be fetched is [commit]()
    - In case of `GitHub` Backend, we can fetch information about [issues]() & [pull requests]()


- References:

- [issue pull-request & repository in case of github backend](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backends/core/github.py#L40)


#### `uuid` :

- `uuid` attribute is the SHA-1 Hash of the string. A string is our case is formed via concatination of the values from a list using ":" ( colon symbol ).

- for example
    - `uuid` in case of each item fetched via `Git` Backend is SHA-1 Hash of the "<origin>:<commit>"
    - In case of each item fetched via `GitHub` Backend, the SHA-1 Hash is of the string "<origin>:<id>" .

- References: 

1. [setting value of uuid](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L162)
2. [concatination of list and sha-1](https://github.com/chaoss/grimoirelab-perceval/blob/805d73122b871c29146a70601d8f3d78267b41e1/perceval/backend.py#L427)


<hr>

- Common git commands used by Perceval backend
    - clone
    - fetch
    - log
    - show
    - remote


<hr>
<div align="center">
    This concludes microtask #3 ;)
</div>
