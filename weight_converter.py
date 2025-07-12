class weight:
    """ A class to convert the weight from kgs to pounds and vice versa"""
    #ignore warnings
    @staticmethod
    def weight_input():
        """Getting weight from user"""
        try:
            kgs_or_pounds=input("Enter wight in kgs or punds(K /L): ")
            kgs_or_pounds=kgs_or_pounds.upper()
            weight_user=input("Enter the weight : ")
            return kgs_or_pounds, float(weight_user)
        except Exception as e:
            print(f"Invalid input {e}")
            SystemExit()
    @staticmethod
    def converter(kgs_or_pounds, weight_user):
        
        try:  
            """Convert Kgs to pounds"""
            if kgs_or_pounds=="K":
                weight= weight_user * 2.20462
                return round(weight,2)
            elif kgs_or_pounds=="L":
                weight=weight_user / 2.20462
                return round(weight,2)
            else:
                print("Please enter valid input K for kgs and L for pounds")
                
        except Exception as e:
            print(f"Invalid input {e}") 
            SystemExit()
    @staticmethod
    def print_weight(kgs_or_pounds,converter):
        """Printing weight"""
        if kgs_or_pounds=="K":
            print(f"The user weight is : {converter} Pounds")
        else:
            print(f"The user weight is : {converter} Kilograms")
            
    @staticmethod
    def main():
        kgs_or_pounds, weight_user=weight.weight_input()
        converter=weight.converter(kgs_or_pounds,weight_user)
        show_weight=weight.print_weight(kgs_or_pounds,converter)
        return show_weight
    
weight.main()
        
        
        