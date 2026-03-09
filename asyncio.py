import asyncio                          # Line 1

async def say_hello(name, delay):       # Line 2
    await asyncio.sleep(delay)          # Line 3
    print(f"Hello, {name}!")            # Line 4

async def main():                       # Line 5
    await asyncio.gather(               # Line 6
        say_hello("Alice", 2),          # Line 7
        say_hello("Bob", 1),            # Line 8
    )                                   

asyncio.run(main())                     # Line 9
```

**Output:**
```
Hello, Bob!      ← appears after 1s
Hello, Alice!    ← appears after 2s