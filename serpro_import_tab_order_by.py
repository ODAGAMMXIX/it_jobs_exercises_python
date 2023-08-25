def format_data_line(line):
    data = line.strip().split(', ')
    formatted_data = []
    for i in range(0, len(data) - 1, 17):  # Set the tuple size to 17
        formatted_data.append(data[i:i+17])
    return formatted_data

def main():
    file_path = 'SERPRO-DB-CLASSIFICACAO-02.txt'  # Replace with your file path

    try:
        with open(file_path, 'r') as file:
            next(file)  # Skip the header row
            data_sets = []
            for line in file:
                formatted_data = format_data_line(line)
                data_sets.extend(formatted_data)
            
            # Sort data sets by the last column ('NOTA FINAL nas provas objetivas')
            sorted_data_sets = sorted(data_sets, key=lambda x: float(x[-1].split()[0]))

            # Print the sorted data sets
            for data_set in sorted_data_sets:
                print(data_set)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == '__main__':
    main()
