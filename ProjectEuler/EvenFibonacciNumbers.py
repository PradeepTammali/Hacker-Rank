sum = 2
first = 1
second = 2
third = 0
while third < 4000000:
    third = first+second
    first = second
    second = third
    if third % 2 == 0:
        sum += third
print(sum)
