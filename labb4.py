sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)

print([len(word) for word in words])

print([len(word) for word in words if word != "the"])

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([ num for num in numbers if num > 0])

numbers1 = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print([num for num in numbers1 if num % 2 == 0])

words = ["hello", "my", "name", "is", "Sam"]

print([(word.upper(), len(word)) for word in words])
