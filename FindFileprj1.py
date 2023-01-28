import os
import time
class FileFinder:
    def __init__(self):
        pass

    def find_files(self, filename, filepath):
        files=[]
        self.filename = filename
        self.filepath = filepath
        for root, dir, file in os.walk(filepath):
            if filename in file:
                files.append(os.path.join(root, filename))

        return files
