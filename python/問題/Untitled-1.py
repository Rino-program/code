def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

# 使用例
file_path = 'example.txt'
print(f"The number of lines in the file is: {count_lines_in_file(file_path)}")