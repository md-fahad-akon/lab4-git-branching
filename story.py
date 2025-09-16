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
    act = input("Do you want to pull the sword out? (pull/help): ").strip().lower()
    if act == "pull":
        print("You pull the sword out and defeated the biggest dragon ever! Yay!")
    elif act == "help":
        print("You decided to get help and a fairy shows up to train you on how you can defeat a dragon.")
    else:
        print("You hesitate and the opportunity slips away.")

def center_path():
    print("You walk center and discover a hidden treasure chest filled with gold.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You bravely accept the challenge and win the duel!")

if __name__ == "__main__":
    intro()
