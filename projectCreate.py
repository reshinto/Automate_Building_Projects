import os
import sys
import subprocess
from libraries import filelib as fl


class Project:
    """Create new project template."""
    def __init__(self, projectType, files, projectName=None, default=True):
        self.projectName = projectName
        if default is True:
            if self.projectName is None:
                self.projectName = input("Project name: ")
            projectPath = os.environ.get(projectType)
            self.path = f"{projectPath}/{self.projectName}"
        else:
            getPath = fl.FileSystem()
            getPath.setPath()
            self.path = f"{getPath.filePath}/{self.projectName}"
        createFile(files, self.path)


class PythonProject(Project):
    """
    Create Python project.
    - To enable default path, ensure the path is saved in the environment
    variable as the self.projectType value.
    - Add all files and folders to be created in the self.files array
    """
    def __init__(self, projectName=None, default=True):
        # UPDATE THIS to your environment variable
        self.projectType = "pyProject"
        self.files = ["readme.md", "main.py", ".gitignore"]
        super().__init__(self.projectType, self.files, projectName, default)


class WebJSProject(Project):
    """
    Create Web project that uses Javascript.
    - To enable default path, ensure the path is saved in the environment
    variable as the self.projectType value.
    - Add all files and folders to be created in the self.files array
    """
    def __init__(self, projectName=None, default=True):
        # UPDATE THIS to your environment variable
        self.projectType = "webProject"
        self.files = ["readme.md", "index.html", "public/stylesheets/main.css",
                      "public/javascripts/app.js", ".gitignore"]
        super().__init__(self.projectType, self.files, projectName, default)


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
    def __init__(self, projectType, projectName=None, default=True):
        if projectDict.get(projectType) is None:
            print(f"{projectType} is not supported")
        else:
            self.project = projectDict[projectType](projectName, default)
        self.path = self.project.path
        os.chdir(self.path)  # required to run commands at correct path
        for command in self.getCommands():
            self.runCommand(command)

    def runCommand(self, command):
        """Run commands in the terminal."""
        return subprocess.check_output(command, shell=True).decode().strip()

    def getCommands(self):
        """List of commands to be runned in the terminal."""
        # UPDATE THIS to your environment variable
        return [
            "git init && git add . && git commit -m 'first commit'",
            f"curl -u '{os.environ.get('githubUser')}' "
            "https://api.github.com/user/repos -d '"
            "{\"name\":\"" + f"{self.project.projectName}" + "\"}'",
            "git remote add origin https://github.com/"
            f"{os.environ.get('githubUser')}/"
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


def htmlTemplate():
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


def gitignoreTemplate():
    return gitignoreDict[sys.argv[1]]


# Dictionary of all buildable projects available for automation
projectDict = {
    "python": PythonProject,
    "webjs": WebJSProject
}

# Dictionary of all templates, add if more template functions are required
templateDict = {
    "index.html": htmlTemplate,
    ".gitignore": gitignoreTemplate
}

# Dictionary of files to ignore, add if other files are required to ignore
gitignoreDict = {
    "python": "__pycahce__\n*.pyc",
    "webjs": "._*"
}
