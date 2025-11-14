#Practical 2: Computing the GCD/HCF
#Approach 1: Using a variable which is updated as the highest factor changes

def gcd(m,n):
    for  i in range(1,min(m,n)+1):
        if m%i == 0 and n%i == 0:
            mrcf=i  #most recent common factor
    return mrcf

m,n=input("Enter two numbers separated by a comma: ").split(',')
m,n=int(m),int(n)
print(gcd(m,n))