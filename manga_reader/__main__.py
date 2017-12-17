import sys
import zipfile

import manga_reader.mangazip as mangazip
import manga_reader.mangahelp as mangahelp
import manga_reader.gui as gui

def print_list(myList):
    for value in myList:
        print(value)

def open_pathlist(myzip, imagepaths):
    if len(imagepaths)==0:
        print(sys.argv[0] + ": No images at that location.")
        sys.exit()
    manga_gui = gui.Manga_Gui(myzip, imagepaths)

def main():
    if len(sys.argv)<=2: # no zip file to open
        mangahelp.print_help(sys.argv[0])
        sys.exit()
    if not zipfile.is_zipfile(sys.argv[2]):
        print(sys.argv[0] + ": Invalid zip file.")
        sys.exit()
    
    with zipfile.ZipFile(sys.argv[2]) as myzip:
        if len(sys.argv)==3: # No internal directory passed in
            internal_directory=""
            dir_depth=0
        else:
            internal_directory=sys.argv[3]
            dir_depth=mangazip.file_depth(internal_directory)+1 # +1 lets us look inside of the directory
        if sys.argv[1]=="list":
            dirs=mangazip.get_files_at_path(myzip, True, dir_depth, internal_directory)
            print_list(dirs)
            files=mangazip.get_files_at_path(myzip, False, dir_depth, internal_directory)
            print_list(files)
            sys.exit()
        elif sys.argv[1]=="open":
            imagepaths=mangazip.get_files_all(myzip)
            open_pathlist(myzip, imagepaths)
        elif sys.argv[1]=="open-dir":
            imagepaths=mangazip.get_files_at_path(myzip, False, dir_depth, internal_directory) # TODO: Add check for image files rather than just if files exist
            open_pathlist(myzip, imagepaths)

if __name__ == '__main__':
    main()
