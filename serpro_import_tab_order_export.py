import csv

def format_data_line(line):
    data = line.strip().split(', ')
    formatted_data = []
    for i in range(0, len(data) - 1, 17):  # Set the tuple size to 17
        formatted_data.append(data[i:i+17])
    return formatted_data

def main():
    input_file_path = 'SERPRO-DB-CLASSIFICACAO-02.txt'  # Replace with your input file path
    output_file_path = 'sorted_data.csv'  # Replace with the desired output file path

    try:
        with open(input_file_path, 'r') as input_file:
            next(input_file)  # Skip the header row
            data_sets = []
            for line in input_file:
                formatted_data = format_data_line(line)
                data_sets.extend(formatted_data)
            
            # Sort data sets by the last column ('NOTA FINAL nas provas objetivas')
            sorted_data_sets = sorted(data_sets, key=lambda x: float(x[-1].split()[0]))

            # Write sorted data to CSV file
            with open(output_file_path, 'w', newline='') as output_file:
                csv_writer = csv.writer(output_file)
                csv_writer.writerow(['numero de inscricao', 'nome do candidato em ordem alfabetica', 'nota final Lingua Portuguesa', 'N.A. Lingua Portuguesa', 'nota final Lingua Inglesa', 'NA Lingua Inglesa', 'nota final Estatistica/Probabilidade', 'NA Estatistica/Probabilidade', 'nota final Raciocinio Logico', 'NA Raciocinio Logico', 'nota final Legislacao', 'NA Legislacao', 'nota final conhecimentos basicos (P1)', 'NA conhecimentos basicos (P1)', 'nota final conhecimentos especificos (P2)', 'NA conhecimentos especificos (P2)', 'NOTA FINAL nas provas objetivas'])
                for data_set in sorted_data_sets:
                    csv_writer.writerow(data_set)
            
            print(f"Sorted data has been saved to '{output_file_path}'.")
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")

if __name__ == '__main__':
    main()
