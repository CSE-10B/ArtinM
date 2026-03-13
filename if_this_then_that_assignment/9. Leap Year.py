def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #leap year if divisible by 4, except years divisible by 100 unless also divisible by 400

year = int(input())

result = leap(year) #call function, "result " is either true or false

print(result)