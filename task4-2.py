n_number=int(input("Enter a number to calculate Factorial Sum: "))
factorial_sum=0
for i in range(1,n_number+1):
    factorial=1
    for j in range(1,i+1):
        factorial*=j
    factorial_sum+=factorial
print(f"Sum of factorials is: {factorial_sum}")
