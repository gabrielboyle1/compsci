name = input("What is the name? \n").strip( )


if name:

    if name[:1].lower() <= "m":
        print("Name starts at or before M!")

    else:
        print("Name starts at or after N!")

## test !!!!!!!!!!!!!