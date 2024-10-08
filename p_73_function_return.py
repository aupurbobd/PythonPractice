def add(a,b):
    c=a+b
    return c

def format_name(fname, lname):
    first_name=fname.title()
    last_name=lname.title()
    return f'{first_name}, {last_name}'


print(add(5,9))

print(format_name('JAHANGIR','ALAM'))