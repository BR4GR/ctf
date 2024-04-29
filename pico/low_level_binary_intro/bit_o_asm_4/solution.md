Can you figure out what is in the eax register? 
Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. 
If the answer was 0x11 your flag would be picoCTF{17}.

### Assembly Code Breakdown:

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

1. **Instructions +0 to +11: Function Prologue**
   - `endbr64`: No operational effect; typically for security features against certain exploits.
   - `push rbp`: Saves the base pointer on the stack.
   - `mov rbp, rsp`: Sets the base pointer to the current stack pointer.
   - `mov DWORD PTR [rbp-0x14], edi` and `mov QWORD PTR [rbp-0x20], rsi`: Saves function parameters to the stack (local variables).

2. **Instruction +15: Initializing Local Variable**
   - `mov DWORD PTR [rbp-0x4], 0x9fe1a`: Stores the hexadecimal value `0x9fe1a` (decimal 654874) in a local variable at `[rbp-0x4]`.

3. **Instruction +22: Compare Operation**
   - `cmp DWORD PTR [rbp-0x4], 0x2710`: Compares the value at `[rbp-0x4]` (654874) to `0x2710` (decimal 10000).

4. **Instruction +29: Conditional Jump Based on Compare**
   - `jle 0x55555555514e`: Jumps to address `0x55555555514e` if the value is less than or equal to 10000. Since 654810 is greater, this jump will not be taken.

5. **Instructions +31 and +35: Subtract Operation and Unconditional Jump**
   - `sub DWORD PTR [rbp-0x4], 0x65`: Subtracts `0x65` (decimal 101) from the value at `[rbp-0x4]`.
   - The new value becomes 654874 - 101 = 654773.
   - `jmp 0x555555555152`: Jumps to the address `0x555555555152 <main+41>`, skipping over the next instruction.

6. **Instruction +37: Add Operation (Skipped)**
   - This instruction would add `0x65` to `[rbp-0x4]`, but it is skipped due to the unconditional jump.

7. **Instruction +41: Move to `eax`**
   - `mov eax, DWORD PTR [rbp-0x4]`: Moves the current value at `[rbp-0x4]` (654773) into the `eax` register.

8. **Instructions +44 and +45: Function Epilogue**
   - `pop rbp`: Restores the base pointer.
   - `ret`: Returns from the function.


### Putting it in picoCTF flag format:

```
picoCTF{654773}
```