import os
import sys
import subprocess
import platform
from libraries import filelib as fl


class Project:  # pylint: disable=too-few-public-methods
    """Create new project template."""
    def __init__(self, project_name, default):
        self.project_name = project_name
        if default is True:
            if self.project_name is None:
                self.project_name = input("Project name: ")
            project_path = os.environ.get(envDict[sys.argv[1]])
            self.path = f"{project_path}"
        else:
            get_path = fl.FileSystem()
            get_path.setPath()
            self.path = f"{get_path.file_path}"
        # skip file creation if filesDict returns a string
        if not isinstance(filesDict[sys.argv[1]], str):
            createFile(filesDict[sys.argv[1]],
                       f"{self.path}/{self.project_name}")


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
    def __init__(self, project_name=None, load=False, default=True):
		# TODO: fix ugly code
        self.project = Project(project_name, default)
        if isinstance(filesDict[sys.argv[1]], str):
            self.path = self.project.path
            os.chdir(self.path)  # required to run commands at correct path
            runCommand(filesDict[sys.argv[1]])
        self.path = f"{self.project.path}/{self.project.project_name}"
        os.chdir(self.path)  # required to run commands at correct path
        if sys.argv[1] == "reactTut":
            for command in getReactDependencies():
                runCommand(command)
        if not isinstance(filesDict[sys.argv[1]], str):
            runCommand(self.getGitCommand())
        try:
            for command in self.getGithubCommands():
                runCommand(command)
        except KeyboardInterrupt:
            print("\nCreating of new Github repository has been cancelled.")
        # open new project in another terminal
        self.setLoad(load)

    @staticmethod
    def getGitCommand():
        """List of commands to be runned in the terminal."""
        return "git init && git add . && git commit -m 'first commit'"

    def getGithubCommands(self):
        """List of Github commands to be runned in the terminal."""
        return [
            f"curl -u '{os.environ.get(envDict['user'])}' "
            "https://api.github.com/user/repos -d '"
            "{\"name\":\"" + f"{self.project.project_name}" + "\"}'",
            "git remote add origin https://github.com/"
            f"{os.environ.get(envDict['user'])}/"
            f"{self.project.project_name}.git",
            "git push -u origin master"
        ]

    def setLoad(self, load):
        if load:
            if navDict.get(platform.system()) is None:
                print("OS not supported, unable to auto load.")
            # command = navDict[platform.system()] + f" {self.path}"
            command = navDict[platform.system()] + f" ."
            print(self.path)
            runCommand(command)


def runCommand(command):
    """Run commands in the terminal."""
    return subprocess.check_output(command, shell=True).decode().strip()


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
  <script type="text/javascript" src="public/javascripts/app.js"></script>
</body>
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
  <script type="text/javascript" src="{sys.argv[2]}.js"></script>
</body>
</html>
"""


def gitignoreTemplate():
    return gitignoreDict[sys.argv[1]]

def getReactDependencies():
    return ["npm i react react-dom prop-types",
            "npm i --save-dev @babel/core @babel/preset-env",
            "npm i --save-dev @babel/preset-react webpack webpack-cli",
            "npm install --save-dev @babel/plugin-proposal-class-properties",
            "npm i --save-dev webpack-dev-server babel-loader css-loader",
            "npm i --save-dev style-loader html-webpack-plugin"]


def reactNpmInitTemplate():
    return f"""\
{{
  "name": "{sys.argv[2]}",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "babel": {{
    "presets": [
      "@babel/preset-env",
      "@babel/preset-react"
    ],
    "plugins": [
      [
        "@babel/plugin-proposal-class-properties"
      ]
    ]
  }},
  "scripts": {{
    "start": "webpack-dev-server --open"
  }},
  "keywords": [],
  "author": "",
  "license": "ISC"
}}
"""


def webpackTemplate():
    return r"""const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "index_bundle.js",
  },
  module: {
    rules: [
      {test: /\.(js)$/, use: "babel-loader"},
      {test: /\.css$/, use: ["style-loader", "css-loader"]},
    ],
  },
  mode: "development",
  plugins: [
    new HtmlWebpackPlugin({
      template: "src/index.html",
    }),
  ],
};
"""


def reactJsTemplate():
    return """\
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

class App extends React.Component {
  render() {
    return (
      <div>
        Hello World!
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"))
"""


def reactHtmlTemplate():
    return """\
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""


if len(sys.argv) >= 3:
    ###################
    # 1) Update if have default path for new project,
    # and to edit saved github username environemnt variable
    # Dictionary of environment variables for Github user and default paths
    envDict = {
        "user": "githubUser",
        "python": "pyProject",
        "staticWebJs": "webProject",
        "react": "webProject"
    }

    ###################
    # 2) Update to create files or folder with files for new project
    # Dictionary of files or folder with files to be created
    filesDict = {
        "python": ["readme.md", "main.py", ".gitignore"],
        "staticWebJs": ["readme.md", "index.html",
                        "public/stylesheets/main.css",
                        "public/javascripts/app.js", ".gitignore"],
        "d3Tutorial": ["index.html", f"{sys.argv[2]}.css",
                       f"{sys.argv[2]}.js"],
        "react": f"npx create-react-app {sys.argv[2]}",
        "reactTut": [".gitignore", "package.json", "webpack.config.js",
                     "src/index.js", "src/index.css", "src/index.html"]
    }

    ###################
    # 3) Update if required to add data for specific files
    # If updated, 4) and/or 5) might also need to be updated
    # Dictionary of all templates, add if more template functions are required
    templateDict = {
        "index.html": htmlTemplate,
        ".gitignore": gitignoreTemplate,
        "package.json": reactNpmInitTemplate,
        "webpack.config.js": webpackTemplate,
        "src/index.js": reactJsTemplate,
        "src/index.html": htmlTemplate
    }

    ###################
    # 4) Update if required to edit files for specific project types
    htmlDict = {
        "staticWebJs": staticTemplate,
        "d3Tutorial": d3TutorialTemplate,
        "reactTut": reactHtmlTemplate
    }

    ###################
    # 5) Update for .gitignore support
    # Dictionary of files to ignore, add if other files are required to ignore
    gitignoreDict = {
        "python": "__pycahce__\n*.pyc",
        "staticWebJs": "._*",
        "reactTut": "node_modules\n.DS_Store\ndist"
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
