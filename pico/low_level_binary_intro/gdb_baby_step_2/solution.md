
Notice how the code jumps backwards! The same block of code is executed multiple times. This is how a loop looks in assembly language. To statically figure out what is in eax at main+56 we’d have to precisely calculate how many times this loop runs. This is possible, but in this case, we can easily set a breakpoint to pause program execution after the loop. To set a breakpoint and examine eax, follow these steps:

1. (gdb) break *main+59 This sets a breakpoint at the instruction immediately after the one in question. This guarantees that the instruction in question has actually been executed.
2. (gdb) run This lets the program run until it tries to execute the instruction at our breakpoint.
3. (gdb) info registers eax This prints out our answer in hexadecimal and decimal.

```
eax 0x4af4b 307019
picoCTF{307019}
```