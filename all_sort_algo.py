def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n // 2):
        min_idx = i
        max_idx = i
        for j in range(i, n - i):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        if max_idx == i:
            max_idx = min_idx

        arr[n - i - 1], arr[max_idx] = arr[max_idx], arr[n - i - 1]

def binary_search(arr, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i)
        arr[j+1:i+1] = arr[j:i]
        arr[j] = key

def main():
    arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    
    while True:
        print("\nSelect a sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            bubble_sort(arr)
            print("Sorted array using Bubble Sort:", arr)
        elif choice == 2:
            selection_sort(arr)
            print("Sorted array using Selection Sort:", arr)
        elif choice == 3:
            insertion_sort(arr)
            print("Sorted array using Insertion Sort:", arr)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
