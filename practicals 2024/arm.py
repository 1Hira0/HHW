for num in range(1000000000):
    m = num
    nl = []
    while m>0:
            nl.append(m%10)
            m = m//10
    p = len(nl)
    s = 0
    for i in nl:
        s += i**p
    if s == num:
        print(f"{s} is arm")
        for i in range(2, num//2):
            if num%i==0:
                pr = False
        else:
                print(f'{num} is prime and armstrong')
                rev = 0
                while m>0:
                    rev = rev*10 + m%10
                    m = m//10
                if rev == num:
                     if rev == s:
                          print(f'{rev} is arm and per')