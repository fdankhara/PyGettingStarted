print("Welcome to: 'This Is YOUR Choice'")
choice6 = ""
choice2= ""
def choiceSix():
    choice6 = input().upper()
    if choice6 == "YES":
        print("You pick up a stone from the ground and start to pick at the rocks. Minutes later, a diamond falls into your hands. You see your wolf run up to you with a ruby in its mouth. You realise you have not named it. What do you want to call it?")
        wolfname = input().upper()
        print(wolfname," is a great name! It will only respond to you now!")
    elif choice6 == "NO":
        print("You wander deeper into the cave, watching the wolf play around. It hits you that you haven't chosen a name for your wolf. It comes in front of you and looks up at you. What do you want to name it?")
        wolfname = input()
        print("Wow! What a great name! Your wolf is now called ", wolfname)

def choiceTwo():
    choice2 = input().uppper()
    print(choice2);
    if choice2 == "WANDER DEEPER IN":
        print("You find a wolf. It is tame but hurt. Do you help it or leave it?")
        choice3 = input().upper()
        if choice3 == "HELP IT":
            print("You helped it and it was grateful enough to commit to stay with you as your best friend.")
            print("Your wolf smells something ahead. Do you want to follow it?")
            choice4 = input().upper()
            if choice4 == "YES":
                print("You stumble into a massive cave with a waterfall splashing over it. Do you want to go in?")
            elif choice4 == "NO":
                print("You walk back to the ariplane with the wolf at your tail. You were then killed by a wolf pack who thought your wolf friend was in danger.")
            elif choice3 == "LEAVE IT":
                print("The wolf pack hunts you down and kills you by ripping you bit by bit.")
        elif choice2 == "TURN AROUND":
            print("You spend the night in the airplane. The next day, you go back into the forest. You find a wolf which is hurt. You help it and become best friends. The wolf smells something. Do you follow it or not?")
            if choice4.upper() == "YES":
                print("You stumble into a massive cave with a waterfall splashing over it. Do you want to go in?")
                choice5 = input().upper()
            elif choice4 == "NO":
                print("You walk back to the ariplane with the wolf at your tail. You spend the night there but then you are killed by the wolf pack who thought your wolf was in danger. GAME OVER")
                if choice5 == "NO":
                    print("You are thirsty, so you take a drink from the waterfall")
                    print("You then see something sparkle in the cave. You decide to cautiously walk into it.")
                    print("You find yourself surrounded by diamonds and precious gems of all types. Do you want to take some?")
                elif choice5 == "YES":
                    print("You find yourself surrounded by diamonds and precious gems of all types. Do you want to take some?")
                    choice6 = input().upper()
                    choiceSix()

def startHere():
    choice = input().upper()
    if choice == "STAY AND FIND SUPPLIES":
        print("Good choice. You found a pocketknife and some crackers (biscuits)")
        print("You start to walk into the forest and hear a roar somewhere deeper in the forest. Do you wander deeper or turn around?")
    elif choice == "WALK INTO THE FOREST AHEAD":
        print("You immediately regret the decision and go back to find supplies. You find a pocketknife and some crackers")
        print("You start to walk into the forest and hear a roar somewhere deeper in the forest. Do you wander deeper or turn around?")
        choiceTwo()
        
    
print("What is your name?")
name = input()
print("Hello, ",name)
print("Get ready...")
print("You have just woken up from an airplane crash. You see the airplane behind you, in flames. You are the only surviver. Do you stay and find any supplies left or walk into a forest ahead of you?")
startHere()
            
