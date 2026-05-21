start= True
 
while start==True:
    time = 91
    power = 153
    cams = 1
    move_rabbit = 1
    move_bird = 1
    move_fox = 0
    kill_fox = 0
    move_fox_dec = 0
    dead_fox = False
    move_bear = 0
    kill_bear = 0
    dead_bear = False
    look_left =False
    look_right = False
    light_on_L = False
    light_on_R = False
    door_close_L = False
    door_close_R = False
    cams_on = False
    power_out = False
    print("One Night At Python's")
    action=input("enter mode ('info' 'play' 'quit') ").lower().strip()
    if action=="quit":
        print("good bye")
        break
    if action=="info":
        print("you need to survive from 3am to 6am")
        print("time moves per input")
        print("a new threat gets add every hour")
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
        move_fox=1
    if time==30:
        print("it's now 5am")
        move_bear=1
    if time==0:
        print("it's now 6am, your shift has ended")
        print("you win")
        print("leftover power: " + power + "/153")
        start=True
        alive=False
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
        if look_right==True:
            if move_bear >= 11 and kill_bear == False :
                print("you see the bear standing at the door, it looks looks like it not going to leave")
            if move_bear < 11 or kill_bear == True:
                print("there nothing there")
    if power<0 or power==0:
        print("the power run out")
        power_out=True
    if not move_fox == 0:
        move_fox=move_fox+1
    if move_fox == 7 or move_fox==7.5:
            kill_fox=1
    if kill_fox >= 1:
        if door_close_L == False:
            if kill_fox == 5:
                kill_fox=0
                dead_fox=True
            kill_fox = kill_fox+1
        else:
            if kill_fox == 5:
                kill_fox=0
                move_fox_dec=move_fox-0.5
                move_fox=move_fox_dec-1
                if move_fox==-0.5:
                    move_fox=0.5
                print("you hear a slam at the right door, then a footstep heading away from the door")
            else:
                kill_fox= kill_fox + 1
    if dead_fox==True:
        print("the fox ran and jumped onto your with it's jaw open...")
        print("it started to ripping you to shreds, killing you")
        start=True
        alive=False
    if not move_bear == 0:
        move_bear=move_bear+1
    if move_bear == 11:
        kill_bear = 1
        if kill_bear >= 1:
            if door_close_R == False:
                if kill_bear == 3:
                    kill_bear=0
                    dead_bear=True
                kill_bear = kill_bear+1
            else:
                if kill_bear == 3:
                    kill_bear=1
                    print("you hear a series of knock on the right door")
                else:
                    kill_bear = kill_bear+1
    if dead_bear == True:
        print("you feel like the bear is inside your office")
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
                if bear >= 11 and kill_bear == False :
                    print("you see the bear standing at the door, it looks looks like it not going to leave")
        else:
            print ("your are not looking at a light button")
    elif action == "door":
        if look_left == True:
            if door_close_L == True:
                print("You open the left door")
                door_close_L = False
            else:
                if dead_bear ==True:
                    print("the door button is not working")
                else:
                    print("you shut the left door")
                    door_close_L = True
        elif look_right == True:
            if door_close_R == True:
                print("You open the right door")
                door_close_R = False
            else:
                if dead_bear ==True:
                    print("the door button is not working")
                else:
                    print("you shut the right door")
                    door_close_R = True
        else:
            print ("your are not looking at a door")
    elif action == "cams":
        look_left=False
        look_right=False
        cams_on=True
        print("you turn to your cameras systems and turn it on")
    else:
        print("you wait as time pass")
    
    while cams_on == True:
        time=time-1
        power=power-1
        if time== 60:
            print("it's now 4am")
        if time==30:
            print("it's now 5am")
            bear = 1
        if time==0:
            print("it's now 6am, you turn off the cameras, because your shift has ended")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        if not move_fox == 0:
            move_fox=move_fox+1
        if not move_bear == 0:
            move_bear=move_bear+1
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
        if power<0 or power==0:
            print("the power run out, forcing you cameras off")
            power_out=True
            cams_on=False
            break
        if move_fox == 7 or move_fox==7.5:
            kill_fox=1
        if kill_fox >= 1:
            if door_close_L == False:
                if kill_fox == 5:
                    kill_fox=0
                    dead_fox=True
                kill_fox = kill_fox+1
            else:
                if kill_fox == 5:
                    kill_fox=0
                    move_fox_dec=move_fox-0.5
                    move_fox=move_fox_dec-1
                    if move_fox==-0.5:
                        move_fox=0.5
                    print("you hear a slam at the right door, then a footstep heading away from the door")
                else:
                    kill_fox= kill_fox + 1
        if dead_fox==True:
            print("will on the cameras the fox ran into you and slamed you into the cameras screen...")
            print("the shards form the screen cause you to bleed to death")
            start=True
            alive=False
        if move_bear == 11:
            kill_bear = 1
        if kill_bear >= 1:
            if door_close_R == False:
                if kill_bear == 3:
                    kill_bear=0
                    dead_bear=True
                kill_bear = kill_bear+1
            else:
                if kill_bear == 3:
                    kill_bear=1
                    print("you hear a series of knock on the right door")
                else:
                    kill_bear = kill_bear+1
        if dead_bear == True:
            print("you feel like the bear is inside your office")
        if cams == 1:
            print("the main stage, the farthest part of this place")
            if move_bear == 0:
                print("you see the bear in the middle of the stage, inactive")
            if move_bear == 1 or move_bear == 2:
                print("you see the bear in the middle of the stage, eyes staring at the cameras")
                move_bear=move_bear-1
        if cams == 2:
            print("the main siting area, the top middle of the map")
            if move_bear == 3 or move_bear == 4:
                print("you see the bear's eyes hiding in the shadows, staring at the cameras")
                move_bear=move_bear-1
        if cams == 3:
            print("the kids area, the top left of the map")
            if move_fox <= 2 and not move_fox == 0:
                print("you see an eye peeking out from the curtains of the mini stage")
                move_fox=move_fox-0.5
            if move_fox > 2 and move_fox <= 4:
                print("you see the fox's head poping out of the curtain of the mini stage")
                move_fox=move_fox-0.5
            if move_fox > 4 and move_fox <= 6:
                print("you see the fox steping out of the slightly open curtain of the mini stage")
                move_fox=move_fox-0.5
            if move_fox >= 7:
                print("you see the open curtain of the mini stage, no fox in sight")
                move_fox=move_fox-0.5
        if cams == 4:
            print("the kitchen, the top right of the map")
            if move_bear == 5 or move_bear == 6:
                print("you see the bear at the edge of the cameras, head turned to the camera")
                move_bear=move_bear-1
        if cams == 5:
            print("the hallway, the middle left of the map")
        if cams == 6:
            print("the storage room, the middle right of the map")
            if move_bear == 7 or move_bear == 8:
                print("you see the bear hiding behind a shelf, only the eyes are visable")
                move_bear=move_bear-1
        if cams == 7:
            print("the reception area, close to your left door")
        if cams == 8:
            print("the staff room, close to your right door")
            if move_bear == 9 or move_bear == 10:
                print("you see the bear by the door leading to your office, looking at where you stand")
                move_bear-1
        if move_bear == 11:
            kill_bear = 1
        action=input("what do you do? (input action) ").lower().strip()
        if action == "1":
            if cams == 1:
                print("your already on that camera")
            else:
                cams = 1
                print("you change to camera 1")
        elif action == "2":
            if cams == 2:
                print("your already on that camera")
            else:
                cams = 2
                print("you change to camera 2")
        elif action == "3":
            if cams == 3:
                print("your already on that camera")
            else:
                cams = 3
                print("you change to camera 3")
        elif action == "4":
            if cams == 4:
                print("your already on that camera")
            else:
                cams = 4
                print("you change to camera 4")
        elif action == "5":
            if cams == 5:
                print("your already on that camera")
            else:
                cams = 5
                print("you change to camera 5")
        elif action == "6":
            if cams == 6:
                print("your already on that camera")
            else:
                cams = 6
                print("you change to camera 6")
        elif action == "7":
            if cams == 7:
                print("your already on that camera")
            else:
                cams = 7
                print("you change to camera 7")
        elif action == "8":
            if cams == 8:
                print("your already on that camera")
            else:
                cams = 8
                print("you change to camera 8")
        elif action == "cams":
            print("you turn off the camera systems")
            cams_on=False
            if dead_bear == True:
                print("then suddenly, you are grabed by the bear, it lifted you to it's mouth and bite your head")
                print("your have been killed")
                start=True
                alive=False
        else:
           print("you stay on the same camera your on")
   
    while power_out == True:
        print("the room was dark with all the doors open")
        time=time-1
        if time== 60:
            print("it's now 4am, but you feel like its to late")
        if time==30:
            print("it's now 5am, but you feel like it's to late")
        if time==0:
            print("it's now 6am, your shift has ended, just in time")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        print("you see two glowing eyes by you door")
        time=time-1
        if time== 60:
            print("it's now 4am, but you feel like its to late")
        if time==30:
            print("it's now 5am, but you feel like it's to late")
        if time==0:
            print("it's now 6am, your shift has ended, just in time")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        print("your hear some music coming from the eye")
        time=time-1
        if time== 60:
            print("it's now 4am, but you feel like its to late")
        if time==30:
            print("it's now 5am, but you feel like it's to late")
        if time==0:
            print("it's now 6am, your shift has ended, just in time")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        print("the eyes are now infornt of you")
        time=time-1
        if time== 60:
            print("it's now 4am, but you feel like its to late")
        if time==30:
            print("it's now 5am, but you feel like it's to late")
        if time==0:
            print("it's now 6am, your shift has ended, just in time")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        print("the eyes are now gone")
        time=time-1
        if time== 60:
            print("it's now 4am, but you feel like its to late")
        if time==30:
            print("it's now 5am, but you feel like it's to late")
        if time==0:
            print("it's now 6am, your shift has ended, just in time")
            print("you win")
            print("leftover power: " + power + "/153")
            start=True
            alive=False
            break
        print("a hand grabs your head, you look up and see the eyes had returned, they slam you onto the floor")
        print("the force of the slam has killed you")
        start=True
        alive=False
