def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "center":
        center_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def center_path():
    print("You walk center and discover a hidden treasure chest filled with gold.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You seize dark power and strike the squirrel down with full of cruelty.")

if __name__ == "__main__":
    intro()
