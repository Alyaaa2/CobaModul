from sport_salary import *
surname = input('Coach surname:')
job = input('Employment (1-full, 2-hourly):')
if job == '1':
    experience = int(input('Experience in years:'))
    salary = get_full_time(experience)
elif job == '2':
    hours = int(input('Hours worked:'))
    salary = get_part_time(hours)
print(surname, '-', salary)