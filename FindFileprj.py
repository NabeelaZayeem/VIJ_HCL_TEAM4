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

if __name__ == '__main__':
    st=time.time()

    obj = FileFinder()
    print(obj.find_files('hcl.txt', 'C:/'))
    et=time.time()
    print(et-st)