import argparse

try:
    import pybytesreader.modules.core_functions as cf
except ImportError as e:
    import logging
    logging.log(logging.ERROR, "Please run 'pip install -r requirements.txt'")
    raise e


parser = argparse.ArgumentParser(description = 'Simple file reader in Python3.')

__VERSION__ = cf.get_version()
parser.add_argument('-v', '--version', action = 'version', version = __VERSION__)

parser.add_argument('input_file', metavar = 'input_file', type = str, help = 'Input file path')
parser.add_argument('output_file', metavar = 'output_file', type = str, help = 'Output file name')


def main() -> None:

    # Parse input parameters
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    # Ask for user input
    start_line: int = int(input('Start reading from line number: '))
    number_of_bytes: int = int(input('Read this number of bytes: '))

    # Call subroutine
    cf.read_file_from_line_byte_by_byte(input_file, output_file, start_line, number_of_bytes)

    print('Press any key to exit...')
    input()


if __name__ == '__main__':
    main()
