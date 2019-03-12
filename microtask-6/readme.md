## Microtask #6

- In this microtask, we'll create a Python script to execute Graal via its Python interface using the CoCom and CoLic backends.

- CoCom Backend [ [Jupyter Notebook](./cocom_backend/graal_cocom_backend.ipynb) | [Script](./cocom_backend/graal_cocom_backend.py) ] 
- CoLic Backend [ [Jupyter Notebook](./colic_backend/graal_colic_backend.ipynb) | [Script](./colic_backend/graal_colic_backend.py) ] 

<hr>

#### CoCom Backend

- CoCom ( Code Complexity ) Backend based on supported languages with the help of [Lizard](https://github.com/terryyin/lizard), provides us with various source code analysis such as:
  - Cyclomatic Complexity and Average Cyclomatic Complexity
  - Lines of Code and Average Lines of Code
  - Number of functions
    ... and many more

#### CoLic Backend

- CoLic ( Code License ) Backend gathers license information from git repositories with the help of
  - [NOMOS](https://github.com/fossology/fossology/tree/master/src/nomos)
  - [SCANCODE](https://github.com/nexB/scancode-toolkit)
- They can be activated by passing the corresponding category: `code_license_nomos` or `code_license_scancode`

<br>

**NOTE** : We need to pass executable path of NOMOS & SCANCODE as a parameter in order to work with CoLic backend.

<hr>

**Steps for setting up CoLic backend for NOMOS & SCANCODE executables**

**NOMOS**

```sh
    # clone the repository
    git clone https://github.com/fossology/fossology

    # setup NOMOS
    cd fossology/src/nomos/agent/
    make -f Makefile.sa
```

**SCANCODE**

```sh
    # download the scancode distribution v3.0.0
    wget https://github.com/nexB/scancode-toolkit/releases/download/v3.0.0/scancode-toolkit-3.0.0.zip

    # unzip the distribution and change directory
    unzip -q scancode-toolkit-3.0.0.zip
    cd scancode-toolkit-3.0.0

    # setup scancode for the first execution
    ./scancode --help
```

**Note:** In order to reproduce the results please change the executable path in the source files.
