import os
import time
print('Current directory is:',os.getcwd())

currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir, filename)

print('The constructed path is: ', fullpath)

relativePath = 'output.txt'
print('\nThe absolute path is: ',os.path.abspath(relativePath))

filepath = r'C:\Users\micha\Desktop\!Nauka\Python\Udemy\pierwszyProjekt\OperacjeIO\results.txt'
print('\nThe file name part is: ',os.path.basename(filepath))
print('The directory part is: ', os.path.dirname(filepath))

print('\nIs file existing? ', os.path.exists(filepath))

if os.path.exists(filepath):
    print('\nLast modify date is: ', os.path.getmtime(filepath)) #epoch time
    print('Last modify date is: ', time.localtime(os.path.getmtime(filepath)))

    print('\nFile size is: ', os.path.getsize(filepath)) #w bajtach

    print('\nIs it a file?', os.path.isfile(filepath))
    print('Is it a dir?', os.path.isdir(filepath))

    print('\nPath splitted: ', os.path.split(filepath)) #odrywa ostatni fragment ścieżki
    print('Only file name part: ', os.path.split(filepath)[1])

    print('\nPath splitted into drive: ', os.path.splitdrive(filepath))
    print('Only drive: ', os.path.splitdrive(filepath)[0])





