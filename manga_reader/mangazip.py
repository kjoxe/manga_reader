import zipfile

def valid_zip(path):
    return zipfile.is_zipfile(path)

def get_files_all(zip_file):
    paths=[]
    for fileinfo in zip_file.infolist():
        if not fileinfo.is_dir():
            paths.append(fileinfo.filename)
    return paths
