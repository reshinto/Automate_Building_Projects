# Automate Building of New Project
* The purpose of this app is to automate the building of new projects.
* Currently support python projects and Web projects using Javascript.
* No installation of additional libraries are required.

## Tests
* Tested on Mac OSX Mojave.
* Python 3.6 and above should work.

## How to get it to work?
* Python needs to be installed.
* Use the help command for instructions and to view the list of supported Projects.
> python run.py help
* All dictionaries have to updated accordingly in the run.py and projectCreate.py.
    * menuDict elements in the run.py have to be updated if not using default values.
    * Github username environment variable.
        * This MUST be updated to create a Github repository.
    * Default path environment variable for each different type of project.
        * This is required to use the default feature.
* By default, folders, files, git init, git add, git commit, git repository, git remote, git push will automatically be created and initiated.
    * If creating of a git repository is not required, press "ctrl - c" when requested for password.
        * By doing this, load feature will not be supported as it is not required for me at the moment.

## Customizable expansion
* Create different types of projects (can be unrelated to Python and Javascript).
    * Update all elements in all Dictionaries in run.py and projectCreate.py.
        * menuDict in run.py must be updated to accept different types of projects.
        * envDict in projectCreate.py must be updated for Github username and default path.
            * Keys must be similar to menuDict, excluding Github username.
            * Values are the String of environment variables.
                * Default path must be saved as an environment variable, and stored as the value of the key.
        * filesDict in projectCreate.py must be updated to create the desired files and or folders with files.
            * Key must be similar to menuDict.
            * Values must be a list of Strings, which are the file and or folder with file names.
        * templateDict in projectCreate.py can be updated if adding data to a new file is required.
            * Key must be the file or folder with file name.
                * If tutorial html projects are created, all filenames will be named as project name by default.
            * Value is the function name, which must be created and returned with the desired data to be stored.
        * htmlDict in projectCreate.py must be updated to create the desirable template for the html file.
            * Keys must be similar to menuDict.
            * Value is the function name, which must be created and returned with the desired data to be stored.
        * gitignoreDict in projectCreate.py must be updated to ignore the unwanted files.
            * Key must be similar to menuDict.
            * Value is the String of files to ignore.
        * navDict in projectCreate.py must be updated to enable the load feature for opening and navigating to new Project folder in unsupported OS.
