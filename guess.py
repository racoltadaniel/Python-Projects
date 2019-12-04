#Guess the number
''' 3 levels of difficulty:
Level 1 = Numbers between 1 and 10
Leven 2 = Numbers between 1 and 25
Level 3 = Numbers between 1 and 50
'''

def guess():

    def countdown(seconds):
        import time
        x = 10
        while seconds > 0:
            print(" " * (10- seconds) + "*" * seconds + str(seconds) + "*" * seconds)
            time.sleep(2)
            seconds -= 1
            if seconds ==0:
                print("        Start!")

    def level():  #level = 2.2
        global n
        level = int(input("Chose level difficulty \n" +
        "Select a number between 1 and 3:"))
        while level > 4 or level < 0:
                level = int(input("Try again: \n" +
                "Select a number between 1 and 3:"))
        if 0 < level < 4:
            print("Level " + str(level) + " is starting in :" )
            if level == 1:
                n = 10
            elif level == 2:
                n = 25
            else:
                n = 50
    
        
        
    def game():
                import random
                import subprocess
                number = random.randint(1,int(n))
                nr_guess = 0
                


                while nr_guess < 4:
                    
                    guess = int(input("Enter a number between 1 and " + str(n) + ":"))
                    nr_guess += 1

                    if nr_guess == 4:
                        subprocess.run(["/usr/bin/notify-send", "--icon=error", "You lost"])
                        print("You lost"+ "\n" + "Better luck next time")
                        subprocess.run(["/usr/bin/notify-send", "--icon=error", "Looser!"])
                        break

                    if number > guess:
                        print("Enter a greater number")

                    if number < guess:
                        print("Enter a lower number")

                   

                    if number == guess:
                        
                        subprocess.run(["/usr/bin/notify-send", "--icon=error", "You won 10 points"])
                        print("Good job!The number was: " + repr(number) + "\n" + "You guessed the number in " + repr(nr_guess) + " attempts")
                        subprocess.run(["/usr/bin/notify-send", "--icon=error", "You won 10 points"])
                        break
                    
        

       
    level()
    countdown(10)
    game()
    

guess()


#subprocess