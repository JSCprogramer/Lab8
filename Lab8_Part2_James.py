def sumof_even(N):
    if N <= 0:
        return 0
    
    
    
    N=int(input("Enter stopping number: "))
    total=0
    for x in range(2,N+1,2):
        total=total+x
        
    print(f'The sum of even numbers from 1 to {N} is: {total}')
    
