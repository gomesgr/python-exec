"""
    Write a Python program which accepts the radius of a circle from the user and compute the area.
    
    Sample Output :
    r = 1.1
    Area = 3.8013271108436504
"""
from math import pi

raio = float(input('Digite um valor para o raio: '))
area = pi * raio ** 2
print(f'Area = {area:.3f}')