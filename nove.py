"""
    Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)
date = ''

for n in range(3):
    date += str(exam_st_date[n])
    if (n < 2):
        date += ' / '
print(date)
