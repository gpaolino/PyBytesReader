#!.venv\Scripts\python.exe

from pybytesreader.modules.core_functions import read_file_from_line_byte_by_byte as rfflbbb

def main() -> None:

    # Example of use
    input_file = input('Input file path: ')
    output_file = input('Output file name: ')
    start_line: int = int(input('Start reading from line number: '))
    number_of_bytes: int = int(input('Read this number of bytes: '))

    rfflbbb(input_file, output_file, start_line, number_of_bytes)

    print('Press any key to exit...')
    input()


if __name__ == '__main__':
    main()
