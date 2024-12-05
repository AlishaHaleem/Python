def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# TODO: Example calls to the function
print(is_leap_year(2400))
print(is_leap_year(1989))
print(is_leap_year(2000))
print(is_leap_year(2100))