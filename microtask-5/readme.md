## Microtask #5

In this microtask, we'll try to set up Graal to be executed from PyCharm IDE.

<hr>

#### # Steps

- Firstly download and install [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- Clone [Graal](https://github.com/chaoss/grimoirelab-graal) repository for development purpose.
- Open the Graal project in PyCharm IDE

#### # Run/Debug Configuration

1. Select `Script path` as `bin/graal` from the project repository.
2. Add Graal parameters in `Parameters` input tab.
3. Apply the changes & Run the script

<div align="center">
    <b> Below: I'm setting up Graal's `CoCom` backend for execution.</b>
    <br><br>
    <img src="./images/graal_setup.gif">
</div>

<br>

<div align="center">
    <b>  Below: I'm setting up grimoirelab-perceval & grimoirelab-toolkit, with this we can have a look at the dependent source and debug faster. </b>
    <br><br>
    <img src="./images/add_toolkit_to_path_graal.gif">
</div>

<br>

- Refer PyCharm [basics](https://www.jetbrains.com/help/pycharm/essentials.html)
- Refer to other commands by passing `--help` in configuration parameter

<hr>
<div align="center">
    <b> This concludes microtask #5 </b>
</div>
