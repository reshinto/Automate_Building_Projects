import os
import sys
import subprocess
import platform
from libraries import filelib as fl


class Project:
    """Create new project template."""
    def __init__(self, projectName, default):
        self.projectName = projectName
        if default is True:
            if self.projectName is None:
                self.projectName = input("Project name: ")
            projectPath = os.environ.get(envDict[sys.argv[1]])
            self.path = f"{projectPath}/{self.projectName}"
        else:
            getPath = fl.FileSystem()
            getPath.setPath()
            self.path = f"{getPath.filePath}/{self.projectName}"
        createFile(filesDict[sys.argv[1]], self.path)


class GitInitiate:
    """
    Save project in Github:
    - Initiate Git
    - Add all files
    - Make commit
    - Create new respository in Github
    - Link project to respository
    - Push project to respository
    """
    def __init__(self, projectName=None, load=False, default=True):
        self.project = Project(projectName, default)
        self.path = self.project.path
        os.chdir(self.path)  # required to run commands at correct path
        try:
            for command in self.getCommands():
                self.runCommand(command)
        except KeyboardInterrupt:
            print("\nCreating of new Github repository has been cancelled.")
        # open new project in another terminal
        if load is True:
            if navDict.get(platform.system()) is None:
                return "OS not supported, unable to auto load."
            command = navDict[platform.system()] + f" {self.path}"
            self.runCommand(command)

    def runCommand(self, command):
        """Run commands in the terminal."""
        return subprocess.check_output(command, shell=True).decode().strip()

    def getCommands(self):
        """List of commands to be runned in the terminal."""
        return [
            "git init && git add . && git commit -m 'first commit'",
            f"curl -u '{os.environ.get(envDict['user'])}' "
            "https://api.github.com/user/repos -d '"
            "{\"name\":\"" + f"{self.project.projectName}" + "\"}'",
            "git remote add origin https://github.com/"
            f"{os.environ.get(envDict['user'])}/"
            f"{self.project.projectName}.git",
            "git push -u origin master"
        ]


def createFile(files, path):
    """Create folders with files and insert data if required."""
    for file in files:
        filename = f"{path}/{file}"
        fl.FileSystem().createFile(filename, True)
        if templateDict.get(file):
            fl.FileSystem().editFile(filename, templateDict[file]())


# Add template functions or dictionaries to expand
def htmlTemplate():
    return htmlDict[sys.argv[1]]()


def staticTemplate():
    return """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <link rel="stylesheet" href="public/stylesheets/main.css">
</head>
<body>

</body>
<script type="text/javascript" src="public/javascripts/app.js"></script>
</html>
"""


def d3TutorialTemplate():
    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="https://d3js.org/d3.v5.min.js"></script>
    <link rel="stylesheet" href="{sys.argv[2]}.css">
</head>
<body>
</body>
<script type="text/javascript" src="{sys.argv[2]}.js"></script>
</html>
"""


def gitignoreTemplate():
    return gitignoreDict[sys.argv[1]]


if len(sys.argv) >= 3:
    ###################
    # 1) Update if have default path for new project,
    # and to edit saved github username environemnt variable
    # Dictionary of environment variables for Github user and default paths
    envDict = {
        "user": "githubUser",
        "python": "pyProject",
        "staticWebJs": "webProject"
    }

    ###################
    # 2) Update to create files or folder with files for new project
    # Dictionary of files or folder with files to be created
    filesDict = {
        "python": ["readme.md", "main.py", ".gitignore"],
        "staticWebJs": ["readme.md", "index.html",
                        "public/stylesheets/main.css",
                        "public/javascripts/app.js", ".gitignore"],
        "d3Tutorial": [f"{sys.argv[2]}.html", f"{sys.argv[2]}.css",
                       f"{sys.argv[2]}.js"]
    }

    ###################
    # 3) Update if required to add data for specific files
    # If updated, 4) and/or 5) might also need to be updated
    # Dictionary of all templates, add if more template functions are required
    templateDict = {
        "index.html": htmlTemplate,
        f"{sys.argv[2]}.html": htmlTemplate,
        ".gitignore": gitignoreTemplate
    }

    ###################
    # 4) Update if required to edit files for specific project types
    htmlDict = {
        "staticWebJs": staticTemplate,
        "d3Tutorial": d3TutorialTemplate
    }
    
    ###################
    # 5) Update for .gitignore support
    # Dictionary of files to ignore, add if other files are required to ignore
    gitignoreDict = {
        "python": "__pycahce__\n*.pyc",
        "staticWebJs": "._*"
    }

    ###################
    # 6) Update for OS support
    # Dictionary of opening terminal commands for each OS
    # This command will combine with new project folder path
    # to open new project folder in a new terminal window or tab
    navDict = {
        "Darwin": "open -a iTerm",
        "Windows": "",
        "Linux": ""
    }
