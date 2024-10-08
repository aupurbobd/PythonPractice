def isleapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                #print(f"{year} is a leap year")
            else:
                return False
                #print(f"{year} is not a leap year")
        else:
            return True
    else:
        return False
        #print(f"{year} is not a leap year")

def daysinmonth(year, month):
    days31 = [1, 3, 5, 7, 8, 10, 12]
    days30 = [4, 6, 9, 11]
    if month in days31:
        return 31
    elif month in days30:
        return 30
    else:
        if isleapyear(year) is True:
            return 29
        else:
            return 28
def days_in_a_month(year,month):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isleapyear(year) and month==2:
        return f'{months[month-1]}-{year} is in 29 days'
    else:
        return f'{months[month-1]}-{year} is in {days[month-1]} days'


year=int(input('Enter year:'))
month=int(input('Enter month number:'))

print(daysinmonth(year, month))
print(days_in_a_month(year,month))

