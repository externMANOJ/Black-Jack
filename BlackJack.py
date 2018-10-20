from random import shuffle, choice, randint

print ":::::::::::::::::::::::::::::::::::::::"
print ":::::::::::::: BLACKJACK ::::::::::::::"
print ":::::::::::::::::::::::::::::::::::::::"

def sysassign(turn):
    yurcards.append(cards.pop(randint(0,len(cards)-1)))
    print "\nSystem assigns card-%d to you:"%(turn+1),yurcards[turn]
    
    syscards.append(cards.pop(randint(0,len(cards)-1)))
    if turn==0: print "System assigns card-%d to itself: -x-"%(turn+1)
    else: print "System assigns card-%d to itself:"%(turn+1),syscards[turn]

def yurassign(turn):
    print "\nENTER in range(1-%d) To assign card-%d to System:"%(len(cards),turn+1),
    syscards.append(cards.pop(input()-1))
    if turn==0: print "You assigns card-%d to System: -x-"%(turn+1)
    else: print "You assigns card-%d to System:"%(turn+1),syscards[turn]
    
    print "\nENTER in range(1-%d) To assign card-%d to yourself:"%(len(cards),turn+1),
    yurcards.append(cards.pop(input()-1))
    print "You assigns card-%d to yourself:"%(turn+1),yurcards[turn]
    
def check(typ):
    value = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,'J':10,'K':10,'Q':10,'A':11}
    
    checksys, checkyur = [], []
    copysys, copyyur = [], []
    
    for i in syscards:
        copysys.append(i)
        checksys.append(value[i])
        
    for i in yurcards:
        copyyur.append(i)
        checkyur.append(value[i])

    while 'A' in copysys and sum(checksys)>21:
        checksys[copysys.index('A')] = 1
        copysys.remove('A')
            
    while 'A' in copyyur and sum(checkyur)>21:
        checkyur[copyyur.index('A')] = 1
        copyyur.remove('A')

    if typ=="syssum": return sum(checksys)
    if typ=="yursum": return sum(checkyur[1:])
    
    if typ=="declare":
        if sum(checksys)>sum(checkyur):
            print "\nYOU LOSE THE GAME!"
        elif sum(checksys)<sum(checkyur):
            print "\nYOU WON THE GAME!"
        else:
            print "\nGAME DRAW!"

        cards_value(checksys,checkyur)
        
        return False
    
    if sum(checksys)>21 or sum(checkyur)>21:
        if sum(checksys)>21 and sum(checkyur)>21: print "\nGAME DRAW!"
        elif sum(checksys)>21: print "\nYOU WON THE GAME!"
        elif sum(checkyur)>21: print "\nYOU LOSE THE GAME!"

        cards_value(checksys,checkyur)
        
        return False
    
    return True
        
def sys_turn(turn):
    print "\nSystem turn:"
    syschoice = ""
    if check("syssum")==21: syschoice = 1
    elif (check("syssum")>=17 and check("yursum")<16): syschoice = 1
    
    if syschoice==1:
        print "::: System declared the GAME:::"
        if check("declare")==False: return False
    else:
        syscards.append(cards.pop(randint(0,len(cards)-1)))
        print "System assigns card-%d to itself:"%(turn+1),syscards[turn]
        if check("")==False: return False
        else: return True

def yur_turn(turn):
    print "\nYour turn:"
    print "1.Declare the GAME\t2.Continue the GAME"
    print "Select your choice:",
    yurchoice = input()
    
    if yurchoice==1:
        print "::: You declared the GAME :::"
        if check("declare")==False: return False
        
    elif yurchoice==2:
        print "\nENTER in range(1-%d) To assign card-%d to yourself:"%(len(cards),turn+1),
        yurcards.append(cards.pop(input()-1))
        print "You assigns card-%d to yourself:"%(turn+1),yurcards[turn]
        if check("")==False: return False
        else: return True
    else:
        print "\n::: INVALID CHOICE :::"
        exit()

def cards_value(checksys,checkyur):
    print "\nSYSTEM:"
    for i in range(len(syscards)):
        print "card-%d:"%(i+1),syscards[i]
    print "Total:",sum(checksys)

    print "\nYOU:"
    for i in range(len(yurcards)):
        print "card-%d:"%(i+1),yurcards[i]
    print "Total:",sum(checkyur)
    
if __name__=="__main__":
    cards = [2,3,4,5,6,7,8,9,'J','Q','K','A',2,3,4,5,6,7,8,9,'J','Q','K','A',2,3,4,5,6,7,8,9,'J','Q','K','A',2,3,4,5,6,7,8,9,'J','Q','K','A']
    shuffle(cards)
    
    syscards, yurcards = [], []
    
    print "Who want to distribute the cards,"
    print "1.System\t2.You"
    print "Select your choice:",
    turn_choice = input()
    
    try:
        if turn_choice==1:
            for turn in range(2): sysassign(turn)
            turn = 2
            while(check("")):
                if(yur_turn(turn))==False: break
                if(sys_turn(turn))==False: break
                turn+=1
            
        elif turn_choice==2:
            for turn in range(2): yurassign(turn)
            turn = 2
            while(check("")):
                if(sys_turn(turn))==False: break
                if(yur_turn(turn))==False: break
                turn+=1
            
        else:
            print "\n::: INVALID CHOICE :::"
            
    except IndexError as ie: print "\n::: INVALID RANGE ENTERED :::"
