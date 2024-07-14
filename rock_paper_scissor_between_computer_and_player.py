import random
import time
my_list=['rock','paper','scissor']

#c1=inputt()
#print(c1)
p_score=c_score=0
while(True):
    c1=random.choice(my_list)
    c2 = ""
    while (len(c2) == 0):
        c2 = input("Rock,Paper or Scissor?: ")


    time.sleep(3)
    print("Computer's choice was: "+c1)
    if((c1=='rock' and c2.lower()=='scissor')or(c1=='paper' and c2.lower()=='rock')or (c1=='scissor' and c2.lower()=='paper')):
        print("Computer wins")
        c_score+=1
    elif((c2.lower()=='rock' and c1=='scissor')or(c2.lower()=='paper' and c1=='rock')or (c2.lower()=='scissor' and c1=='paper')):
        print("Player wins")
        p_score+=1
    else:
        print("Both the choices of computer and player are either same or player has given wrong input!!")

    time.sleep(5)
    print("-------------------------------------------")
    time.sleep(5)
    if(p_score==3):
        print("You won!!")
        time.sleep(3)
        print(f"Score: \n-------\nPlayer score {p_score} : {c_score} Computer Score")
        time.sleep(5)
        break
    elif(c_score==3):
        print("Computer won!!")
        time.sleep(3)
        print(f"Score: \n-------\nPlayer score {p_score} : {c_score} Computer Score")
        time.sleep(5)
        break

