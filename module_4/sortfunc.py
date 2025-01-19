#nums = [4, 5, 9, 1, 4, 0, 3, 7, 2]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
    return ls

#print(bubble_sort(nums))

def selection_sort(ls):
    for i in range(len(ls)):
        low = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[low]:
                low = j
        ls[i], ls[low] = ls[low], ls[i]
    return ls

#print(selection_sort(nums))

def insertion_sort(ls):
    for i in range(1, len(ls)):
        low = ls[i]
        j = i - 1
        while j >= 0:
            if low < ls[j]:
                ls[j+1] = ls[j]
                ls[j] = low
                j = j - 1
            else:
                break
    return ls

#print(insertion_sort(nums))