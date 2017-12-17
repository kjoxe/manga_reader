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
    if len(sys.argv)<2: # no zip file to open
        mangahelp.print_help(sys.argv[0])
        sys.exit()
    if not zipfile.is_zipfile(sys.argv[-1]):
        print(sys.argv[0] + ": Invalid zip file.")
        sys.exit()
    
    with zipfile.ZipFile(sys.argv[-1]) as myzip:
        imagepaths=mangazip.get_files_all(myzip)
        open_pathlist(myzip, imagepaths)

if __name__ == '__main__':
    main()
