def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid_el = len(arr) // 2
    left_arr = merge_sort(arr[:mid_el])
    right_arr = merge_sort(arr[mid_el:])
    
    return merge(left_arr, right_arr)


def merge(left, right):
    result = []
  
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])  # Corrected the wrong index
            j += 1

    return result + left[i:] + right[j:]


def main():  
    print(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]))


if __name__ == "__main__":
    main() 