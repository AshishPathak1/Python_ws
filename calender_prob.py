import calendar
import sys
date_of_birth = input("Enter your date of birth (DD/MM/YYY): ")

if len(date_of_birth) != 10:
    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
else:
    date_parts = date_of_birth.split('/')
    if len(date_parts) != 3:
        print("Invalid date format. Please enter a valid date.",file=sys.stderr)
        sys.exit(0)
    else:
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
        if len(str(year)) != 4 or not (1 <= month <= 12) or not (1 <= day <= 31):
            print("Invalid date format. Please enter a valid date.",file=sys.stderr)
            sys.exit(0)
        else:
            day_of_week = calendar.weekday(year, month, day)
            day_name = calendar.day_name[day_of_week]
            print("You were born on ", day_name)
