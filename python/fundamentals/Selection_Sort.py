arr = [5,4,7,6,8,2,1,9,3,0]
def ordenar(arr):
    for j in range(len(arr)):
        min = arr[j]
        for i in range(len(arr)):
            if min < arr[i]:
                min = arr[i]
                arr[j], arr[i] = arr[i], arr[j] 
    return arr
print(ordenar(arr))