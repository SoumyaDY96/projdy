from random import randint as rd

game_list=[rd(1,5), rd(1,5), rd(1,5)] 


def game_choice():
    
    ind,value=game_input()
    index=int(ind)
    if game_list[index]==value:
        print("congratulations!")
        game_option()
    else:
        print("Sorry! better luck next time.")
        game_option()

def game_input():
    global pos,pos_value;
    lenn=len(game_list)
    pos=input("Give the index position :")
    if pos.isdigit()==False:
        print("Index must be a NUMBER!!")
        game_input()
    elif int(pos)>=lenn:
        print("list index out of range")
        game_input()
    else:
        pos_value=int(input("Give the value :"))
        print("Let's Go")
    return (pos,pos_value)

def game_option():
    ans=str.upper(input("Do you want to play the game: (Y/N) ", ))
    if ans== 'Y' :
        game_choice()
    elif ans=='N' :
         print ("Thank you")
    else:
        print ("Kindly provide a string value")
        game_option()
        
        
game_option()        