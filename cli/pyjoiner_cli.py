import pyjoiner
import sys

selected_option = 0

_JOIN    =  1
_EXTRACT =  2
_EXIT    =  3

while( selected_option != _EXIT ):
    selected_option = int(input('\n\npyjoiner\n1 - Join Files\n2 - Extract Joined Files\n3 - Exit\nSelect an option: '))
    if (selected_option == _JOIN):
        input_dir       = input('Enter the input directory: ')
        output_filename = input('Enter the name of the output file: ')
        password        = input('Enter joined file password: ')
        pyjoiner.writeWithPassword(input_dir, output_filename, password)
    elif (selected_option == _EXTRACT):
        file_to_extract   = input('Enter file to extract full path (or filename only if on same folder): ')
        password          = input('Enter extraction password: ')
        extension         = input('Enter the desired extension for extracted files: ')
        pyjoiner.extractAndWrite(file_to_extract, password, extension)
    elif (selected_option == _EXIT):
        sys.exit(0)
    else:
        print ("Invalid option. Try again.")
        selected_option = 0