## Microtask #1

In this microtask, we'll try to set up Perceval to be executed from PyCharm IDE.

<hr>

#### # Steps

- Firstly download and install [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- Clone [Perceval](https://github.com/chaoss/grimoirelab-perceval) repository for development purpose.
- Open the Perceval project in PyCharm IDE

#### # Run/Debug Configuration

1. Select `Script path` as `bin/perceval` from the project repository.
2. Add Perceval parameters in `Parameters` input tab.
3. Apply the changes & Run the script

<div align="center">
    <b> Below: I'm setting up Perceval's `Git` backend for execution. </b>
    <br><br>
    <img src="./images/perceval_setup.gif">
</div>

<br>

<div align="center">
    <b> Below: I'm setting up grimoirelab-toolkit, with this we can have a look at the dependent source and debug faster.</b>
    <br><br>
    <img src="./images/add_toolkit_to_path_perceval.gif">
</div>

<br>

- Refer PyCharm [basics](https://www.jetbrains.com/help/pycharm/essentials.html)
- Refer to other commands by passing `--help` in configuration parameter

<hr>
<div align="center">
    <b> This concludes microtask #1 </b>
</div>
