class weight:
    """ A class to convert the weight from kgs to pounds and vice versa"""
    #ignore warnings
    @staticmethod
    def weight_input():
        """Getting weight from user"""
        try:
            kgs_or_pounds=input("Enter wight in kgs or punds(kgs/pounds): ")
            kgs_or_pounds=kgs_or_pounds.lower()
            weight_user=input("Enter the weight : ")
            return kgs_or_pounds, float(weight_user)
        except Exception as e:
            print(f"Invalid input {e}")
            SystemExit()
    @staticmethod
    def converter(kgs_or_pounds, weight_user):
        """Convert Kgs to pounds"""
        if kgs_or_pounds=="kgs":
            weight= weight_user * 2.20462
            return weight
        else:
            weight=weight_user / 2.20462
            return weight
    @staticmethod
    def print_weight(kgs_or_pounds,converter):
        """Printing weight"""
        if kgs_or_pounds=="kgs":
            print(f"The user weight is : {converter} pounds")
        else:
            print(f"The user weight is : {converter} pounds")
            
    @staticmethod
    def main():
        kgs_or_pounds, weight_user=weight.weight_input()
        converter=weight.converter(kgs_or_pounds,weight_user)
        show_weight=weight.print_weight(kgs_or_pounds,converter)
        return show_weight
    
weight.main()
        
        
        