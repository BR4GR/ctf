# Solution stonezarcon's Getting started

Opening the getting_started executable in Ghidra you find the following Funtion.

```c
  char *__s2;
  int local_20;
  int local_1c;
  
  piVar2 = (int *)malloc(0x18);
  if (param_1 < 2) {
    puts("Denied.");
  }
  else {
    *piVar2 = 0x6e;
    piVar2[1] = 0x60;
    piVar2[2] = 0x5e;
    piVar2[3] = 0x6d;
    piVar2[4] = 0x60;
    piVar2[5] = 0x6f;
    for (local_20 = 0; local_20 < 5; local_20 = local_20 + 1) {
      *piVar2 = *piVar2 + 1;
      piVar2[1] = piVar2[1] + 1;
      piVar2[2] = piVar2[2] + 1;
      piVar2[3] = piVar2[3] + 1;
      piVar2[4] = piVar2[4] + 1;
      piVar2[5] = piVar2[5] + 1;
    }
    __s2 = (char *)malloc(7);
    for (local_1c = 0; local_1c < 7; local_1c = local_1c + 1) {
      __s2[local_1c] = (char)piVar2[local_1c];
    }
    __s2[6] = '\0';
    iVar1 = strcmp(*(char **)(param_2 + 8),__s2);
    if (iVar1 == 0) {
      puts("Welcome.");
    }
    else {
      puts("Denied.");
    }
  }
  return 0; 
```


This C code snippet is an example of a simple command-line based authentication program using memory management functions and string comparisons. Here's a breakdown of what each part of the code does:

1. **Memory Allocation**: The program starts by allocating memory for an integer array `piVar2` with space for 6 integers using `malloc(0x18)`, which equals 24 bytes (as each int typically occupies 4 bytes).

2. **Initial Command-Line Argument Check**: It checks if the number of command-line arguments (`param_1`) is less than 2. If this condition is true, the program prints "Denied." and terminates. This check ensures that the user has provided at least one argument apart from the program's name itself.

3. **Initial Values and Manipulation**: 
    - The integer array `piVar2` is initialized with specific hex values: `0x6e`, `0x60`, `0x5e`, `0x6d`, `0x60`, `0x6f`.
    - A loop then increments each value in this array by 1, five times. This modifies each element in the array `piVar2`.

4. **Character Array Creation**: The program then allocates memory for a character array `__s2` of size 7 bytes, initializing a string that will store the ASCII characters corresponding to the integer values in `piVar2`.

5. **Conversion of Integer Array to Character Array**: 
    - A loop runs to convert each integer in `piVar2` to a character by type casting and assigns it to `__s2`. This effectively converts the modified hex values into ASCII characters.
    - The string `__s2` is null-terminated (`__s2[6] = '\0';`).

6. **String Comparison and Output**:
    - The program retrieves the first command-line argument passed by the user (`*(char **)(param_2 + 8)`) and compares it to the string `__s2` using `strcmp`.
    - If the strings match, it prints "Welcome."; otherwise, it prints "Denied."
    - the incremented array results in  `0x73`, `0x65`, `0x63`, `0x72`, `0x65`, `0x74` and the string `'\x73\x65\x63\x72\x65\x74\0'` which is **secret**.