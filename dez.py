"""
    Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
    Sample value of n is 5
    Expected Result : 615
"""

value = int(input('Digite um valor: '))

v1 = int(f'{value}')
v2 = int(f'{value}{value}')
v3 = int(f'{value}{value}{value}')

print(v1 + v2 + v3)