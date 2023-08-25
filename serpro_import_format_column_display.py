def format_data_line(line):
    data = line.strip().split(', ')
    formatted_data = []
    for i in range(0, len(data) - 1, 2):
        formatted_data.append(f"{data[i]}: {data[i + 1]}")
    formatted_data.append(data[-1])  # Adding the last datum
    return ' / '.join(formatted_data)

def main():
    file_path = 'SERPRO-DB-CLASSIFICACAO-02.txt'  # Replace with your file path

    try:
        with open(file_path, 'r') as file:
            for line in file:
                formatted_line = format_data_line(line)
                print(formatted_line)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == '__main__':
    main()
