culture = int(input())

days = 0
while culture % 2 == 0:  # i used mod to check if it is divisible by 2 yet
    culture = (
        culture // 2
    )  # i used google here to work out how to impliment the powers of 2
    days += 1  # this just keeps the days up


print(culture, days)
