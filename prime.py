def printing_prime_number(num):
    for i in range(2,num+1):
        h = i//2
        bo = True
        for j in range(2,h+1):
            if i % j == 0:
                bo = False
                break
        if bo == True:
            print(i)

printing_prime_number(500)












