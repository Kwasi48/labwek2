from functools import reduce

total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
print(total)

def join_strings(words):
    k = reduce(lambda w1, w2: w1 + w2, words)
    return k



words = ["hello", "world"]
helloworld = join_strings(words) # "hello world"
print(helloworld)