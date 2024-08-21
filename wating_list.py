try:
    wating_list= ["hadis","marry"]
    name = input("enter name:" )

    number = wating_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")