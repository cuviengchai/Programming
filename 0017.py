def merge_sort(list: [], left: int, right: int):
    
    if left == right :
        return [list[left]]
    
    mid = (left+right-1)//2
    arr_left = merge_sort(list, left, mid)
    arr_right = merge_sort(list, mid+1, right)

    l = mid - left + 1
    r = right - mid
    result = []
    h_left = 0
    h_right = 0

    while h_left < l and h_right < r:
        if arr_left[h_left] <= arr_right[h_right]:
            result.append(arr_left[h_left])
            h_left +=1
        else:
            result.append(arr_right[h_right])
            h_right +=1
    if h_left < l:
        result += arr_left[h_left:]
    if h_right < r:
        result += arr_right[h_right:]
    return result

text = [int(i) for i in input().strip().split(" ")]
arr = merge_sort(text, 0, len(text) - 1)
print(arr[0]*arr[2])