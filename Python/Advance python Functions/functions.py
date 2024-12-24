# Function :
def Hellofun() :
    print("Hello world")
    
#lambda expression
sqaure = lambda x : x*x
# print(sqaure(5))

# addition = lambda a,b : a+b;
# print(addition(10,50))

# Decorators
# def div(a,b) :
#     print(a/b)
  
# def decorator(func) :
#     def tempDiv(a,b) :
#          if b > a : 
#              a , b = b, a
#          return  func(a,b);
#     return tempDiv;
    
# div = decorator(div);
# div(2,10)

# Recursion :

def factorial(n):
    if n == 0 :
        return 1;
    return n * factorial(n-1)
print(factorial(4))