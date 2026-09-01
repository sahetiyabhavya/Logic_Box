print("Welcome To Pattan And RangeData")

while True:
  
    print("Select An Option ")
    print("1. For Pattan ")
    print("2. For Rangedata ")
    print("3. For Exit")
    
    choice = int(input("Enter A Number Between 1 To 3: "))
    
    if choice==1:
        row = int(input("Enter Number Of Row "))
        for i in range(1,row+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
            
    elif choice==2 :
        start = int(input("Enter The Starting Number: "))
        end = int(input("Enter The Ending Number: "))
        sum = 0
        for i in range(start,end+1):
            if i%2==0:
                print(f"The Numnber {i} Is Even")
            else:
                print(f"The Number {i} Is Odd")
                
            sum = sum+i
        print(f"Total Number Of {start} To {end} is = {sum}")
        
        
    elif choice==3:
        print("Thank You For Using Pattan And Rangedata Game ")
        break
    