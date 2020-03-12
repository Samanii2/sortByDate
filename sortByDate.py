""" Sort by date program """
import shutil
import os
import datetime

def formatTime(date_stat):
    return datetime.datetime.fromtimestamp(date_stat).strftime('%Y-%m-%d')

def modifyDate(path_to_file):  
        stat = os.stat(path_to_file)
        return formatTime(stat.st_mtime)

def SortByDate():
    path = r"C:\utv\Projects\FileSorter\testdata"
    os.chdir(path)
    filesInPath = os.listdir(path)
    filesInPath.sort()

    print("Sorting list...")
    filesToSort = []
    for files in filesInPath:
        if files.endswith(".log"):
            filesToSort.append(files)

    print("Making folders...")
    for files in filesToSort:
        folderPath = modifyDate(path + '/' + files)
        if not os.path.isdir(folderPath):
            os.mkdir(folderPath)
            print(folderPath)

    print("Moving files...")
    for files in filesToSort:
        shutil.move(path + '/' + files, path + '/' + modifyDate(path + '/' + files))
        
    print("Sorting complete.")

SortByDate()
