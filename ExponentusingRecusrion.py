def calc_exponent(base,power):
    if(power == 1):
        return base
    else:
        return base * calc_exponent(base,power-1)
    
n = int(input("Enter a base value: "))
p = int(input("Enter power value: "))
print(calc_exponent(n,p))