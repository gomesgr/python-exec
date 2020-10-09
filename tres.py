"""
    Write a Python program to display the current date and time.
    Sample Output :
    Current date and time :
    2014-07-05 14:34:14
"""
from datetime import datetime
today = datetime.now()
print(today.strftime('%Y-%m-%d %H:%M:%S'))
