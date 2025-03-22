def HCF_Routine (a:int, b:int) -> int:
    x = a
    y = b 
    if x == y:
        HCF = x
    else:
        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x
        HCF = x
    return HCF

def LCM_Routine (a:int, b:int) -> int:
    LCM = a*b//(HCF_Routine (a,b))
    return LCM
    
while True:
    print ('Enter  operation to perform on two fractions, or Exit')
    Operation = input ('Enter operation: ').strip() # this removes any spaces from before or after the input

    if Operation == 'Exit':
        print ('Program Ended.')
        break
    
    if Operation in ['Addition', 'Subtraction', 'Division', 'Multiplication']:
        while True:
            try: #try means attempt the following lines of code
                Num1 = int(input("Enter numerator of 1st fraction: "))
                Den1 = int(input("Enter denominator of 1st fraction: "))
                Num2 = int(input("Enter numerator of 2nd fraction: "))
                Den2 = int(input("Enter denominator of 2nd fraction: "))
                
                if Num1 <= 0 or Den1 <= 0 or Num2 <= 0 or Den2 <= 0:
                    print ('Error, all values must be greater than zero and an integer.')
                    continue
                break
            except ValueError:
                print("Error, please enter valid integers.")

    if Operation == 'Multiplication':
            a :int = Num1*Num2
            b: int = Den1*Den2
            HCF = HCF_Routine (a,b)
            a = a // HCF
            b = b // HCF
            print ('Product is:')
            width = max(len(str(a)), len(str(b)))
            print(f"{a}".rjust(width + 1))   # Right-align numerator
            print("-" * (width + 1))         # Print dashes properly
            print(f"{b}".rjust(width + 1))   # Right-align denominator  
    
    elif Operation == 'Division':
            a :int = Num1*Den2
            b: int = Num2*Den1
            HCF = HCF_Routine (a,b)
            a = a // HCF
            b = b // HCF
            print ('Quotient is:')
            width = max(len(str(a)), len(str(b)))
            print(f"{a}".rjust(width + 1))   # Right-align numerator
            print("-" * (width + 1))         # Print dashes properly
            print(f"{b}".rjust(width + 1))   # Right-align denominator
    
    elif Operation == 'Addition':
           LCM = LCM_Routine(Den1, Den2)
           NewNum1 = Num1 * (LCM // Den1) # uses the LCM subroutine to find the LCM of the two denominators
           NewNum2 = Num2 * (LCM // Den2)
           a = NewNum1 + NewNum2  # For addition
           b = LCM
           HCF = HCF_Routine (a,b)
           a //= HCF # this means that integer division is performed on a and then the result of the division is assigned to the variable a
           b //= HCF
           print ('Sum is:')
           width = max(len(str(a)), len(str(b))) # converts a and b into strings, finds the string length, and then max compares length of both strings, assigning the larger value to width.  
           print(f"{a}".rjust(width + 1))   # this means that spaces are added to the strings left in order to make the total length of the string = value of width + 1
           print("-" * (width + 1))         # this prints 'width + 1' dashes
           print(f"{b}".rjust(width + 1))   # Right-align denominator through same process as numerator
        

    elif Operation == 'Subtraction':
           LCM = LCM_Routine(Den1, Den2)
           NewNum1 = Num1 * (LCM // Den1)
           NewNum2 = Num2 * (LCM // Den2)
           a = NewNum1 - NewNum2  # For subtraction
           b = LCM
           sign = -1 if a < 0 else 1 # To store sign
           a = abs(a)  # abs means absolute value of a. we take its absolute value because when finding hcf we cannot have negative numbers. we will restore the sign later.
           HCF = HCF_Routine (a,b)
           a //= HCF
           b //= HCF
           a *= sign  # Restore sign
           print ('Difference is:')
           width = max(len(str(a)), len(str(b)))
           print(f"{a}".rjust(width + 1))  # Right-align numerator
           print("-" * (width + 1))         # Print dashes properly
           print(f"{b}".rjust(width + 1))   # Right-align denominator)
    
    elif Operation == 'Decimal':
        while True:
            try:
                Num = int(input('Enter numerator: '))
                Den = int(input('Enter denominator: '))
                if Num <= 0 or Den <= 0:
                    print ('Error, all values must be greater than zero and an integer.')
                    continue
                break
            except ValueError:
                print("Error, please enter valid integers.")
        print ('Fraction in decimal format is:')
        print (f'Decimal value: {Num / Den: .4f}')

    else:
        print("Invalid operation. Please enter a valid option.")
