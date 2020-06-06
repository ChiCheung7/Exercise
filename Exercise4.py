num = int(input("Number? "))
for div in range(1, num+1):
    if num % div == 0:
        print(div)

b = [div for div in range(1, num+1) if num % div == 0]
print(b)
