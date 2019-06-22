import os.path
import re


class FileSystem:

    defaultFilePath = None
    file_path = None

    def setPath(self):
        """
        Set full path. When keying path,
        including new folder is not a requisite.
        """
        self.file_path = input(
            "Please provide full path, "
            "excluding the new project folder name to create.\n"
            "e.g.: /pathToSave\n> ")

    def getContents(self, _file_path):
        """
        Check if file exists and if file is empty.
        If both are True, return the contents of the file as a list
        """
        if self.haveFile(_file_path) and not self.isEmpty(_file_path):
            # open and read file
            with open(_file_path, 'r') as rf:
                file_contents = rf.read().split("\n")
            file_contents.pop()
            # Exclude last empty line in text file before return string
            return file_contents
        return None

    def createFile(self, _file_path=None, display_msg=False):
        """
        Check if file exist. If it does not, create new file.
        Display message feature added to provide visualization.
        """
        if _file_path is None:
            if self.defaultFilePath is None:
                self.setPath()
            else:
                self.file_path = self.defaultFilePath
        else:
            self.file_path = _file_path
        # Ensures file does not exist to prevent erasing by mistake
        if not os.path.isfile(self.file_path):
            try:
                # Although filename is included, only new directory be created
                os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
                # Creates a new file
                with open(self.file_path, 'w'):
                    pass
                if display_msg is not False:
                    print(f"A new file has been created at:\n{self.file_path}")
            except FileExistsError as msg:
                print(msg)

    @classmethod
    def useDefaultPath(cls, file_type):
        """
        This will override the predetermined defaultFilePath value.
        Choose file type to set default path and filename.
        Available file types: 1) authen 2) spam
        Add more if needed or just use the createFile method directly.
        """
        cls.defaultFilePath = cls.backOneFolder(cls.getScriptPath())
        settings = {
            "authen": "/settings/authentication.txt",
            "spam": "/settings/spam_list.txt"
        }
        if settings.get(file_type) is None:
            raise ValueError(f"File type: '{file_type}' not available! "
                             "Please use other file types or create one.")
        else:
            cls.defaultFilePath += settings[file_type]

    @staticmethod
    def haveFile(_file_path):
        """Return True if file exists."""
        return os.path.isfile(_file_path)

    @staticmethod
    def isEmpty(_file_path):
        """Return True if file is empty."""
        return os.stat(_file_path).st_size == 0

    @staticmethod
    def getHomePath():
        """
        Get default home path.
        / is not included at the end of the last folder name in path.
        """
        return os.path.expanduser('~')

    @staticmethod
    def getScriptPath():
        """
        Find and return script path that is currently running.
        / is not included at the end of the last folder name in path.
        When concatenating with other strings, remeber to put a /!
        """
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def getCurrentPath():
        """
        Get full path of current working directory
        / is not included at the end of the last folder name in path.
        """
        return os.getcwd()

    @staticmethod
    def backOneFolder(old_path):
        """
        Go back by one folder, then return full path
        last / character is excluded to make paths of all folders & files
        consistent.
        """
        # Using raw string, so \ not required
        result_list = re.findall(r".+?/", old_path)
        # Exclude last / character to standardize directories & files in path
        return "".join(result_list)[:-1]

    @staticmethod
    def editFile(_file_path, text):
        if FileSystem.haveFile(_file_path):
            with open(_file_path, "a") as af:
                af.write(text + "\n")
