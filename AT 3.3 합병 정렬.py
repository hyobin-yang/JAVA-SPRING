def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):  # a의 앞/뒷부분을 합병하여 b에 저장
        if i > mid:
            b[k] = a[j]  # 앞부분이 먼저 소진된 경우
            j += 1
        elif j > high:
            b[k] = a[i]  # 뒷부분이 먼저 소진된 경우
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]  # a[j]가 승자
            j += 1
        else:
            b[k] = a[i]  # a[i]가 승자
            i += 1
    for k in range(low, high + 1):
        a[k] = b[k]  # b를 a에 복사


def merge_sort(a, b, low, high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)       # 왼쪽 부분 순환 호출
    merge_sort(a, b, mid + 1, high)  # 오른쪽 부분 순환 호출
    print(input_list)
    merge(a, b, low, mid, high)      # 왼쪽과 오른쪽 부분 합병


input_list = [37, 10, 22, 30, 35, 13, 25, 24]
aux = [None] * len(input_list)  # 보조 리스트
print('정렬 전:\t', input_list)
merge_sort(input_list, aux, 0, len(input_list) - 1)  # 합병 정렬 호출
print('정렬 후 :\t', input_list)

