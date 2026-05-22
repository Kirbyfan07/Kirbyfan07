import random

def initialize_game():
    state = {
        "time": 91,
        "power": 153,
        "cams": 1,
        # Enemy position trackers (1-8 map to camera numbers)
        # Office entry points: Rabbit/Fox approach Left (7). Bird/Bear approach Right (8).
        "rabbit_pos": 1,   
        "bird_pos": 1,     
        "bear_pos": 1,     
        "move_fox": 0,       # Fox progress stages: 0=Cove, 1-2=Peeking, 3-4=Ready, 5=Running, 6=At door
        "kill_fox": 0,
        "move_fox_dec": 0,
        "fox_warning": False,
        "dead_fox": False,
        "move_bear": 0,
        "kill_bear": 0,
        "dead_bear": False,
        "look_left": False,
        "look_right": False,
        "light_on_L": False,
        "light_on_R": False,
        "door_close_L": False,
        "door_close_R": False,
        "cams_on": False,
        "power_out": False,
        "bear": 0,
    }
    return state

def print_info():
    print("\n====================================================")
    print("           FIVE NIGHTS AT TEXT-BASE                  ")
    print("====================================================")
    print("You need to survive from 3am to 6am")
    print("Time moves per input action")
    print("A new threat gets added every hour")
    print("\nTo survive you need to do the following:")
    print("1. Check doors and cams for threats")
    print("2. If threats are at the doors, close them")
    print("3. The fox will grow in anger when not watched, close the door he rushes to")
    print("4. The bear hates the light in the cams and will stop if looked at, but always heads to you")
    print("5. The rabbit and the bird stick to one side, but are fast")
    print("Every action costs power, don't run out")
    print("\nInputs are the following:")
    print("1. 'wait' lets time move without moving")
    print("2. 'left' go to left door")
    print("3. 'right' go to right door")
    print("4. 'light' turn lights on/off (costs 1 power per turn while on)")
    print("5. 'door' open/close door (costs 1 power per turn while shut)")
    print("6. 'cams' open camera monitor. While in cams, inputs are:")
    print("   '1' to '8' to swap camera channels")
    print("   'exit' to close monitor and return to office")
    print("====================================================\n")

def display_camera_content(state):
    current_cam = state["cams"]
    
    # Base room descriptions
    descriptions = {
        1: "Show Stage: Dark and empty silhouettes stand against the wall.",
        2: "Dining Hall: Rows of empty party tables fade into shadows.",
        3: "Pirate Cove: A purple curtain draped with silver stars.",
        4: "East Hallway: A narrow corridor filled with old party posters.",
        5: "Supply Closet: Shelves stacked with mops, brooms, and cleaning fluids.",
        6: "Kitchen: Camera feed is completely dead, but you can hear audio.",
        7: "West Hall Corner: Just outside your Left Door window.",
        8: "East Hall Corner: Just outside your Right Door window."
    }
    
    print(f"\n[FEED: CAM {current_cam}] - {descriptions[current_cam]}")
    
    # Special audio-only camera overrides
    if current_cam == 6:
        if state["bird_pos"] == 6:
            print(">>> Loud clanging sounds of pots and pans echo from the speaker.")
        else:
            print(">>> Soft, ambient mechanical humming.")
        return

    # Check and print normal enemy locations
    enemies_found = False
    if state["rabbit_pos"] == current_cam:
        print("[-] A tall, blue rabbit silhouette is staring directly into the camera lens.")
        enemies_found = True
    if state["bird_pos"] == current_cam:
        print("[-] A yellow bird is perched awkwardly, its mouth wide open.")
        enemies_found = True
    if state["bear_pos"] == current_cam:
        print("[-] A heavy, large bear shape is lurking silently in the back corner.")
        enemies_found = True
        
    # Pirate cove unique descriptions for the Fox
    if current_cam == 3:
        enemies_found = True
        if state["move_fox"] < 2:
            print("[-] The curtains are tightly closed.")
        elif state["move_fox"] < 4:
            print("[-] The Fox is peeking its head out through the curtain gap.")
        elif state["move_fox"] < 5:
            print("[-] The Fox is stepping out, crouched and ready to run.")
        else:
            print("[-] The curtains are wide open. The Fox is missing!")

    if not enemies_found:
        print("[-] No movement detected.")

def update_enemy_positions(state):
    """Handles basic room shifts for Rabbit and Bird based on current game time"""
    # Simple movement simulation tied to the clock countdown
    if state["time"] == 75:  # Rabbit moves first
        state["rabbit_pos"] = 2
        print("\n*You hear heavy footsteps shuffling in the building*")
    elif state["time"] == 50: # Bird wakes up, Rabbit advances
        state["bird_pos"] = 4
        state["rabbit_pos"] = 5
    elif state["time"] == 35: # Shifting closer to doors
        state["rabbit_pos"] = 7
        state["bird_pos"] = 6
    elif state["time"] == 20: # Bird reaches door threat area
        state["bird_pos"] = 8

