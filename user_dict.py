class user_dict:
    """ class for sample dictionary operations """
    a_dict={"name":"John","age":30,"city":"SFO"}
   
    @staticmethod
    def main():
        """Main function to run the dictionary operations"""
        print(f"Dictionary: {user_dict.a_dict}")
        print(f"Keys: {user_dict.a_dict.keys()}")
        print(f"Values: {user_dict.a_dict.values()}")
        print(f"Items: {user_dict.a_dict.items()}")
        print(f"Name: {user_dict.a_dict['name']}")
        user_dict.a_dict['age'] = 65
        print(f"Updated Age: {user_dict.a_dict['age']}")
        user_dict.a_dict['country'] = "America"
        print(f"Added Country: {user_dict.a_dict['country']}")
        print(user_dict.a_dict)
        user_dict.reg_user()
    @staticmethod
    def reg_user():
        """Register a new user"""
        b_dict={"name":input("Enter your name: "), "age":int(input("Enter your age: ")), "city":input("Enter your city: ")}
        print(f"user name: {b_dict['name']}")
        print(f"registered user: {b_dict}") 
        return b_dict
    
user_dict.main()
    