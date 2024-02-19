a = 9**8 + 3**5 - 9
string = ''
while a > 0:
    string += str(a % 3)
    a //= 3
print(string[::-1])
print(string.count('2'))