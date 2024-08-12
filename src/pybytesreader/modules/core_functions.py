def read_file_from_line_byte_by_byte(input_file, output_file, start_line, number_of_bytes) -> None:
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:

        current_line: int = 0

        # Read until the desired line
        while current_line < start_line - 1:
            infile.readline()
            current_line += 1
        print(f'I read all the rows until the number ', start_line - 1)
    
        current_byte: int = 0

        # Start reading byte by byte from the desired line
        while (byte := infile.read(1)):
            if(current_byte == number_of_bytes):
                break
            outfile.write(byte)
            current_byte += 1
        print(f'I just read the first ', number_of_bytes, ' bytes of the row number ', start_line)