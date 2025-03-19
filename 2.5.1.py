import asyncio
import tracemalloc

tracemalloc.start()

num = 0
count = int(input("What number do you want to count by?"))
closest = 100 - (100 % count)  # Ensures we get the closest multiple

async def countdownfrom100():
    global num  # Use global variable
    num = closest
    while num > 0:
        print(num)
        num -= count
        await asyncio.sleep(0.5)  # Async-friendly sleep

async def count_up():
    global num
    while num < 100 and num != closest:
        num += count
        print(num)
        await asyncio.sleep(0.5)

    if num == closest:
        print("You have reached 100, or the closest number below 100.")
        await countdownfrom100()  # Properly await the coroutine

async def main():
    await count_up()  # Start counting up

# Run the async function properly
asyncio.run(main())
