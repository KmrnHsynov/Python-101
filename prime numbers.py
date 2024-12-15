def is_prime(eded: int) -> bool:
    if eded <= 1:
        return False
    for i in range(2, int(eded**0.5) + 1):
        if eded % i == 0:
            return False
    return True    

while True:
    try:
        eded = int(input("eded yaz bir seyler: "))
        res = is_prime(eded)
        print("eded sadedir" if res else "eded sade deyil")
    except ValueError:
        print("zehmet olmasa ede yazin!")



    