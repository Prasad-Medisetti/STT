EURO = 0.01417
BRITISH_POUND = 0.0100
AUSTRALIUN_DOLLAR = 0.02140
CANADIAN_DOLLAR = 0.02027
while 1:
    print("Choose a conversion", "0. Exit", "1. EURO", "2. BRITISH_POUND", "3. AUSTRALIUN_DOLLAR", "4. CANADIAN_DOLLAR", sep="\n")
    ch = int(input("Enter Choice:"))
    n = int(input("Enter amount in Rupees:\t"))
    if ch == 0:
        break
    elif ch == 1:
        print(n * EURO)
    elif ch == 2:
        print(n * BRITISH_POUND)
    elif ch == 3:
        print( n * AUSTRALIUN_DOLLAR)
    elif ch == 4:
        print(n * CANADIAN_DOLLAR)
    else:
        print("invalid choice...")