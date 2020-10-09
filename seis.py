"""
    Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
"""

dados = input('Digite dados separados por , :')
sep_dados = dados.split(',')

sep_dados = [i.strip() for i in sep_dados]

print(f'List: {sep_dados}')
print(f'Tuple: {tuple(sep_dados)}')