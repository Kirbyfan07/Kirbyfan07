def initialize_game():
    state = {
        "time": 91,
        "power": 153,
        "cams": 1,
        "move_rabbit": 0,
        "kill_rabbit": 0,
        "dead_rabbit": False,
        "move_rabbit_dec": 0,
        "dead_rabbit_force": 6,
        "move_bird": 0,
        "move_fox": 0,
        "kill_fox": 0,
        "move_fox_dec": 0,
        "fox_warning": False,
        "dead_fox": False,
        "move_bear": 0,
        "kill_bear": 0,
        "dead_bear": False,
        "dead_bear_force": 6,
        "look_left": False,
        "look_right": False,
        "light_on_L": False,
        "light_on_R": False,
        "door_close_L": False,
        "door_close_R": False,
        "cams_on": False,
        "power_out": False,
    }
    return state

def print_info():
    print("\n====================================================")
    print("                         INFO                        ")
    print("====================================================")
    print("You need to survive from 3am to 6am")
    print("Time moves per input action")
    print("A new threat gets added every hour")
    print("\nTo survive you need to do the following:")
    print("1. Check doors and cams for threats")
    print("2. If threats are at the doors, close them")
    print("3. The fox will show off and slow down when watched, close the door he rushes to")
    print("4. The bear hates the light in the cams and will stop if looked at, but always heads to you")
    print("5. The rabbit and the bird stick to one side, but are fast in differnt ways")
    print("6. One is fast to get to your office, the other is fast to get in")
    print("Every action costs power, don't run out")
    print("\nInputs are the following:")
    print("1. 'wait' lets time move without moving")
    print("2. 'left' go to left side of your office")
    print("3. 'right' go to right side of your office")
    print("4. 'light' turn lights on/off (costs 1 power per turn while on)")
    print("5. 'door' open/close door (costs 1 power per turn while shut)")
    print("6. 'cams' open camera monitor (costs 1 power per turn while in), While in cams, inputs are:")
    print("   '1' to '8' to swap camera channels")
    print("   'exit' to close monitor and return to office")
    print("   Going to cams bring you to the center of your office")
    print("====================================================\n")

