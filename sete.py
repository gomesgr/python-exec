"""
    Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
    Sample filename : abc.java
    Output : java
"""
entrada = str(input('Digite o nome de um arquivo: '))
print(entrada.split('.')[1])