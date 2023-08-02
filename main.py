#57
#Поиск индекса наименьшего значения элемента массива
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#Сортировка массива
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

#Примеры для проверки
print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([100, 32, 60, 4, 00]))