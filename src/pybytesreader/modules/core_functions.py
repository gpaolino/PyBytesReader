import argparse
import logging
import os.path

import pkg_resources

parser = argparse.ArgumentParser(description = 'Simple file reader in Python3.')

def get_version() -> str:
    version = pkg_resources.require('pybytesreader')[0].version
    project_name = pkg_resources.require('pybytesreader')[0].project_name
    return f'{project_name}, version {version}'
__VERSION__ = get_version()
parser.add_argument('-v', '--version', action = 'version', version = __VERSION__)

parser.add_argument('input_file', metavar = 'input_file', type = str, help = 'Input file path')
parser.add_argument('output_file', metavar = 'output_file', type = str, help = 'Output file name')
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

def set_output_directory() -> str:
    output_dir = './output/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def read_file_from_line_byte_by_byte(start_line, number_of_bytes) -> None:
    # Set default output directory
    output_file_path = set_output_directory() + output_file

    try:
        with open(input_file, 'rb') as infile, open(output_file_path, 'wb') as outfile:

            current_line: int = 0

            # Read until the desired line
            while current_line < start_line - 1:
                infile.readline()
                current_line += 1
            print(f'I read all the rows until the number {start_line - 1}')
    
            current_byte: int = 0

            # Start reading byte by byte from the desired line
            while (byte := infile.read(1)):
                if(current_byte == number_of_bytes):
                    break
                outfile.write(byte)
                current_byte += 1
            print(f'I just read the first {number_of_bytes} bytes starting from the row number {start_line}')
            
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        logging.log(logging.ERROR, f'{e}')
        raise e
    except Exception as e:
        logging.log(logging.ERROR, f'Unexpected error: {e}')
        raise e