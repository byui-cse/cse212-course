def move_up(y, fuel):
    """
    Move y up by 1 and fuel down by 5 (if there is enough fuel)
    Return the updated values
    """
    if fuel >= 5:
        y += 1
        fuel -= 5
    else:
        print("Not enough fuel!")
    return y, fuel

def move_down(y, fuel):
    """
    Move y down by 1 and fuel down by 5 (if there is enough fuel)
    Return the updated values
    """    
    if fuel >= 5:
        y -= 1
        fuel -= 5
    else:
        print("Not enough fuel!")
    return y, fuel

def move_left(x, fuel):
    """
    Move x down by 1 and fuel down by 5 (if there is enough fuel)
    Return the updated values
    """    
    if fuel >= 5:
        x -= 1
        fuel -= 5
    else:
        print("Not enough fuel!")
    return x, fuel

def move_right(x, fuel):
    """
    Move x up by 1 and fuel down by 5 (if there is enough fuel)
    Return the updated values
    """    
    if fuel >= 5:
        x += 1
        fuel -= 5
    else:
        print("Not enough fuel!")
    return x, fuel

def fire_laser(fuel):
    """
    Move fuel down by 10 and display the firing message (if there is enough fuel)
    Return the updated values
    """    
    if fuel >= 10:
        fuel -= 10
        print("Pew Pew!")
    else:
        print("Not enough fuel!")
    return fuel

def main():
    """
    Start with a robot at (5,5) with fuel of 100.  Provide a menu
    for the user to move the robot around.
    """
    choice = None
    robot_x = 5
    robot_y = 5
    robot_fuel = 100
    while choice != "q":
        print("Robot at ({},{}) with {} units fuel".format(
            robot_x, robot_y, robot_fuel))
        print("l)eft r)ight u)p d)own f)ire q)uit")
        choice = input("> ")

        # Call the appropriate function.  The current robot information
        # is sent to the function and the updated informaiton is returned
        # and saved.
        if choice == "l":
            robot_x, robot_fuel = move_left(robot_x, robot_fuel)
        elif choice == "r":
            robot_x, robot_fuel = move_right(robot_x, robot_fuel)
        elif choice == "u":
            robot_y, robot_fuel = move_up(robot_y, robot_fuel)
        elif choice == "d":
            robot_y, robot_fuel = move_down(robot_y, robot_fuel)                                    
        elif choice == "f":
            robot_fuel = fire_laser(robot_fuel)
        print()

# Start the program
main()            