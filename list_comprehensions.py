####list comprehensions
symbols = '$#&*~'

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


##another way of doing this is 

symbols = '*&^%$#@!'

codes = []

codes = [ord(symbol) for symbol in symbols]
print(codes)
