import shutil, os, sys
from extensions import EXTENSIONS, STORAGE_DIRS
from win10toast import ToastNotifier

args = sys.argv[1:]

# Temp vars
file_list = []
files_moved = []
files_not_moved = []

# Directory to be reorganized
TARGET_DIR = 'C:\\Users\\ThinkPad\\Downloads\\'

# Command line arguments
force_move = False
if(args):
    for a in args:
        if a == '-f':
            force_move = True
        if a == '-d': # Accept directory from command line
            index = args.index(a)
            dir = args[index+1]

            if dir.endswith('\\'):
                try:
                    if os.path.exists(dir):
                        TARGET_DIR = dir
                except IndexError:
                    print("Invalid/No Directory Value Supplied")
            else:
                print('Directory must end with backslash (\\)')
                sys.exit()

EXTENSIONS_KEYS = tuple(EXTENSIONS.keys())

# create storage directories if they do not exist
for sd in STORAGE_DIRS:
    if not os.path.isdir(TARGET_DIR + sd):
        os.mkdir(str(TARGET_DIR) + str(sd))

# Collect list of files in the directory
dir_files = [os.path.join(TARGET_DIR, f) for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]

if dir_files:
    for file in dir_files:
        if file.endswith(EXTENSIONS_KEYS):
            # generator expression
            matches = next((suffix for suffix in EXTENSIONS_KEYS if file.endswith(suffix)), None)
            try:
                target_dir_file = TARGET_DIR + str(EXTENSIONS[matches]) + '\\' + os.path.basename(file)
                
                if os.path.isfile(target_dir_file) and force_move == True: # if the file exists in the target dir and the force flag is set
                    file_ext = os.path.splitext(file)[1]
                    newfilename = str(file + " - copy") + file_ext
                    os.renames(file, newfilename)
                    shutil.move(newfilename, TARGET_DIR + str(EXTENSIONS[matches]))
                else:
                    shutil.move(file, TARGET_DIR + str(EXTENSIONS[matches]))
                
                files_moved.append(str(file) + " -> " + TARGET_DIR + str(EXTENSIONS[matches]))
            except:
                files_not_moved.append(str(file) + " -> " + TARGET_DIR + str(EXTENSIONS[matches]))

# Stats
if files_moved:
    print('--------------------')
    print(str(len(files_moved)) + " file(s) relocated.")
    print('--------------------')
    for fm in files_moved:
        print("-- " + str(fm))

if files_not_moved:
    print('-------------------------------------------')
    print(str(len(files_not_moved)) + " file(s) could not be relocated.")
    print('You can use the -f flag to force move them.')
    print('-------------------------------------------')
    for fnm in files_not_moved:
        print("-- " + str(fnm))

# Toast alert in Windows
if files_moved or files_not_moved:    
    toaster = ToastNotifier()
    toaster.show_toast(str(len(files_moved)) + " file(s) moved.", str(len(files_not_moved)) + " file(s) could not be moved.")