import zipfile

def valid_zip(path):
    return zipfile.is_zipfile(path)

def file_depth(path):
    counter=0
    for letter in path:
        if letter=='/':
            counter+=1
    if path[-1]=='/':
        counter-=1
    return counter

def get_files_all(zip_file):
    paths=[]
    for fileinfo in zip_file.infolist():
        if not fileinfo.is_dir():
            paths.append(fileinfo.filename)
    return paths

def get_files_at_path(zip_file, directories_only, expected_depth, expected_initialpath):
    paths=[]
    for fileinfo in zip_file.infolist():
        path=fileinfo.filename
        depth=file_depth(path)
        if (depth==expected_depth and # correct depth
                path.startswith(expected_initialpath) and # correct path
                directories_only==fileinfo.is_dir()): # only get either directories or files
            paths.append(path)
    return paths
