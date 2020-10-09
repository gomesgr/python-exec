# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
nome = str(input('Digite seu primeiro e ultimo nome: '))
list_nome = nome.split(' ')
list_nome = list_nome[::-1]
print(' '.join(list_nome))