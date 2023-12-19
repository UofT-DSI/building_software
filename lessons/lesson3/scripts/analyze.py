def analyze(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    num_lines = len(data)
    print(f"Number of lines in the file: {num_lines}")

if __name__ == "__main__":
    analyze('processed_data.txt')
