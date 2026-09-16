"""
entry while
compare = 0
3 input vars
a b c 
a = input('1)')
b = input('2)')
c = input('3)')

if a > b:
    compare = len(a)
else:
    compare = len(b)

if b > c:
    compare = len(b)
else:
    compare = len(c)

if c > a:
    compare = len(c)
else:
    compare = len(a)


32 / 2 = 16 기준
14 / 2 = 7 
16 - 7 = 9
0 / 2  = 0 
16 - 0 = 0 
"""

while True:

    A = input("1) ")
    B = input("2) ")
    C = input("3) ")
    margin = int(input("여백:"))
    length = 0
    index = ord('A')

    for i in range (3):
        if i == 2:
            if len(globals()[chr(index + i)]) > len(globals()[chr(0)]):
                length = len(globals()[chr(index + i)])
                break

        if len(globals()[chr(index + i)]) > len(globals()[chr(index + i + 1)]):
            length = len(globals()[chr(index + i)])
            

    


    line  = 2 * (margin + 2) + length # generate line
    m = '*' + ' ' * margin
    
    print('*' * line) 



    print('*' * line)

