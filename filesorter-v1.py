import os, time, shutil, sys

# Clearing Console
def consoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Confirming User Directory
def confirmation():
    global userFolder
    consoleClear()
    print("Selected Directory: ", userFolder)
    x = input('Confirm? (Y/n) ')
    if x == 'Y':
        fileVerification()
    elif x == 'n': 
        print('Operation Cancelled.')
        userFolder = input('Please enter the path of the folder you want to organize: ').replace('\\', '')
        confirmation()
    else:
        print('Invalid input ❌! Please try again.')
        confirmation()

# Dot Animation
def dotAnimation(func, maxDots=3):
    startTime = time.time()
    func()
    duration = time.time() - startTime
    dot_count = 0
    while duration < 3:
        for i in range(maxDots):
            time.sleep(.5)
            sys.stdout.write('.')
            sys.stdout.flush()
            dot_count += 1
            if dot_count == maxDots:
                for j in range(maxDots):
                    sys.stdout.write('\b \b')
                dot_count = 0
        duration = time.time() - startTime
    print(' ')

# Verifying User Directory Exists
def fileVerification():
    global userFolder
    consoleClear()
    print("Verifying path exists", end="")
    dotAnimation(lambda: os.path.exists(userFolder))
    if os.path.exists(userFolder) and os.path.isdir(userFolder):
        print('\nPath exists ✅!')
        input("Press Enter to Continue: ")
        organizeFile()
    else:
        print('Path does not exist ❌! Please select a valid path.')
        input('Press enter to continue...')
        consoleClear()
        userFolder = input('Please enter the path of the folder you want to organize: ')
        confirmation()

# Organizing User Directory
def organizeFile():
    consoleClear()
    folderFiles = os.listdir(userFolder)
    
    print("Files and directories in directory: ") 
    print(folderFiles) 
    print("")
    print("Done!")
    
    fileTypes = {
    'Images': ['.png', '.jpg', '.jpeg', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Documents': ['.pdf', '.docx', '.xlsx', '.txt'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Misc': []
    }
    
    for file in folderFiles:
        fileName, fileExtension = os.path.splitext(file)
        fullFilePath = os.path.join(userFolder, file) 
        fileExtension = fileExtension.lower()


        for fileType, extensions in fileTypes.items():
            if fileExtension in extensions:
                if not os.path.exists(userFolder + "/" + fileType):
                    os.mkdir(userFolder + "/" + fileType) 
                shutil.move(fullFilePath, userFolder + "/" + fileType + "/" + file)

print('Welcome to the Basic File Organizer 🗄️ ! \nThis is a casual project for me to train my Python IT Automation Skills :)\n')
print('Note: Subfolders in the directory will not be categorized/organized.')
userFolder = input('Please enter the path of the folder you want to organize: ').replace('\\', '')
confirmation()
