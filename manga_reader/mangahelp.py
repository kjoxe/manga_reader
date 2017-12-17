name="Manga Reader"
version="0.1a"
def print_help(command):
    help_message="""__NAME__ __VERSION__

usage: __COMMAND__ zipfile

Quit       - q
Next image - j/space
Prev image - k
  (Prepend number to jump more than 1 image at once
  For example pressing "5j" will jump 5 images ahead)"""
    help_message=help_message.replace("__NAME__", name)
    help_message=help_message.replace("__VERSION__", version)
    help_message=help_message.replace("__COMMAND__", command.split("/")[-1])
    print(help_message)
