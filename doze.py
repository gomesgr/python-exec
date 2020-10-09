"""
    Write a Python program to print the calendar of a given month and year.
    Note : Use 'calendar' module. 
"""
import calendar

ano = int(input('Digite um ano: '))
mes = int(input('Digite um mes: '))

cal = calendar.TextCalendar()
matrix = cal.formatmonth(ano, mes)
print(matrix)