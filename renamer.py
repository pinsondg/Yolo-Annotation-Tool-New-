from os import listdir, rename, remove
from os.path import isfile, join, splitext

path = '/Users/dpinson/Documents/personal_coding_projects/Yolo-Annotation-Tool-New-/final'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
num = 1
renamed = 0
print('There are ' + str(len(onlyfiles)) + 'in directory.')
for file in onlyfiles:
    ext = splitext(file)
    if ext[1] == '.jpg' or ext[1] == '.png' or ext[1] == '.jpeg':
        newNameImg = path + '/' + 'image_' + str(num) + ext[1]
        newNameLabel = path + '/' + 'image_' + str(num) + '.txt'
        print('Renaming [' + path + '/' + file + '] to [' + newNameImg + ']')
        rename(path + '/' + file, newNameImg)
        try:
            print('Renaming [' + path + '/' + ext[0] + '.txt]' + 'to [' + newNameLabel + ']')
            rename(path + '/' + ext[0] + '.txt', newNameLabel)
            renamed = renamed + 1
        except FileNotFoundError:
            print('ERROR - .txt file not found. Removing: ' + newNameImg)
            remove(newNameImg)
        num = num + 1
print('Successfully renamed ' + str(renamed * 2) + ' files out of ' + str(len(onlyfiles)))
