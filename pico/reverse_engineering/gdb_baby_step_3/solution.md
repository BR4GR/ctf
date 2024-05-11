Examining memory

Just like in the previous problem, we want to pause program execution after a certain instruction has executed, but this time we want to examine memory instead of a register.

1. Set a breakpoint after the constant is written. `(gdb) b *main+25`
2. Run the program. `(gdb) run`
3. Examine memory like so: `(gdb) x/4xb $rbp-0x4`
```
picoCTF{0x6bc96222}
```

You’ll notice that the bytes are in reverse order. This is called little endian and it means that for any given number, the least significant bytes are written first. Big endian is the opposite, and this is what is more natural to people, the most significant bytes are written first. Little endianness is an aspect of the particular assembly language we are using: x86-64.