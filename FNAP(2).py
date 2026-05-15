
start=True
time = 91
power = 153
cams = 1
rabbit = 0
bear = 0
fox = 0
bird = 0
light_on_L = False
light_on_R = False
door_close_L = False
door_close_R = False
cams_on= False
power_out=False

while start==True:
    print("One Night At Python's")
    action=input("enter mode ('info' 'play') ").lower().strip()
    if action=="info":
        print("you need to survive from 3am to 6am")
        print("time moves per input")
        print("to survive you need to do the folowing,")
        print("1. check doors and cams for threats")
        print("2. if threats are at the doors, close them")
        print("3. the fox will grow in anger when not watched, close the door he rush too")
        print("4. the bear hates the light in the cams and will stop if looked at, but allway heads to you")
        print("5. the rabbit and the bird stick to one side, but are fast")
        print("ever action cost power, don't run out")
        print("inputs are the folowing")
        print("1. 'wait' lets time move without moving")
        print("2. 'left' go to left door")
        print("3. 'right' go to right door")
        print("4. 'light' turn lights on or off to see if threats are at door, cost 1 point of power per input when on")
        print("5. 'door' open/chose door to block threats, cost 1 point of power per input when on")
        print("both 'door' and 'light' will work at both sides")
        print("6. 'cams' open/chose cameras to check on threats, cost 1 point per input when on, in cams, input are")
        print("'1' top of map, where they start and return to")
        print("'2' top middle of map, where the map spilts")
        print("'3' top left of map, where the fox lives")
        print("'4' top right of map")
        print("'5' middle left of map")
        print("'6' middle right of map")
        print("'7' bottom left of map, next to your door")
        print("'8' bottom right of map, next to your door")
        print("the cameras remember which cam it was last on")
    elif action=="play":
        start=False
        print("good luck")
        alive=True
    else:
        print("plese type in one of the inputs")

while alive==True:
    time=time-1
    if time== 90:
        print("it's 3am, the start of your shift")
    if time== 60:
        print("it's now 4am")
    if time==30:
        print("it's now 5am")
    if time==0:
        print("it's now 6am, your shift has ended")
        print("you win")
        alive=False
        break
    if power<0 or power==0:
        print("power run out")
        power_out=True
    if door_close_L==True:
        power=power-1
        print("you hear the grinding of the gears in the door to your left")
    if door_close_R==True:
        power=power-1
        print("you hear the grinding of the gears in the door to your right")
    if light_on_L==True:
        power=power-1
        print("you hear the buzzing of the lights to your left")
    if light_on_R==True:
        power=power-1
        print("you hear the buzzing of the lights to your right")
    action=input("what do you do? (input action) ").lower().strip()
    if action =="left":
        print("you look at the left door and it's buttons")
        look_left=True
        look_right=False
    elif action =="right":
        print("you look at the right door and it's buttons")
        look_left=False
        look_right=True
    elif action == "light":
        if look_left == True:
            if light_on_L == True:
                print("You turn the left light off")
                light_on_L = False
            else:
                print("you turn the left light on")
                light_on_L = True
        elif look_right == True:
            if light_on_R == True:
                print("You turn the right light off")
                light_on_R = False
            else:
                print("you turn the right light on")
                light_on_R = True
        else:
            print ("your are not looking at a light button")
    elif action == "door":
        if look_left == True:
            if door_close_L == True:
                print("You open the left door")
                door_close_L = False
            else:
                print("you shut the left door")
                door_close_L = True
        elif look_right == True:
            if door_close_R == True:
                print("You open the right door")
                door_close_R = False
            else:
                print("you shut the right door")
                door_close_R = True
        else:
            print ("your are not looking at a door")
    elif action == "cams":
        look_left=False
        look_right=False
        cams_on=True
        print("you turn to your cameras systems")
    else:
        print("you wait as time pass")
    
    while cams_on == True:
        time=time-1
        power=power-1
        if power<0 or power==0:
            print("power run out, forcing you cameras off")
            power_out=True
            cams_on=False
            break
        if time== 60:
            print("it's now 4am")
        if time==30:
            print("it's now 5am")
        if time==0:
            print("it's now 6am, your shift has ended")
            print("you win")
            alive=False
            break
        if door_close_L==True:
            power=power-1
            print("you hear the grinding of the gears in the door to your left")
        if door_close_R==True:
            power=power-1
            print("you hear the grinding of the gears in the door to your right")
        if light_on_L==True:
            power=power-1
            print("you hear the buzzing of the lights to your left")
        if light_on_R==True:
            power=power-1
            print("you hear the buzzing of the lights to your right")
        if cams == 1:
            print("the main stage, the farthest part of this place")
        if cams == 2:
            print("the main siting area, the top meddle of the map")
        if cams == 3:
            print("the kids area, the top left of the map")
        if cams == 4:
            print("the kitchen, the top right of the map")
        if cams == 5:
            print("the hallway, the meddle left of the map")
        if cams == 6:
            print("the storage room, the meddle right of the map")
        if cams == 7:
            print("the reception area, close to your left door")
        if cams == 8:
            print("the staff room, close to your right door")
        action=input("what do you do? (input action) ").lower().strip()
        if action == "1":
            if cams == 1:
                print("your already on that camera")
            else:
                cams == 1
                print("you change to camera 1")
        elif action == "2":
            if cams == 2:
                print("your already on that camera")
            else:
                cams == 2
                print("you change to camera 2")
        elif action == "3":
            if cams == 3:
                print("your already on that camera")
            else:
                cams == 3
                print("you change to camera 3")
        elif action == "4":
            if cams == 4:
                print("your already on that camera")
            else:
                cams == 4
                print("you change to camera 4")
        elif action == "5":
            if cams == 5:
                print("your already on that camera")
            else:
                cams == 5
                print("you change to camera 5")
        elif action == "6":
            if cams == 6:
                print("your already on that camera")
            else:
                cams == 6
                print("you change to camera 6")
        elif action == "7":
            if cams == 7:
                print("your already on that camera")
            else:
                cams == 7
                print("you change to camera 7")
        elif action == "8":
            if cams == 8:
                print("your already on that camera")
            else:
                cams == 8
                print("you change to camera 8")
        elif action == "cams":
            print("you turn off the camera systems")
            cams_on=False
        else:
           print("you stay on the same camera your on")
