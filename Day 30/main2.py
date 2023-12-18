try:
    file = open("asd.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("asd.txt", 'w')
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")
else:
    contet = file.read()
    print(contet)
finally:
    raise TypeError("This is an error that i made up.")