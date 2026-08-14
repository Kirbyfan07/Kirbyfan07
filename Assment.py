#pre start vaules
score_e = 0
score_h = 0
quiz_mode = 0
Question_number = 0
#make the game run
start = True
#looping start menu
while start == True:
    #reset temp_score of scores to be accurate
    temp_score = 0
    print("Wellcome to the Pokemon type quiz")
    #means to pick mode
    quiz_chose = input("imput mode you want 'easy' 'hard' 'score' 'quit'").lower().strip()
    #start easy mode
    if quiz_chose == "easy":
        quiz_mode = 1
        print("Starting quiz (Easy)")
    #start hard mode
    elif quiz_chose == "hard":
        quiz_mode = 2
        print("Starting quiz (hard)")
    #see the last saved score pre quiz
    elif quiz_chose == "score":
        print("Last saved score for easy is ",score_e," out of 8")
        print("Last saved score for hard is ",score_h," out of 8")
    #kill progain
    elif quiz_chose == "quit":
        print("Bye")
        start = False
    #failsafe
    else:
        print("INVALID, sorry, but can you type in a input")
    #easy quiz
    while quiz_mode == 1:
        print("Question 1/8")
        Question_number = 1
        while Question_number == 1:
            Question = input ("BUG types are resisted by ROCK types? 'True' or 'False'").lower().strip()
            if Question == "false":
                print("Correct")
                print("BUG types are neutral to ROCK types")
                Question_number = 2
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 2
                print("BUG types are neutral to ROCK types")
            else:
                print("INVALID, try again")
        while Question_number == 2:
            print("Question 2/8")
            Question = input ("WATER types are resisted by WATER types").lower().strip()
            if Question == "true":
                print("Correct")
                print("WATER Types are resisted by WATER types")
                Question_number = 3
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 3
                print("WATER Types are resisted by WATER types")
            else:
                print("INVALID, try again")
        while Question_number == 3:
            print("Question 3/8")
            Question = input ("BUG types are neutral to DRAGON types").lower().strip()
            if Question == "true":
                print("Correct")
                print("BUG types are neutral to DRAGON types")
                Question_number = 4
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 4
                print("BUG types are neutral to DRAGON types")
            else:
                print("INVALID, try again")
        while Question_number == 4:
            print("Question 4/8")
            Question = input ("GROUND types are ineffective to FIRE types").lower().strip()
            if Question == "false":
                print("Correct")
                print("GROUND types are supereffective to FIRE types")
                Question_number = 5
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 5
                print("GROUND types are supereffective to FIRE types")
            else:
                print("INVALID, try again")
        while Question_number == 5:
            print("Question 5/8")
            Question = input ("DARK types are resisted by DARK Types").lower().strip()
            if Question == "true":
                print("Correct")
                print("DARK types are resisted by DARK Types")
                Question_number = 6
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 6
                print("DARK types are resisted by DARK Types")
            else:
                print("INVALID, try again")
        while Question_number == 6:
            print("Question 6/8")
            Question = input ("PSYCHIC types resist POISON types").lower().Strip()
            if Question == "false":
                print("Correct")
                print("PSYCHIC types take neutral dammage from POISON")
                Question_number = 7
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 7
                print("PSYCHIC types take neutral dammage from POISON")
            else:
                print("INVALID, try again")
        while Question_number == 7:
            print("Question 7/8")
            Question = input ("FAIRY types are weak to BUG type").lower().strip()
            if Question == "false":
                print("Correct")
                print("FAIRY types resist BUG types")
                Question_number = 8
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 8
                print("FAIRY types resist BUG types")
            else:
                print("INVALID, try again")
        while Question_number == 8:
            print("Question 8/8")
            Question = input ("STEEL types are immune to POISON types").lower().strip()
            if Question == "true":
                print("Correct")
                print("STEEL types are immune to POISON types")
                Question_number = 9
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 9
                print("STEEL types are immune to POISON types")
            else:
                print("INVALID, try again")
        
        if Question_number == 9:
            #turn temp_score to the final score of the quiz
            score_e = temp_score
            print("Quiz complete! Your final score is: ",score_e,"out of 8")
            #end quiz
            quiz_mode=0
        
    #hard quiz
    while quiz_mode == 2:
        print("Question 1/8")
        Question_number = 1
        while Question_number == 1:
            Question = input ("ELECTRIC/DARK is weak to FAIRY types 'True' or 'false'").lower().strip()
            if Question == "true":
                print("Correct")
                print("ELECTRIC/DARK is weak to FAIRY types")
                Question_number = 2
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 2
                print("ELECTRIC/DARK is weak to FAIRY types")
            else:
                print("INVALID, try again")
        while Question_number == 2:
            print("Question 2/8")
            Question = input ("ROCK/GHOST resist FIGHTING types").lower().strip()
            if Question == "false":
                print("Correct")
                print("ROCK/GHOST is immune to FIGHTING types")
                Question_number = 3
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 3
                print("ROCK/GHOST is immune to FIGHTING types")
            else:
                print("INVALID, try again")
        while Question_number == 3:
            print("Question 3/8")
            Question = input ("BUG/FIRE are neutral to GROUND types").lower().strip()
            if Question == "true":
                print("Correct")
                print("BUG/FIRE have a normal effectiveness to GROUND types")
                Question_number = 4
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 4
                print("BUG/FIRE have a normal effectiveness to GROUND types")
            else:
                print("INVALID, try again")
        while Question_number == 4:
            print("Question 4/8")
            Question = input ("ELECTRIC/POISON are only weak to GROUND types").lower().strip()
            if Question == "false":
                print("Correct")
                print("ELECTRIC/POISON are also weak to PSYCHIC types")
                Question_number = 5
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 5
                print("ELECTRIC/POISON are also weak to PSYCHIC types")
            else:
                print("INVALID, try again")
        while Question_number == 5:
            print("Question 5/8")
            Question = input ("FAIRY/PSYCHIC are weak to POISON types").lower().strip()
            if Question == "true":
                print("Correct")
                print("FAIRY/PSYCHIC are weak to POISON types")
                Question_number = 6
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 6
                print("FAIRY/PSYCHIC are weak to POISON types")
            else:
                print("INVALID, try again")
        while Question_number == 6:
            print("Question 6/8")
            Question = input ("GRASS/DRAGON heavyily resist GRASS").lower().strip()
            if Question == "true":
                print("Correct")
                print("GRASS/DRAGON heavyily resist GRASS")
                Question_number = 7
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 7
                print("GRASS/DRAGON heavyily resist GRASS")
            else:
                print("INVALID, try again")
        while Question_number == 7:
            print("Question 7/8")
            Question = input ("STEEL/DARK are weak to FAIRY types").lower().strip()
            if Question == "false":
                print("Correct")
                print("STEEL/DARK are weak to FAIRY types")
                Question_number = 8
                temp_score = temp_score+1
            elif Question == "true":
                print("Wrong")
                Question_number = 8
                print("FAIRY types resist BUG types")
            else:
                print("INVALID, try again")
        while Question_number == 8:
            print("Question 8/8")
            Question = input ("STEEL types are immune to POISON types").lower().strip()
            if Question == "true":
                print("Correct")
                print("STEEL types are immune to POISON types")
                Question_number = 9
                temp_score = temp_score+1
            elif Question == "false":
                print("Wrong")
                Question_number = 9
                print("STEEL types are immune to POISON types")
            else:
                print("INVALID, try again")
        if Question_number == 9:
            score_h= temp_score
            print("Quiz complete! Your final score is: ",score_h,"out of 5")
            quiz_mode=0
    
