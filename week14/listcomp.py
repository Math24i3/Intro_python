import string

# two ways in making a list (comprehensions)
l = []
for i in range(1, 10):
    l.append(i)
print(l)
# another way
lc = [i for i in range(1, 10)]
print(lc)

# listing the english alphabet with chr()
englishAlph = [chr(i) for i in range(65, 91)]
print(englishAlph)

# different comprehensions for listing with string
alphabet = [l for l in string.ascii_uppercase]
print(alphabet)

alphabet2 = list(string.ascii_uppercase)
print(alphabet2)

alphabet3 = []
for l in string.ascii_uppercase:
    alphabet3.append(l)
print(alphabet3)

# print list of alphabet, but exclude every fifth letter
exAlh = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]
print(exAlh)

# a list of t-shirt colors'n sizes
colors = ['white', 'black']
sizes = ['s', 'm', 'l', 'xl']

shirts = [(color, size) 