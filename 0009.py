arr = [int(i) for i in input().strip().split(" ")]

def merge_sort(list: [], left: int, right: int):
    if left == right:
        return [list[left]]
    mid = (left + right - 1)//2
    arr_left = merge_sort(list, left, mid)
    arr_right = merge_sort(list, mid+1, right)
    
    head_left = 0
    head_right = 0
    n1 = mid - left + 1
    n2 = right - mid
    result = []
    
    while head_left < n1 and head_right < n2:
        if(arr_left[head_left] <= arr_right[head_right]):
            result.append(arr_left[head_left])
            head_left += 1
        else:
            result.append(arr_right[head_right])
            head_right += 1
    if head_left < n1:
        result = result + arr_left[head_left:]    
    if head_right < n2:
        result = result + arr_right[head_right:]
    return result

arr = merge_sort(arr, 0, len(arr)-1)

text = input().strip()

for s in text:
    i = ord(s) - ord("A")
    print(arr[i], end =" ")
