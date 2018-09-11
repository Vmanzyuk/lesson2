def get_summ(num_one,num_two):
    try:
        num_one=int(num_one)
        num_two=int(num_two)
        return num_one+num_two
    except (ValueError):
        return'Please enter numbers'

print(get_summ('k',2))