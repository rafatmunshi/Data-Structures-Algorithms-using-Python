a= 7 # 0111
b= 6 # 0110
c = -10
print(a&b) # bitwise AND operator- 0110, Return 1 if both the bits are 1 else 0
print(a|b) # bitwise OR operator- 0111, Return 1 if either of the bit is 1 else 0
print(a^b) # bitwise EXOR- 0001, REturn 1 if both bits are different, and 0 if both bits are same
print(~a) # bitwise NOT operator 1000 - 8 in decimal, Return ones compliment of hte number

print(a >> 1) # 0111 0011 Bitwise Right shift, if right shifted by 1 bit, it divides by 2
print(a << 1) # 0111 1110 Bitwise Left shift, if left shifted by 1 bit, it multiplies by 2

print(c >> 1) # 0111 0011 Bitwise Right shift, if right shifted by 1 bit, it divides by 2
print(c << 1) # 0111 1110 Bitwise Left shift, if left shifted by 1 bit, it multiplies by 2

# x & (x-1) # Clears the last set bit
# x & ~(x-1) # extracts the lowest set bit
# x & (x + (1 << n)) # clears the nth bit
# x & ~(x + (1 << n))
# x | (x + 1)
# x | ~(x + 1)
# x | (x - (1 << n))
# x | ~(x - (1 << n))
#
# 1. Get a bit (ith position of num)
# num & (1 << i)
#
# 2. set a bit (ith position of num)
# num | (1 << i)
#
# 3. clear ith bit
# mask= ~(1 << i)
# num & mask

# X^X = 0 ^ X = X