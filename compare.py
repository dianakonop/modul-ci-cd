def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f)

def find_common_lines(lines1, lines2):
    return lines1 & lines2

def find_diff_lines(lines1, lines2):
    return lines1 ^ lines2

def write_lines(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in sorted(lines):
            f.write(line + '\n')

