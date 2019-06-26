import sys
from projectcreate import GitInitiate as Git


# add elements in dictionary to expand
menuDict = {
    "python": "python",
    "staticWebJs": "staticWebJs",
    "d3Tutorial": "d3Tutorial",
    "react": "react",
	"reactTut": "reactTut"
}


def invalid(message=None):
    if message is None:
        message = "Invalid command!"
    print(f"{message}\nUse the help argument to display the help menu")


# modify help menu if expanding
def helpMenu():
    print("""\
Help Menu:
1) Create new Project
    - Create new Python project at default path.
      > python run.py python {nameOfNewProjectFolder}

    - Create new Web project with Javascript at default path.
      > python run.py webjs {nameOfNewProjectFolder}

2) Create new Project and open Project in new terminal.
    - load variable MUST be used.
      > python run.py {projectType} {nameOfNewProjectFolder} load

3) Disable load function.
    > python run.py {projectType} {nameOfNewProjectFolder} {xxx}

4) Create new Project at designated path with load feature.
    > python run.py {projectType} {nameOfNewProjectFolder} load manual
    * then follow the instruction.

5) Create new Project at designated path without load feature.
    > python run.py {projectType} {nameOfNewProjectFolder} {xxx} manual
    * then follow the instruction.

List of Project types currently supported:
1) python: Creates a simple python project.
2) staticWebJs: Creates a simple static web project with Javascript.
3) d3Tutorial: Creates a D3 tutorial project.
4) react: Creates a react project.
5) reactTut: Creates a react tutorial project.
   (does not contain the full react package.)
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
                Git(projectName, False, True)
                print("New project created!")
            else:
                load = sys.argv[3] == "load"
                if len(sys.argv) == 4:
                    Git(projectName, load, True)
                    print("New project created!")
                if sys.argv[4] == "manual":
                    Git(projectName, load, False)
                    print("New project created!")
                else:
                    invalid(f"{sys.argv[4]} is not supported")
    except IndexError as msg:
        invalid(msg)
