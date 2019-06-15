# Automate Building of New Project
* The purpose of this app is to automate the building of new project.
* This currently support python project and Web projects using Javascript
* No installation of additional libraries are required.

## Tests
* Tested on Mac OSX Mojave
* Python 3.6 and above should work

## How to get it to work?
* Python needs to be installed.
* Use the help command for instructions.
> python run.py help
* All dictionaries have to updated accordingly in the run.py and projectCreate.py.
    * menuDict elements in the run.py have to be updated if not using default values.
    * Github username environment variable
        * This MUST be updated to create a Github repository.
    * Default path environment variable for each different type of project
        * This is required to use the default feature.

## Customizable expansion: projectCreate.py file
* Create different types of projects (can be unrelated to Python and Javascript).
    * Update all elements in all Dictionaries in run.py and projectCreate.py.
        * menuDict in run.py must be updated to accept different types of projects.
        * envDict in projectCreate.py must be updated for Github username and default path.
            * Keys must be similar to menuDict, excluding Github username.
            * Values are the String of environment variables.
                * Default path must be saved as an environment variable, and stored as the value of the key.
        * filesDict in projectCreate.py must be updated to create the desired files and or folders with files
            * Key must be similar to menuDict.
            * Values must be a list of Strings, which are the file and or folder with file names.
        * templateDict in projectCreate.py can be updated if adding data to a new file is required.
            * Key must be the file or folder with file name.
            * Value is the function name, which must be created and returned with the desired data to be stored.
        * gitignoreDict in projectCreate.py must be update to ignore the unwanted files.
            * Key must be similar to menuDict.
            * Value is the String of files to ignore.
