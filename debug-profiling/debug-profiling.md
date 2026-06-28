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