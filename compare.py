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


def compare_files(file1, file2):
    lines1 = read_file_lines(file1)
    lines2 = read_file_lines(file2)

    same = find_common_lines(lines1, lines2)
    diff = find_diff_lines(lines1, lines2)

    write_lines('same.txt', same)
    write_lines('diff.txt', diff)


if __name__ == "__main__":
    compare_files("file1.txt", "file2.txt")