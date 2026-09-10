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

