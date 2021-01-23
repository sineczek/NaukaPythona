#filename = input("Enter filename: ")
#print("The file name is: %s" % (filename))

#wszystko co input przeczyta to zawsze string %s!
'''filesizeStr = input("Enter the ma file size (MB): ")
filesizeInt = int(filesizeStr)
print("The max size of file is %d" % (filesizeInt))
print("The max size of file is %d kb" % (filesizeInt*1024))'''

while True:
    filesizeStr = input("Enter the ma file size (MB): ")
    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break
print("The max size of file is %d" % (filesizeInt))
print("The max size of file is %d kb" % (filesizeInt*1024))
