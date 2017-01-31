# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    x = ord(letter) + n
    if x > 122:
        x = 97 + ((x - 122) % 26) - 1
    if x < 97:
        x = 122 - ((97 - x) % 26) + 1
    return chr(x)


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
print shift_n_letters('z', 26)
print shift_n_letters('a', 26)
