## Debugging and Profiling

### Debugging

Debug a sorting algorithm: The following pseudocode implements merge sort but contains a bug. Implement it in a language of your choice, then use a debugger (gdb, lldb, pdb, or your IDE’s debugger) to find and fix the bug.

- See the merge_sort.py file. The incorrect element was being selected because of the incorrect if else statement:
```
if left[i] <= right[j]:
    result.append(left[i])
    i += 1
else:
    # Wrong index
    result.append(right[i]) → result.append(right[j])      
    j += 1
```


Install rr and use reverse debugging to find a corruption bug. Save this program as corruption.c.
Compile with gcc -g corruption.c -o corruption and run it. Student 1’s ID gets corrupted, but the corruption happens in a function that only touches student 0. Use rr record ./corruption and rr replay to find the culprit. Set a watchpoint on students[1].id and use reverse-continue after the corruption to find exactly which line of code overwrote it.

```
(rr) b 22
Breakpoint 1 at 0x5e8d26d281d2: file corruption.c, line 23.
(rr) watch students[1].id
Hardware watchpoint 2: students[1].id
(rr) c
Continuing.

Hardware watchpoint 2: students[1].id

Old value = 0
New value = 1002
init () at corruption.c:17
17          students[1].scores[0] = 90;
(rr) c
Continuing.
=== Initial state ===
Student 0: id=1001
Student 1: id=1002

Breakpoint 1, curve_scores (student_idx=0, curve=5) at corruption.c:23
23          for (int i = 0; i < 4; i++) {
(rr) c
Continuing.

Hardware watchpoint 2: students[1].id

Old value = 1002
New value = 1007
curve_scores (student_idx=0, curve=5) at corruption.c:23
23          for (int i = 0; i < 4; i++) {
(rr) c
Continuing.

=== After curving ===
Student 0: id=1001
Student 1: id=1007

ERROR: Student 1's ID was corrupted! Expected 1002, got 1007
```

 - The bug is the for statement in line 23, because the student scores are 3, not 4:

```
for (int i = 0; i < 4; i++) {
    students[student_idx].scores[i] += curve;
}

correct: for (int i = 0; i < 3; i++)  
```


Debug a memory error with AddressSanitizer. Save this as uaf.c.
First compile and run without sanitizers: gcc uaf.c -o uaf && ./uaf. It may appear to work. Now compile with AddressSanitizer: gcc -fsanitize=address -g uaf.c -o uaf && ./uaf. Read the error report. What bug does ASan find? Fix the issue it identifies.

 - The greeting array gets used after its memory is freed: 
```
free(greeting);

greeting[0] = 'J';
printf("%s\n", greeting);

 ==1918==ERROR: AddressSanitizer: heap-use-after-free on address 0x503000000040 at pc 0x578e978202ca bp 0x7fffef31d390 sp 0x7fffef31d380
```

- To correct this, just move free(greeting) at the end