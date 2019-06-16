import sys
from projectCreate import GitInitiate as Git


# add elements in dictionary to expand
menuDict = {
    "python": "python",
    "webjs": "webjs"
}


def invalid(msg=None):
    if msg is None:
        msg = "Invalid command!"
    print(f"{msg}\nUse the help argument to display the help menu")


# modify help menu if expanding
def helpMenu():
    print("""\
Help Menu:
1) Create new Python project at default path.
python run.py python nameOfNewProjectFolder

2) Create new Web project with Javascript at default path.
python run.py webjs nameOfNewProjectFolder

3) Create new Python project at designated path.
python run.py python nameOfNewProjectFolder manual
* then follow the instruction.

4) Create new Web project with Javascript at designated path.
python run.py webjs nameOfNewProjectFolder manual
* then follow the instruction.
""")


if __name__ == "__main__":
    try:
        projectType = sys.argv[1]
        if projectType == "help":
            helpMenu()
        elif menuDict.get(projectType) is None:
            msg = f"'{projectType}' is an invalid command."
            invalid(msg)
        else:
            projectName = sys.argv[2]
            if len(sys.argv) == 3:
                print(sys.argv)
                Git(projectName)
                print("New project created!")
            elif sys.argv[3] == "manual":
                Git(projectName, False)
                print("New project created!")
            else:
                invalid()
    except IndexError as msg:
        invalid(msg)
