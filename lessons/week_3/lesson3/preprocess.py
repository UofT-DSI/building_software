import datetime

def preprocess(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()
    
    processed_data = f"Processed on {datetime.datetime.now()}\n" + data

    with open(output_file, 'w') as file:
        file.write(processed_data)

if __name__ == "__main__":
    preprocess('data/sample_data.txt', 'processed_data.txt')