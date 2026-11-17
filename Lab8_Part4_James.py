def fibonacci(N):
    
    if N<=1:
        return N
    else:
        return fibonacci(N-1) + fibonacci(N-2)
    
for i in range(int(input("Enter stopping number: S"))+1):
    print(f'fibonacci ({i}): {fibonacci(i)}')