def play_game():
    state = initialize_game()
    print("Good luck!")

    while True:
        # Time decrement and events
        state["time"] -= 1

        if state["time"] == 90:
            print("-- It's 3am, the start of your shift --")
        elif state["time"] == 60:
            print("-- It's now 4am, The Fox is waking up --")
            state["move_fox"] = 1
        elif state["time"] == 30:
            print("-- It's now 5am, The Bear begins moving --")
            state["move_bear"] = 1
            state["bear"] = 1
        elif state["time"] <= 0:
            print("\n====================================================")
            print("It's now 6am, your shift has ended")
            print("You win!")
            print(f"Leftover power: {state['power']}/153")
            print("====================================================\n")
            return True  # Win

        # Power drain from doors and lights
        if state["door_close_L"]:
            state["power"] -= 1
            print("-- You hear the grinding of the gears in the door to your left --")
        if state["door_close_R"]:
            state["power"] -= 1
            print("-- You hear the grinding of the gears in the door to your right --")
        if state["light_on_L"]:
            state["power"] -= 1
            print("-- You hear the buzzing of the lights to your left --")
            if state ["look_left"]:
                if state["kill_rabbit"] >=1 and not state["dead_rabbit"]:
                    print("-- you see the rabbit tapping on the window --")
        if state["light_on_R"]:
            state["power"] -= 1
            print("-- You hear the buzzing of the lights to your right --")
            if state ["look_right"]:
                if state ["kill_bear"] >= 1 and not state ["dead_bear"]:
                    print("-- you see the bear standing at the door, it looks looks like it not going to leave --")

        # Check power out
        if state["power"] <= 0:
            print("-- The power ran out --")
            state["power_out"] = True
        
        # Rabbit movement and attack logic
        state["move_rabbit"]+= 0.4
        print(state["move_rabbit"])
        if state["move_rabbit"] in [6, 6.2]:
            state["kill_rabbit"] = 1
        if state["kill_rabbit"] >= 1:
            if not state["door_close_L"]:
                if state["kill_rabbit"] == 5:
                    state["kill_rabbit"] = 0
                    state["dead_rabbit"] = True
                    state["kill_rabbit"] += 1
            else:
                if state["kill_rabbit"] == 5:
                    state["kill_rabbit"] = 0
                    state["move_rabbit_dec"] = state["move_rabbit"] - 0.4
                    state["move_rabbit"] = state["move_rabbit_dec"] - 1
                    if state["move_rabbit"] != 0:
                        state["move_rabbit"] *= -1
                    print("-- You hear a bang at the left door, then stomps heading away from the door --")
                else:
                    state["kill_rabbit"] += 1
                
        if state["dead_rabbit"]:
            print("-- You feel like the rabbit is inside your office getting ready to attack --")
            state["dead_rabbit_force"] -= 1
                
        if state["dead_rabbit_force"] == 0:
            print("\n====================================================")
            print("you get knocks over onto the floor while you where watching the cams")
            print("when you turn to see what knocked you over you see the rabbit in the air")
            print("it land on your back and starts jumping on you, squishing you to death")
            print("Game over")
            print("====================================================\n")
            return False

        # Fox movement and attack logic
        if state["move_fox"] != 0:
            state["move_fox"] += 1
        
        if state["move_fox"] in [7, 7.5]:
            state["kill_fox"] = 1

        if state["kill_fox"] >= 1:
            if not state["door_close_L"]:
                if state["kill_fox"] == 5:
                    state["kill_fox"] = 0
                    state["dead_fox"] = True
                state["kill_fox"] += 1
            else:
                if state["kill_fox"] == 5:
                    state["fox_warning"] = False
                    state["kill_fox"] = 0
                    state["move_fox_dec"] = state["move_fox"] - 0.5
                    state["move_fox"] = state["move_fox_dec"] - 1
                    if state["move_fox"] == -0.5:
                        state["move_fox"] = 0.5
                    if state["light_on_L"] and state["look_left"]:
                        print("-- you hear a slam at the left door, the see the fox walk away from the door --")
                    else:
                        print("-- You hear a slam at the left door, then footsteps heading away from the door --")
                else:
                    state["kill_fox"] += 1

        if state["dead_fox"]:
            print("\n====================================================")
            print("The fox ran and jumped onto you with its jaw open...")
            print("It started ripping you to shreds, killing you")
            print("Game over")
            print("====================================================\n")
            return False  # Death

        # Bear movement and attack logic
        if state["move_bear"] != 0:
            state["move_bear"] += 1
        if state["move_bear"] == 11:
            state["kill_bear"] = 1

        if state["kill_bear"] >= 1:
            if not state["door_close_R"]:
                if state["kill_bear"] == 3:
                    state["kill_bear"] = 0
                    state["dead_bear"] = True
                state["kill_bear"] += 1
            else:
                if state["kill_bear"] == 3:
                    print("You hear a series of knocks on the right door")
                state["kill_bear"] += 1

        if state["dead_bear"]:
            print("-- You feel like the bear is inside your office getting ready to attack --")
            state["dead_bear_force"] -= 1
        
        if state["dead_bear_force"] == 0:
            print("\n====================================================")
            print("The bear jumps out of the darkness in your office and grabs your head")
            print("the bear lean's to your head and bite into it, killing you")
            print("Game over")
            print("====================================================\n")
            return False

        # Player action input
        action = input("What do you do? (input action) ").lower().strip()

        if action == "left":
            print("-- You look at the left door and its buttons --")
            state["look_left"] = True
            state["look_right"] = False
        elif action == "right":
            print("-- You look at the right door and its buttons --")
            state["look_left"] = False
            state["look_right"] = True
        elif action == "light":
            if state["look_left"]:
                if state["light_on_L"]:
                    print("-- You turn the left light off --")
                    state["light_on_L"] = False
                else:
                    print("-- You turn the left light on --")
                    state["light_on_L"] = True
            elif state["look_right"]:
                if state["light_on_R"]:
                    print("-- You turn the right light off --")
                    state["light_on_R"] = False
                else:
                    print("-- You turn the right light on --")
                    state["light_on_R"] = True
            else:
                print("-- You are not looking at a light button --")
        elif action == "door":
            if state["look_left"]:
                if state["door_close_L"]:
                    print("-- You open the left door --")
                    state["door_close_L"] = False
                else:
                    if state["dead_bear"] or state["dead_rabbit"]:
                        print("-- The door button is not working --")
                    else:
                        print("-- You shut the left door --")
                        state["door_close_L"] = True
            elif state["look_right"]:
                if state["door_close_R"]:
                    print("-- You open the right door --")
                    state["door_close_R"] = False
                else:
                    if state["dead_bear"] or state["dead_rabbit"]:
                        print("-- The door button is not working --")
                    else:
                        print("-- You shut the right door --")
                        state["door_close_R"] = True
            else:
                print("-- You are not looking at a door --")
        elif action == "cams":
            state["look_left"] = False
            state["look_right"] = False
            state["cams_on"] = True
            print("-- You turn to your camera systems and turn it on --")

            # Camera mode loop
            while state["cams_on"]:
                state["time"] -= 1
                state["power"] -= 1

                if state["time"] == 60:
                    print("-- It's now 4am, The Fox is waking up --")
                elif state["time"] == 30:
                    print("-- It's now 5am, The Bear is moving --")
                    state["move_bear"] = 1
                elif state["time"] <= 0:
                    print("\n====================================================")
                    print("It's now 6am, you turn off the cameras because your shift has ended")
                    print("You win!")
                    print(f"Leftover power: {state['power']}/153")
                    print("====================================================\n")
                    state["cams_on"] = False
                    return True

                # Power drain from doors and lights
                if state["door_close_L"]:
                    state["power"] -= 1
                    print("-- You hear the grinding of the gears in the door to your left --")
                if state["door_close_R"]:
                    state["power"] -= 1
                    print("-- You hear the grinding of the gears in the door to your right --")
                if state["light_on_L"]:
                    state["power"] -= 1
                    print("-- You hear the buzzing of the lights to your left --")
                if state["light_on_R"]:
                    state["power"] -= 1
                    print("-- You hear the buzzing of the lights to your right --")

                if state["power"] <= 0:
                    print("-- The power ran out, forcing your cameras off --")
                    state["power_out"] = True
                    state["cams_on"] = False

                # Rabbit, bird, fox and bear logic repeated for cameras mode
                state["move_rabbit"]+= 0.4
                if state["move_rabbit"] in [6, 6.2]:
                    state["kill_rabbit"] = 1
                if state["kill_rabbit"] >= 1:
                    if not state["door_close_L"]:
                        if state["kill_rabbit"] == 5:
                            state["kill_rabbit"] = 0
                            state["dead_rabbit"] = True
                            state["kill_rabbit"] += 1
                    else:
                        if state["kill_rabbit"] == 5:
                            state["kill_rabbit"] = 0
                            state["move_rabbit_dec"] = state["move_rabbit"] - 0.4
                            state["move_rabbit"] = state["move_rabbit_dec"] - 1
                            if state["move_rabbit"] != 0:
                               state["move_rabbit"] *= -1
                            print("-- You hear a bang at the left door, then stomps heading away from the door --")
                else:
                    state["kill_rabbit"] += 1
                
                if state["dead_rabbit"]:
                    print("-- You feel like the rabbit is inside your office getting ready to attack --")
                    state["dead_rabbit_force"] -= 1
                
                if state["dead_rabbit_force"] == 0:
                    print("\n====================================================")
                    print("you get knocks over onto the floor while you where watching the cams")
                    print("when you turn to see what knocked you over you see the rabbit in the air")
                    print("it land on your back and starts jumping on you, squishing you to death")
                    print("Game over")
                    print("====================================================\n")
                    return False
                
                if state["move_fox"] != 0:
                    state["move_fox"] += 1
                if state["move_fox"] in [7, 7.5]:
                    state["kill_fox"] = 1

                if state["kill_fox"] >= 1:
                    if not state["door_close_L"]:
                        if state["kill_fox"] == 5:
                            state["kill_fox"] = 0
                            state["dead_fox"] = True
                        state["kill_fox"] += 1
                    else:
                        if state["kill_fox"] == 5:
                            state["fox_warning"] = False
                            state["kill_fox"] = 0
                            state["move_fox_dec"] = state["move_fox"] - 0.5
                            state["move_fox"] = state["move_fox_dec"] - 1
                            if state["move_fox"] == -0.5:
                                state["move_fox"] = 0.5
                            print("-- You hear a slam at the left door, then footsteps heading away from the door --")
                        else:
                            state["kill_fox"] += 1

                if state["dead_fox"]:
                    print("\n====================================================")
                    print("While on the cameras the fox ran into you and slammed you into the camera screen...")
                    print("The shards from the screen cause you to bleed to death")
                    print("Game over")
                    print("====================================================\n")
                    return False

                if state["move_bear"] != 0:
                    state["move_bear"] += 1
                if state["move_bear"] == 11:
                    state["kill_bear"] = 1

                if state["kill_bear"] >= 1:
                    if not state["door_close_R"]:
                        if state["kill_bear"] == 3:
                            state["kill_bear"] = 0
                            state["dead_bear"] = True
                        state["kill_bear"] += 1
                    else:
                        if state["kill_bear"] == 3:
                            print("-- You hear a series of knocks on the right door --")
                        state["kill_bear"] += 1

                if state["dead_bear"]:
                    print("-- You feel like the bear is inside your office planing to attack --")
                    state["dead_bear_force"] -= 1
                
                if state["dead_bear_force"] == 0:
                   print("\n====================================================")
                   print("wille you watch your cameras you feel two hands grabing your head")
                   print("the hands force you to turn toward themself, revaling the bear")
                   print("the bear lean's to your head and bite into it, killing you")
                   print("Game over")
                   print("====================================================\n")
                   return False

                if state["cams"] == 1:
                    print("-- the main stage, the farthest part of this place --")
                    if state["move_rabbit"] <=1:
                        print("-- the rabbit is playing on a prop guitar --")
                    if state["move_bear"] == 0:
                        print("-- you see the bear in the middle of the stage, inactive --")
                    if state["move_bear"] == 1 or state["move_bear"] == 2:
                        print("-- you see the bear in the middle of the stage, eyes staring at the cameras --")
                        state["move_bear"] -=1
                if state["cams"] == 2:
                    print("-- the main siting area, the top middle of the map --")
                    if state["move_rabbit"] <=2 and state["move_rabbit"] >1:
                        print("-- the rabbit is by a table messing with some party hats --")
                    if state["move_bear"] == 3 or state["move_bear"] == 4:
                        print("-- you see the bear's eyes hiding in the shadows, staring at the cameras --")
                        state["move_bear"]-=1
                if state["cams"] == 3:
                    print("-- the kids area, the top left of the map ---")
                    if state["move_rabbit"] <=3 and state["move_rabbit"] >2:
                        print("-- the rabbit is in the ballpit, trying to entertain themself --")
                    if state["move_fox"] == 0:
                        print("-- the mini stage curtains are fully closed --")
                    if state["move_fox"] <= 2 and not state["move_fox"] == 0:
                        print("-- you see an eye peeking out from the curtains of the mini stage --")
                        state["move_fox"]-=0.5
                    if state["move_fox"] > 2 and state["move_fox"] <= 4:
                        print("-- you see the fox's head poping out of the curtain of the mini stage --")
                        state["move_fox"]-=0.5
                    if state["move_fox"] > 4 and state["move_fox"] <= 6:
                        print("-- you see the fox steping out of the slightly open curtain of the mini stage --")
                        state["move_fox"]-=0.5
                    if state["move_fox"] >= 7:
                        print("-- you see the open curtain of the mini stage, no fox in sight --")
                if state["cams"] == 4:
                    print("-- the kitchen, the top right of the map --")
                    if state["move_bear"] == 5 or state["move_bear"] == 6:
                        print("-- you see the bear at the edge of the cameras, head turned to the camera --")
                        state["move_bear"]-=1
                if state["cams"] == 5:
                    print("-- the hallway of fame, the middle left of the map --")
                    if state["move_rabbit"] <=4 and state["move_rabbit"] >3:
                        print("-- the rabbit is trying to skip across the hallway --")
                if state["cams"] == 6:
                    print("-- the storage room, the middle right of the map --")
                    if state["move_bear"] == 7 or state["move_bear"] == 8:
                        print("-- you see the bear hiding behind a shelf, only the eyes are visable --")
                        state["move_bear"]-=1
                if state["cams"] == 7:
                    print("-- the reception area, close to your left door --")
                    if state["move_rabbit"] <=5 and state["move_rabbit"] >4:
                        print("the rabbit is messing with the bell on the reception deck")
                    if state["kill_fox"] >= 1 and not state["fox_warning"]:
                        print("-- the fox is dashing and sliding to your office --")
                        state["kill_fox"] = 2
                        state["fox_warning"] = True
                        state["move_fox"] -= 0.5
                if state["cams"] == 8:
                    print("-- the staff room, close to your right door --")
                    if state["move_bear"] == 9 or state["move_bear"] == 10:
                        print("-- you see the bear by the door leading to your office, looking at where you stand --")
                        state["move_bear"]-=1

                cam_action = input("Camera mode - enter cam number (1-8) or 'exit' to leave cameras: ").lower().strip()
                if cam_action == "exit":
                    state["cams_on"] = False
                    if state["dead_rabbit"]:
                        print("\n====================================================")
                        print("as you turn off the camera you see the rabbit behind you on the screen reflexion")
                        print("it pushs you onto the floor and jumps into the air")
                        print("it then land on your back and starts jumping on you, squishing you to death")
                        print("Game over")
                        print("====================================================\n")
                        return False
                    if state["dead_bear"]:
                        print("\n====================================================")
                        print("as you turn off your cameras you feel two hands grabing your head")
                        print("the hands force you to turn toward themself, revaling the bear")
                        print("the bear lean's to your head and bite into it, killing you")
                        print("Game over")
                        print("====================================================\n")
                        return False
                    print("-- You turn off the cameras --")
                elif cam_action in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    state["cams"] = int(cam_action)
                    print(f"you switch to cameras {state['cams']}")
                else:
                    print("Invalid camera input")
        elif action == "wait":
            print("-- You wait as time passes --")
        else:
            print("-- Invalid input, you wait as time passes --")

        #Power out stage
        while state["power_out"]:
            print("-- the room was dark with all the doors open --")
            state["time"]-=1
            if state["time"]== 60:
                print("-- it's now 4am, but you feel like its to late --")
            if state["time"]==30:
                print("-- it's now 5am, but you feel like it's to late --")
            if state["time"]==0:
                print("\n====================================================")
                print("it's now 6am, your shift has ended, just in time")
                print("you win")
                print(f"Leftover power: {state['power']}/153")
                print("====================================================\n")
                return True
            print("-- you see two glowing eyes by you door --")
            state["time"]-=1
            if state["time"]== 60:
                print("-- it's now 4am, but you feel like its to late --")
            if state["time"]==30:
                print("-- it's now 5am, but you feel like it's to late --")
            if state["time"]==0:
                print("\n====================================================")
                print("it's now 6am, your shift has ended, just in time")
                print("you win")
                print(f"Leftover power: {state['power']}/153")
                print("====================================================\n")
                return True
            print("-- your hear some music coming from the eye --")
            state["time"]-=1
            if state["time"]== 60:
                print("-- it's now 4am, but you feel like its to late --")
            if state["time"]==30:
                print("-- it's now 5am, but you feel like it's to late --")
            if state["time"]==0:
                print("it's now 6am, your shift has ended, just in time")
                print("you win")
                print(f"Leftover power: {state['power']}/153")
                return True
            print("-- the eyes are now infornt of you --")
            state["time"]-=1
            if state["time"]== 60:
                print("-- it's now 4am, but you feel like its to late --")
            if state["time"]==30:
                print("-- it's now 5am, but you feel like it's to late --")
            if state["time"]==0:
                print("\n====================================================")
                print("it's now 6am, your shift has ended, just in time")
                print("you win")
                print(f"Leftover power: {state['power']}/153")
                print("====================================================\n")
                return True
            print("-- the eyes are now gone --")
            state["time"]-=1
            if state["time"]== 60:
                print("-- it's now 4am, but you feel like its to late --")
            if state["time"]==30:
                print("-- it's now 5am, but you feel like it's to late --")
            if state["time"]==0:
                print("\n====================================================")
                print("it's now 6am, your shift has ended, just in time")
                print("you win")
                print(f"Leftover power: {state['power']}/153")
                print("====================================================\n")
                return True
            print("\n====================================================")
            print("a hand grabs your head, you look up and see the eyes had returned, they slam you onto the floor")
            print("the force of the slam has killed you")
            print("Game over")
            print("====================================================\n")
            return False
            
def main():
    while True:
        print("An Half Night In Python")
        action = input("Enter mode ('info' 'play' 'quit'): ").lower().strip()
        if action == "quit":
            print("Good bye")
            break
        elif action == "info":
            print_info()
        elif action == "play":
            survived = play_game()
            if not survived:
                print("Restarting game...")
            # After game ends (win or death), loop back to start menu
        else:
            print("Please type in one of the inputs")

if __name__ == "__main__":
    main()