def play_game():
    state = initialize_game()
    print_info()
    print("Good luck! Your shift begins now.")

    while True:
        # Step game time forward
        state["time"] -= 1

        # Check hour notifications
        if state["time"] == 90:
            print("\n--- 3:00 AM ---")
        elif state["time"] == 60:
            print("\n--- 4:00 AM - The Fox is waking up ---")
            state["move_fox"] = 1
        elif state["time"] == 30:
            print("\n--- 5:00 AM - The Bear begins moving ---")
            state["move_bear"] = 1
            state["bear"] = 1
        elif state["time"] <= 0:
            print("\n====================================================")
            print("6:00 AM - The morning bell rings!")
            print("You survived the night!")
            print(f"Remaining Power: {state['power']}/153")
            print("====================================================")
            return True  # Win

        # Background movement engine
        update_enemy_positions(state)

        # Ambient power drain calculations
        if state["door_close_L"]:
            state["power"] -= 1
            print("[POWER] Left door hydraulic hum is active.")
        if state["door_close_R"]:
            state["power"] -= 1
            print("[POWER] Right door hydraulic hum is active.")
        if state["light_on_L"]:
            state["power"] -= 1
            print("[POWER] Left hallway light is burning.")
        if state["light_on_R"]:
            state["power"] -= 1
            print("[POWER] Right hallway light is burning.")

        # Immediate check for office layout power loss
        if state["power"] <= 0:
            print("\n[!!!] The power cut out completely. Everything goes pitch black...")
            print("Game over.")
            return False

        # --- Door jump scare check triggers ---
        if state["rabbit_pos"] == 7 and state["light_on_L"] and not state["door_close_L"]:
            print("\n[WARNING] A shadow is standing right at your left window!")
        if state["bird_pos"] == 8 and state["light_on_R"] and not state["door_close_R"]:
            print("\n[WARNING] A shadow is peering through your right window!")

        # Fox attack engine
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
                    print("\n[BANG!] You hear a violent crash against the Left Door, followed by fading footsteps.")
                    state["move_fox"] = 1 # Reset fox back to stage
                else:
                    state["kill_fox"] += 1

        if state["dead_fox"]:
            print("\nThe Fox bursts through your open left doorway, screeching wildly!")
            print("Game over.")
            return False

        # Bear attack engine
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
                    print("\nYou hear deep, heavy knocks pounding against the Right Door.")
                state["kill_bear"] += 1

        if state["dead_bear"]:
            print("\nA phantom laugh echoes inside the office. The Bear materialises behind you.")
            print("Game over.")
            return False

        # Get Office input command
        print(f"\n[Status: Power {state['power']}% | Cam Memory: Cam {state['cams']}]")
        action = input("Command? (wait/left/right/light/door/cams): ").lower().strip()

        if action == "left":
            print("Swiveled your chair to look towards the Left Door.")
            state["look_left"] = True
            state["look_right"] = False
        elif action == "right":
            print("Swiveled your chair to look towards the Right Door.")
            state["look_left"] = False
            state["look_right"] = True
        elif action == "light":
            if state["look_left"]:
                state["light_on_L"] = not state["light_on_L"]
                print(f"Left light toggled {'ON' if state['light_on_L'] else 'OFF'}.")
            elif state["look_right"]:
                state["light_on_R"] = not state["light_on_R"]
                print(f"Right light toggled {'ON' if state['light_on_R'] else 'OFF'}.")
            else:
                print("You need to turn and look 'left' or 'right' before using the light switches.")
        elif action == "door":
            if state["look_left"]:
                if state["dead_bear"]:
                    print("The security mechanisms are jammed!")
                else:
                    state["door_close_L"] = not state["door_close_L"]
                    print(f"Left security door toggled {'CLOSED' if state['door_close_L'] else 'OPEN'}.")
            elif state["look_right"]:
                if state["dead_bear"]:
                    print("The security mechanisms are jammed!")
                else:
                    state["door_close_R"] = not state["door_close_R"]
                    print(f"Right security door toggled {'CLOSED' if state['door_close_R'] else 'OPEN'}.")
            else:
                print("You need to turn and look 'left' or 'right' before using the door switches.")
        elif action == "wait":
            print("You sit completely still and keep an eye on your desk.")
        
        # --- THE WORKING CAMERA SUB-MENU LOOP ---
        elif action == "cams":
            state["look_left"] = False
            state["look_right"] = False
            state["cams_on"] = True
            
            print("\n>>> Lifting Up Security Monitor Screen")
            
            while state["cams_on"]:
                # Display current camera status
                display_camera_content(state)
                
                # Check monitor battery drain inside loop
                state["power"] -= 1
                print(f"[Monitor Power: {state['power']}%]")
                
                if state["power"] <= 0:
                    print("\n[!!!] The monitors instantly black out. Zero Power remaining.")
                    state["cams_on"] = False
                    break
                
                # Prompt user inside sub-loop
                cam_input = input("Monitor Command? (Enter 1-8 to swap channel, 'exit' to close screen): ").strip().lower()
                
                if cam_input in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    state["cams"] = int(cam_input)
                    # If looking at Bear on camera, stunt/slow his movement countdown stage
                    if state["bear"] == 1 and state["bear_pos"] == state["cams"]:
                        state["move_bear"] = max(1, state["move_bear"] - 1)
                        print("-> The Bear freezes in place under the bright camera lens flare.")
                elif cam_input == "exit":
                    state["cams_on"] = False
                    print(">>> Putting down Security Monitor Screen.")
                else:
                    print("Error: Unknown monitor frequency channel.")

# Run the complete game program
if __name__ == "__main__":
    play_game()