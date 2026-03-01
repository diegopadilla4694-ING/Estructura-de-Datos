def positive_sum(arr):
    
    bool = True
    while True:
        
        numeros = int(input("ingrese un numero por favor: "))
        
        if arr != 0 or arr != " ":
             arr.append(numeros)

        if numeros <= 0:
             break
    
    print(arr)
    total = 0
    for num in arr:
        total = total + num
        print(total)

positive_sum(arr=[])