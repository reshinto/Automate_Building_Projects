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
* Please set the following environment variables and update the projectCreate.py file:
    * Look for "# UPDATE THIS to your environment variable" to update environment variable
        * Github username environment variable
            * This MUST be updated for the manual path input to work.
        * Default path environment variable for each different type of project
            * This is required to use the default feature.

## Customizable expansion
* Create different types of projects (can be unrelated to Python and Javascript).
    * Create a NewProject class and make it inherit from the Project class.
    * Update the environment variable in the NewProject class and assign it to the self.projectType variable.
    * Create the self.files list with files and folders with files to create.
* Add Template:
    * Update the templateDict and add the relevant template function.
    * This will add the desired data into the file by default.
* Add Gitignore varieties.
    * Update the gitignoreDict for more varieties.
