def function1(S):
    count = 0
    for i in range(1, len(S)+1): 
        for j in range(0, 10):
            if i == 1:
                if (int(S[:-1])*10+ j)%3 == 0: 
                    print((int(S[:-i])*10 + j))
                    count += 1
            elif i = len(s):
                if (10**(i-1)*j + int(S)%10**(i-1))%3 == 0:
                    print((10**(i-1)*j + int(S)%10**(i-1)))
                    count += 1
            else:
                if (int(s[:-i])*(10**i) + 10**(i-1)*j+ int(s[-1+1:]))%3 == 0: 
                    print((int(s[:-i])*(10**i) + 10**(i-1)*j+ int(s[-1+1:]))) 
                    count += 1
    return count
