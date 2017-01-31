# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    x = ord(letter) + n
    if x > 122:
        x = 97 + ((x - 122) % 26) - 1
    if x < 97:
        x = 122 - ((97 - x) % 26) + 1
    return chr(x)

def rotate(t, n):
    s = ''
    for c in t:
        if c == ' ':
            s += ' '
        else:
            s += shift_n_letters(c, n)
    return s
    
print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
print rotate('this course teaches you to code', 7)
