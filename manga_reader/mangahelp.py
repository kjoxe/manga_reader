name="Manga Reader"
version="0.1a"
def print_help(command):
    help_message="""
__NAME__ __VERSION__

  usage: __COMMAND__ open path_to_zip
     or: __COMMAND__ open-dir/list path_to_zip [internal_folder]

options:

  open     - Open all files in GUI and scroll through in alphabetical order
  open-dir - Only open the files contained in the specified directory.
             If no directory specified then only the root directory will be opened
  list     - List files contained in the specified directory.
             If no directory specified then only the root directory will be printed"""
    help_message=help_message.replace("__NAME__", name)
    help_message=help_message.replace("__VERSION__", version)
    help_message=help_message.replace("__COMMAND__", command)
    print(help_message)
