num = 25
import time
while num > 0:
    if num != 5 and num != 6 and num != 7 and num != 8 and num != 13:
        print(num)
        num -= 1
        time.sleep(0.25)
    else:
        num -= 1

