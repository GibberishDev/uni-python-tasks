num_a=int(input("Enter number A: "))
num_b=int(input("Enter number B: "))
print("The sequence from A to B is: ")
if num_a==num_b:
    print(num_a)
else:
    seq=""
    if num_a>num_b:
        for i in range(num_a,num_b-1,-1):
            seq+=str(i) + " "
    else:
        for i in range(num_b,num_a-1,-1):
            seq=str(i) + " " + seq
    print(seq)