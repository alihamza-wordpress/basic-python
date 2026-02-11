numbers = [ 1, 2, 3,-3, -7, -2]
for num in numbers:
    print(num)


numbers = [ 1, 2, 3,-3, -7, -2]
positive_numbers_count = 0
for num in numbers:
    if num >0:
        positive_numbers_count += 1
print("final coount for positive numbers:", positive_numbers_count)