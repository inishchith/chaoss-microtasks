import os
import subprocess

current_directory = os.getcwd()
REPO_URL = "https://github.com/chaoss/grimoirelab-perceval"
REPOSITORY_NAME = os.path.join(current_directory, REPO_URL.split("/")[-1])

# checkout to commit
sha = "076953e95735401b4d9266562f9ae406a30751a0"

if not os.path.isdir(REPOSITORY_NAME):
    msg = subprocess.check_output(['git', 'clone', REPO_URL]).decode("utf-8")
else:
    print("REPOSITORY ALREADY CLONED !")

os.chdir(REPOSITORY_NAME)

try:
    msg = subprocess.check_output(["git", "checkout", sha]).decode("utf-8")
except subprocess.CalledProcessError as e:
    error = e.output.decode("utf-8")
    print(error)


try:
    msg = subprocess.check_output(["flake8", "."]).decode("utf-8")
except subprocess.CalledProcessError as e:
    msg = e.output.decode("utf-8")

if len(msg) > 0:
    print(msg)
else:
    print("> OK")

msg = subprocess.check_output(["git", "checkout", "master"]).decode("utf-8")