#Practical 129: Computing the GCD/HCF
#Approach 1: Using a list CF (common factors)

def gcd(m,n):
    cf=[]
    for  i in range(1,min(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
    return cf[-1]

m,n=input("Enter two numbers separated by a comma: ").split(',')
m,n=int(m),int(n)
print(gcd(m,n))