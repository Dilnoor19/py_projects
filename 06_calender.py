import calendar

year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))

a = calendar.month(year,month)

print(a)