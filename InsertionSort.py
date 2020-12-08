def insertion_sort(arr):

    for i in range(1, len(arr)):

        position = i
        currentvalue = arr[i]

        while position > 0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position-=1

        arr[position]=currentvalue

    return arr