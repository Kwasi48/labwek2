def is_even(x):
    if x % 2 == 0:
        return x



    

numbers = [1,56,234,87,4,76,24,69,90,135]
#num =  list(map(is_even, numbers))

num  = list(filter((lambda x : x % 2 == 0), numbers))
num1  = list(filter((lambda x : x % 2 != 0), numbers))
print(num)
print(num1)
