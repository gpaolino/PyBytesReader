#!.venv\Scripts\python.exe

try:
    import pybytesreader.modules.core_functions as cf
except ImportError as e:
    import logging
    logging.log(logging.ERROR, "Please run 'pip install -r requirements.txt'")
    raise e

def main() -> None:

    # Example of usage
    #input_file = input('Input file path: ')
    #output_file = input('Output file name: ')
    start_line: int = int(input('Start reading from line number: '))
    number_of_bytes: int = int(input('Read this number of bytes: '))

    cf.read_file_from_line_byte_by_byte(start_line, number_of_bytes)

    print('Press any key to exit...')
    input()


if __name__ == '__main__':
    main()
