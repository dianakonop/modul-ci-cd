def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f)