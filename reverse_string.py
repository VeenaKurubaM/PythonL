def pallindrome_string():
    """name is pallindrom"""
    name=input("enter name: ").strip()
    print(name[::-1])
    if name[0:]== name[::-1]:
        print("name is pallndrome")
    else:
        print("name is not pallndrome")
pallindrome_string()
    
    