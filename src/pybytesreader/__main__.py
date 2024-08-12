#!.venv\Scripts\python.exe

from pybytesreader.modules.core_functions import read_file_from_line_byte_by_byte as rfflbbb

def main() -> None:

    # Example of use
    input_file = 'examples/data/example_dataset.txt'
    output_file = 'examples/data/output_file.txt'
    start_line: int = 3  # Start reading from line 3
    number_of_bytes: int = 5 # Read the first 5 bytes of the start line

    rfflbbb(input_file, output_file, start_line, number_of_bytes)

    print('Press any key to exit...')
    input()


if __name__ == '__main__':
    main()
