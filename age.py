age=input('Enter your age:')
intage=int(age)
def destiny(age):
    if age < 3:
        return 'The program does not support age less 3'
    elif age < 7:
        return'What do you think about your kindergarten ?'
    elif age < 17:
        return 'I guess you studying in school'
    elif age < 22:
        return 'Student'
    elif age > 21:
        return 'Worker'   
print(destiny(intage))