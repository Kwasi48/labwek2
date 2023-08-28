def is_even(x):
    if not (x % 2 == 0):
        return  x

numbers = [1,56,234,87,4,76,24,69,90,135]

no = list(filter(is_even, numbers))
print(no)