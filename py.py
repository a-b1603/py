"""
import time

ch, msg = input("문자:"), input("메시지:")
MSG = msg.upper()
margin = int(input('여백크기:'))
n = len(msg)
line = str(ch) * (n + margin * 2 + 2)
front = str(ch) + ' ' * margin
back = ' ' * margin + str(ch)
print(line)
print(front + msg + back)
print(front + MSG + back)
print(line)
"""

ch = input("문자:")
msg = input("메시지:")
MSG = msg.upper()
margin = int(input('여백:'))
n = len(msg)
loop = int(input('반복횟수:'))
line = str(ch) * ((n + margin * 2 + 2) * loop - (loop-1))
front = str(ch) + ' ' * margin
back = ' ' * margin 
 
print(line)
print((front + msg + back) * loop + str(ch))
print((front + MSG + back) * loop + str(ch))
print(line)
