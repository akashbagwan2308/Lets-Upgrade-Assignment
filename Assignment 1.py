
for num in range(1,201):
    if num>=1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)