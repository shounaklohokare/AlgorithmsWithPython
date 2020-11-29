def binary_search(arr, key):

    start = 0
    end = len(arr) - 1

    found = False

    while start<=end and not found:

        mid = (start+end)//2

        if arr[mid]==key:
            found = True

        else:
            if key < arr[mid]:
                end = mid-1

            else:
                start = mid + 1

    return found


def recursive_binary_search(arr, key):

    if len(arr) == 0:
        return False

    else:

        mid = len(arr)//2

        if arr[mid] == key:
            return True

        else:
            if key < arr[mid]:
                return recursive_binary_search(arr[:mid], key)

            else:
                return recursive_binary_search(arr[mid+1:], key)