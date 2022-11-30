num =  int(input('Введите число: '))
list = [0]

def Fibonacci(num):
    if num in [1, 2]:                       
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

def NegaFibonacci(num):
    if num == 1:                       
        return 1
    elif num == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, num):
            num1, num2 = num2, num1 - num2
        return num2
        
for e in range(1, num + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)