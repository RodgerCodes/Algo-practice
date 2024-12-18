

unsorted_list = [3, 5, 1, 6, 2, 9, 8]

def bubble_sort(unsorted_data):
    """
    Sort data
    """
    for i in range(len(unsorted_data)):
        for j in range(len(unsorted_data) - 1 - i):
            if unsorted_data[j] > unsorted_data[j + 1]:
                unsorted_data[j], unsorted_data[j + 1] = unsorted_data[j+1], unsorted_data[j]



bubble_sort(unsorted_list)
print(unsorted_list)