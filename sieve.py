n = 100
i = 2
prime_list = []
possible_list = [i for i in range(2, n+1)]
while i**2<=n:
    if i in possible_list:
        prime_list.append(i)
        for j in possible_list:
            if j%i == 0:
                possible_list.remove(j)
            else:
                pass

    i+=1
for i in possible_list:
    prime_list.append(i)

print(prime_list)