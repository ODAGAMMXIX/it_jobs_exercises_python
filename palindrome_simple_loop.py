def is_palindrome(word):
    word = word.lower()
    length = len(word)
    
    for i in range(length):
        if word[i] != word[length - i - 1]: #TERRA RADAR 
            return False
    return True

def main():
    # Read the input word from the user
    word = input("Enter a word: ")

    is_palidrome = is_palindrome(word)
    if is_palidrome: # == True: 
    # Check if the word is a palindrome
    #if is_palindrome(word):
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

if __name__ == '__main__':
    main()

#n this version of the code, 
# we use a loop to iterate through
#  the characters of the word. 
# The loop variable i starts from 0 and goes up to length - 1.
#  We compare the characters at index i and length - i - 1
#  to check for palindromes. 
# If the characters are not equal at any point, we return False.
#  If the loop completes without finding a mismatch, 
# we return True, indicating that the word is a palindrome.



import mysql.connector

# Configuração da conexão com o banco de dados ++ pip3 install mysql
config = {
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'host': 'localhost',
    'database': 'seu_banco_de_dados'
}

# Conectando ao banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão estabelecida com sucesso!")

    # A partir daqui, você pode executar suas consultas SQL
    # por meio do objeto 'conn'

    # Exemplo de consulta
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sua_tabela")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

    # Finaliza a conexão
    conn.close()

except mysql.connector.Error as err:
    print(f"Erro ao conectar no banco de dados: {err}")