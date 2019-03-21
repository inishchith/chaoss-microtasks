# chaoss-microtasks

### Microtasks for GSOC Idea #3 : Support of Source Code Related Metrics [READ MORE](https://github.com/chaoss/grimoirelab/issues/182)

### # Microtask 1: 

- **Task:** Set up Perceval to be executed from PyCharm.
- Explanation can be found [here](./microtask-1)


<hr>

### # Microtask 2:

- **Task:** Create a Python script to execute Perceval via its Python interface using the Git and GitHub backends. Feel free to select any target repository.
- The scripts can be found [here](./microtask-2)
- I've chosen one of my personal projects i.e [MeetInTheMiddle](https://github.com/inishchith/MeetInTheMiddle) for this task.


<hr>

### # Microtask 3:

- **Task:** : Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:
  - What is the meaning of the JSON attribute 'timestamp'?
  - What is the meaning of the JSON attribute 'updated_on'?
  - What is the meaning of the JSON attribute 'origin'?
  - What is the meaning of the JSON attribute 'category'?
  - What is the meaning of the JSON attribute 'uuid'?
  - Which are the common methods of the Perceval backends?
  - List and explain at least 3 Git commands used by the Perceval backend.

- Answers to the above questions can be found [here](./microtask-3)

<hr>

### # Microtask 4:

- **Task:** : Create a Python script to fetch data from SoftwareHeritage using its API.
Given a target GitHub repository, the script should return a message if the repository is not available on SoftwareHeritage or the date of the last visit.
  - The script should rely on the endpoints: origin and visits.
  - Please use the Python library requests to issue requests to the SofwareHeritage API.

- The script can be found [here](./microtask-4)

<hr>

### # Microtask 5:

- **Task:** Set up Graal to be executed from PyCharm.
- Explanation can be found [here](./microtask-5)


<hr>

### # Microtask 6:

- **Task:** Create a Python script to execute Graal via its Python interface using the CoCom and CoLic backends. Feel free to select any target repository, for instance the GitHub repository hosting Toolkit.
- The scripts and installation steps can be found [here](./microtask-6)


<hr>

### # Microtask 7:

- **Task:** Based on the JSON documents produced by Graal and its source code, try to answer the following questions:
  - Which are the common methods of the Graal backends?
  - List and explain at least 2 Git commands used by Graal (and not implemented in Perceval).

- Answers to the above questions can be found [here](./microtask-7)

<hr>

### # Microtask 8:

- **Task:** Create a Python script to execute flake8 for a given commit of any Git repository. Given a commit SHA and a Git repository, the script should clone the repository (if it doesn't exist locally), perform a checkout based on the commit SHA and execute flake8 on that checkout. The script should return a message that either lists the errors found or "OK" if flake8 successfully ended.

- The script can be found [here](./microtask-8)


<hr>


### # Microtask 9:

- **Task:** Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc.

- I've produced 5 pull requests until this point.
- Information related to each pull request can be found [here](./microtask-9)

<hr>

#### In order to reproduce the results from this repository:

1. Clone the repository
```
    $ git clone https://github.com/inishchith/chaoss-microtasks.git
```

2. Install dependencies from the corresponding requirements of [microtask-*](#)

<hr>

**Note:**
- Each folder contains one microtask. 
- `readme.md` file under each directory contains information about the corresponding task.