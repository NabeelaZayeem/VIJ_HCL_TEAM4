from Level1.FindFileprj1 import FileFinder
from Level06.mysql_database import Mysql_DBaccess
filename=input("Enter the file name to search:")
filepath=input("Enter the drive")
expected=filename

dbobj=Mysql_DBaccess('localhost','root','Nabila@123','searchfiles')
res=dbobj.searchDB(filename)
if res==expected:
    print(dbobj.searchDB(filename))

else:
    obj=FileFinder()
    print(obj.find_files(filename,filepath))



   # print(obj.find_files(filename,drive))
#else:
    #dbobj.searchDB("C:\\\hcl\\\hcl.txt")