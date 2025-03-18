num = 0
count = int(input("What number do you want to count by?"))
closest = 100 - count
import time

async def countdownfrom100():
    num = 100
    while num > 0:
        print(num)
        num -= count
        time.sleep(0.5)

while num < 100 and num != closest:
        num += count
        print(num)
        time.sleep(0.5)

if num == closest:
    print("You have reached 100, or the closest number below 100.")
    async def countdownfrom100() -> None:
        await countdownfrom100()

