import os
import glob
import base64
from pathlib import Path

splitToken = "joinedFilesEnd"

def getFileBytes(file_path):
    with open(file_path, "rb") as f:
        bytes = f.read(os.path.getsize(file_path))
        return bytes


def joinAllDirFiles(dir):
    global splitToken
    output = b""
    for file_path in glob.glob(dir):
        if(".py" not in file_path and ".data" not in file_path):
            output += getFileBytes(file_path)
            output += bytes(splitToken, 'utf-8')
    return output


def writeWithPassword(input_dir, output_filename, password):
    global splitToken
    bytes_to_write = joinAllDirFiles(input_dir + "*.*")
    password = base64.b64encode(bytes(password, 'utf-8'))
    bytes_to_write = password + bytes(splitToken, 'utf-8') + bytes_to_write
    outfile = open(output_filename + ".data", 'wb')
    outfile.write(bytes_to_write)
    outfile.close
    return True


def extractAndWrite(filename_to_extract , password, files_extension):
    global splitToken
    to_extract = open(filename_to_extract, 'rb').read(os.path.getsize(filename_to_extract))
    split_token = bytes(splitToken, 'utf-8')
    password = base64.b64encode(bytes(password, 'utf-8'))
    to_extract = to_extract.split(split_token)
    if (password == to_extract[0]):
        Path("./extraction").mkdir(parents=True, exist_ok=True)
        for x in range(1, len(to_extract) - 1):
            temp_file = open('./extraction/' + str(x) + '.' + str(files_extension), 'wb')
            temp_file.write(to_extract[x])
            temp_file.close()