def read_csv_and_sort(filename, target_student):
    with open(filename, 'r') as file:
        data = file.read().strip().split(' / ')

    student_data = []  # Create a list to store student data

    for student_info in data:
        inscricao, nome, nota = student_info.strip().split(', ')
        student_data.append((inscricao, nome, nota))

    # Sort the students by their marks (in descending order)
    sorted_data = sorted(student_data, key=lambda x: float(x[2].strip(' /')), reverse=True)

    total_students = len(sorted_data)  # Get the total number of students

    for position, (inscricao, nome, nota) in enumerate(sorted_data, start=1):
        print(f"Position: {position}, Inscricao: {inscricao}, Nome: {nome}, Nota: {nota}")

    for position, (inscricao, nome, nota) in enumerate(sorted_data, start=1):
        if inscricao == target_student:
            print(f"The target student, {target_student}, is at position {position} out of {total_students} students.")
            break

  

if __name__ == "__main__":
    csv_filename = "prova_pratica.csv"
    target_student = "10023132, Fabio Odaguiri, 35.00"
    read_csv_and_sort(csv_filename, target_student)
    
