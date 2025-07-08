#ignore warnings
class Calculator:
    """Calculator"""
    #ignore warnings
 
    def __init__(self,operator):
        """Constructor for Calculator class"""
        self.operator = operator
        
        #operator=input("Enter your opetaor(+,*,-,/): ")
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
       
        if operator =="+":
            self.result = num1 + num2
        elif operator== "-":
            self.result=num1/num2
        elif operator=="*":
            self.result=num1*num2
        elif operator=="/":
            self.result=num1/num2
            
        else:
            print("Invalid operator")

          
       
calc =Calculator(input("Enter your operator (+, *, -, /): "))
print(f"Result:{calc.result}")


                  
   
                  
    
    