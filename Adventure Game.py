import os
import random
import time

items = []

def scrolling_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print(" ↵", end='')
    user_input = input()
    if user_input == "":
        return True
    else:
        return False

def splash(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def path(p1, p2, p1_func, p2_func):
    scrolling_text(f"Do you choose: {p1}/{p2})")
    chosen_path = input("Choice: ").strip().lower()
    if chosen_path == p1.lower():
        scrolling_text(f"You've decided to choose: {p1}...")
        p1_func()
    elif chosen_path == p2.lower():
        scrolling_text(f"You've decided to choose: {p2}...")
        p2_func()
    else:
        scrolling_text("You stand there confused...")
        path(p1, p2, p1_func, p2_func)

def gameover(cause):
    print(f"Oh no, you have fallen due to {cause}...")
    splash("""

      _____          _____        ______  _______        ______                 _____     ____      ____      ______        _____   
  ___|\    \     ___|\    \      |      \/       \   ___|\     \           ____|\    \   |    |    |    | ___|\     \   ___|\    \  
 /    /\    \   /    /\    \    /          /\     \ |     \     \         /     /\    \  |    |    |    ||     \     \ |    |\    \ 
|    |  |____| |    |  |    |  /     /\   / /\     ||     ,_____/|       /     /  \    \ |    |    |    ||     ,_____/||    | |    |
|    |    ____ |    |__|    | /     /\ \_/ / /    /||     \--'\_|/      |     |    |    ||    |    |    ||     \--'\_|/|    |/____/ 
|    |   |    ||    .--.    ||     |  \|_|/ /    / ||     /___/|        |     |    |    ||    |    |    ||     /___/|  |    |\    \ 
|    |   |_,  ||    |  |    ||     |       |    |  ||     \____|\       |\     \  /    /||\    \  /    /||     \____|\ |    | |    |
|\ ___\___/  /||____|  |____||\____\       |____|  /|____ '     /|      | \_____\/____/ || \ ___\/___ / ||____ '     /||____| |____|
| |   /____ / ||    |  |    || |    |      |    | / |    /_____/ |       \ |    ||    | / \ |   ||   | / |    /_____/ ||    | |    |
 \|___|    | / |____|  |____| \|____|      |____|/  |____|     | /        \|____||____|/   \|___||___|/  |____|     | /|____| |____|
   \( |____|/    \(      )/      \(          )/       \( |_____|/            \(    )/        \(    )/      \( |_____|/   \(     )/  
    '   )/        '      '        '          '         '    )/                '    '          '    '        '    )/       '     '   
        '                                                   '                                                    '                  
""", 0.0001)
    time.sleep(3)
    os.system("shutdown /p")

def beginning():
    splash("""

  _____                 _____            ______   _________________      ______        _____   
 |\    \   _____    ___|\    \       ___|\     \ /                 \ ___|\     \   ___|\    \  
 | |    | /    /|  /    /\    \     |    |\     \\______     ______/|     \     \ |    |\    \ 
 \/     / |    || |    |  |    |    |    |/____/|   \( /    /  )/   |     ,_____/||    | |    |
 /     /_  \   \/ |    |__|    | ___|    \|   | |    ' |   |   '    |     \--'\_|/|    | |    |
|     // \  \   \ |    .--.    ||    \    \___|/       |   |        |     /___/|  |    | |    |
|    |/   \ |    ||    |  |    ||    |\     \         /   //        |     \____|\ |    | |    |
|\ ___/\   \|   /||____|  |____||\ ___\|_____|       /___//         |____ '     /||____|/____/|
| |   | \______/ ||    |  |    || |    |     |      |`   |          |    /_____/ ||    /    | |
 \|___|/\ |    | ||____|  |____| \|____|_____|      |____|          |____|     | /|____|____|/ 
    \(   \|____|/   \(      )/      \(    )/          \(              \( |_____|/   \(    )/   
     '      )/       '      '        '    '            '               '    )/       '    '    
            '                                                               '                  
""", 0.0001)
    time.sleep(3)
    scrolling_text("You wake up alone sitting on top of a pile of trash... (Press Enter to continue)")
    scrolling_text("Confused, you start thinking about how you got here...")
    scrolling_text("You pat the ash from your clothes and stand up...")
    scrolling_text("You look around and see a path leading to the left and right...")
    scrolling_text("There are poles with signs on them...")
    scrolling_text("You see a sign on the left that says 'To Town'")
    scrolling_text("You see a sign on the right that says 'To Forest'")
    path("Village", "Forest", village_scene, forest)

def village_scene():
    scrolling_text("You arrive at the village...")
    scrolling_text("You see a sign that says 'Welcome to the Village of the Lost'...")
    scrolling_text("As you walk through the village, you notice that there were no people...")
    scrolling_text("As you keep walking trying to find somebody, you hear a loud noise...")
    scrolling_text("A villager walks up to you and says 'You are not welcome here'...")
    scrolling_text("The villager pulls out a sword and attacks you...")
    def fight():
        pass
    path("Fight", "Run", fight, forest)
    scrolling_text("After a few minutes, you became friends with the villager...")
    scrolling_text("You:'So, what is this place?'")
    scrolling_text("Villager:'This is the Village of the Lost, one of the only surviving places here after the plastic incident'...")
    scrolling_text("You:'Plastic incident?'")
    scrolling_text("Villager:'Yes, the plastic incident, it was a disaster that happened a few years ago'...")
    scrolling_text("You:'What happened?'")
    scrolling_text("Villager: 'After plastic became the main source of everything, it started to take over the world, leading to the ocean to be filled with this waste'...")
    scrolling_text("Villager: 'This pollution choked marine wildlife, damaged soil and poisoned groundwater, and caused serious health impacts'...")
    scrolling_text("Villager: 'The world was in chaos, and many people died, and the survivors were forced to adapt to this new reality'...")
    scrolling_text("Villager: 'We had to learn to live with the plastic, to find ways to survive in this changed world'...")
    scrolling_text("Villager: 'Some of us found refuge in places like this village, while others were not so lucky'...")
    scrolling_text("Villager: 'But we continue to hope for a better future, and work towards finding a solution to the plastic problem'...")
    scrolling_text("You:'That's a lot to take in... What can I do to help?'")
    scrolling_text("Villager: 'For now, you should rest and regain your strength. There will be time to discuss more later.'")
    scrolling_text("You nod and follow the villager to a small hut where you can rest.")
    scrolling_text("You guys walked to a cozy little house and the villager pulled out a book...")
    scrolling_text("Villager: 'Here, read this and you'll understand everything about plastic: https://sites.google.com/wis.edu.hk/is-there-problem-with-plastic/problem-research'")
    scrolling_text("You:'Thank you, I'll read it right away'")
    items.append("Book")
    scrolling_text("You've received a book about plastic pollution!")
    scrolling_text("Villager: 'Rest well, and now you can just explore the village and see what you can find'")
    village()

def village():
    scrolling_text("You walk towards the inner of the village...")
    scrolling_text("You see a dark path leading to somewhere...")
    scrolling_text("You see a small shop with a sign that says 'Make some money!'...")
    path("Dark Path", "Shop", forest, gambling)

def gambling():
    scrolling_text("You walk inside, and you see several gambling machines...")
    scrolling_text("There are so many to choose from, which one do you wanna play?")
    path("Slot Machine", "Blackjack", slot_machine, blackjack)

def slot_machine():
    scrolling_text("You approach the slot machine and insert a coin...", 0.01)
    result = [random.choice(["7️⃣", "🅱️🅰️®️", "🍒", "🍀", "🔔", "💎", "🍉", "🧲"]) for _ in range(3)]
    scrolling_text(f"The reels spin... {result[0]} - {result[1]} - {result[2]}", 0.01)
    if result[0] == result[1] == result[2]:
        scrolling_text("Congratulations! You've won the jackpot!")
        items.append("Secret Coin")
        scrolling_text("You've received a Secret Coin!")
    else:
        scrolling_text("Sorry, you didn't win this time. Better luck next time!", 0.01)
    path("Play Again", "Leave", slot_machine, village)

def blackjack():
    scrolling_text("You sit at the blackjack table and place your bet...", 0.01)

    player_hand = [random.randint(1, 11), random.randint(1, 11)]
    dealer_hand = [random.randint(1, 11), random.randint(1, 11)]

    scrolling_text(f"Your hand: {player_hand[0]} and {player_hand[1]} (Total: {sum(player_hand)})", 0.01)
    scrolling_text(f"Dealer's hand: {dealer_hand[0]} and ?", 0.01)

    while sum(player_hand) < 21:
        scrolling_text("Do you want to Hit or Stand?", 0.01)
        choice = input().strip().lower()
        if choice == "hit":
            new_card = random.randint(1, 11)
            player_hand.append(new_card)
            scrolling_text(f"You drew a {new_card}. Your hand: {player_hand} (Total: {sum(player_hand)})", 0.01)
        elif choice == "stand":
            break
        else:
            scrolling_text("Invalid choice. Please choose 'Hit' or 'Stand'.", 0.01)

    while sum(dealer_hand) < 17:
        new_card = random.randint(1, 11)
        dealer_hand.append(new_card)

    scrolling_text(f"Dealer's hand: {dealer_hand} (Total: {sum(dealer_hand)})")

    if sum(player_hand) > 21:
        scrolling_text("You bust! Dealer wins.")
    elif sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
        scrolling_text("Congratulations! You win!")
        items.append("Secret Card")
        scrolling_text("You've received a Secret Card!")
    else:
        scrolling_text("Dealer wins. Better luck next time!")

    path("Play Again", "Leave", blackjack, village)

def forest():
    scrolling_text("You arrive at the forest...")
    scrolling_text("You see a sign saying 'DANGER: DO NOT ENTER'...")
    scrolling_text("You decide to ignore the sign and venture deeper into the forest...")
    scrolling_text("As you walk, you hear strange noises and feel like you're being watched...")
    scrolling_text("Suddenly, a huge plastic monster appears in front of you!")
    scrolling_text("The monster roars and blocks your path...")
    path("Fight", "Run", fight_monster, run_from_monster)

def run_from_monster():
    scrolling_text("You turn around and start running as fast as you can...")
    scrolling_text("But the monster is too fast and catches up to you...")
    gameover("being caught by the plastic monster")

def fight_monster():
    scrolling_text("You decide to stand your ground and fight the monster...")
    scrolling_text("The monster looks at you and says, 'If you want to defeat me, you must answer my questions about plastic pollution!'")
    quiz()

def quiz():
    questions = [
        {
            "question": "What is the main cause of plastic pollution?",
            "choices": ["A. Natural disasters", "B. Human activities", "C. Animal activities", "D. Solar flares"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a consequence of plastic pollution?",
            "choices": ["A. Improved air quality", "B. Enhanced soil fertility", "C. Harm to marine life", "D. Increased plant growth"],
            "answer": "C"
        },
        {
            "question": "What can individuals do to reduce plastic pollution?",
            "choices": ["A. Use single-use plastics", "B. Recycle and reuse plastics", "C. Burn plastic waste", "D. Dump plastics in the ocean"],
            "answer": "B"
        }
    ]

    for q in questions:
        scrolling_text(q["question"])
        for choice in q["choices"]:
            scrolling_text(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == q["answer"]:
            scrolling_text("Correct... The monster is weakened by your knowledge!")
        else:
            scrolling_text("Wrong answer! The monster attacks you...")
            gameover("failing the quiz")

    scrolling_text("You have answered all the questions correctly! The monster vanishes, and you continue your journey.")
    path("Continue to deeper forest", "Return to village", deeper_forest, village)

def deeper_forest():
    scrolling_text("You venture deeper into the forest, feeling more confident after defeating the monster...")
    def hunter_encounter():
        scrolling_text("As you walk deeper into the forest, you encounter a hunter...")
        scrolling_text("Hunter: 'Halt! Who goes there?'")
        scrolling_text("You: 'I'm just a traveler trying to find my way.'")
        scrolling_text("Hunter: 'If you wish to pass, you must prove your knowledge about plastic pollution. Answer my questions correctly, or face the consequences!'")
        hunter_quiz()

    def hunter_quiz():
        questions = [
            {
                "question": "What percentage of plastic waste is actually recycled globally?",
                "choices": ["A. 9%", "B. 25%", "C. 50%", "D. 75%"],
                "answer": "A"
            },
            {
                "question": "Which type of plastic is most commonly found in ocean debris?",
                "choices": ["A. PET", "B. HDPE", "C. LDPE", "D. PP"],
                "answer": "A"
            },
            {
                "question": "How long does it take for a plastic bottle to decompose in the ocean?",
                "choices": ["A. 10 years", "B. 50 years", "C. 100 years", "D. 450 years"],
                "answer": "D"
            },
            {
                "question": "What is the Great Pacific Garbage Patch primarily composed of?",
                "choices": ["A. Metal waste", "B. Glass waste", "C. Plastic waste", "D. Organic waste"],
                "answer": "C"
            },
            {
                "question": "Which country is the largest producer of plastic waste?",
                "choices": ["A. China", "B. India", "C. USA", "D. Brazil"],
                "answer": "C"
            }
        ]

        for q in questions:
            scrolling_text(q["question"])
            for choice in q["choices"]:
                scrolling_text(choice)
            answer = input("Your answer: ").strip().upper()
            if answer == q["answer"]:
                scrolling_text("Correct... The hunter nods in approval.")
            else:
                scrolling_text("Wrong answer! The hunter attacks you...")
                gameover("failing the hunter's quiz")

        scrolling_text("You have answered all the questions correctly! The hunter allows you to pass.")
        path("Continue to final mountain", "Return to village", final_mountain, village)

    hunter_encounter()

def final_mountain():
    scrolling_text("You arrive at the final mountain, where the air is thin and the wind is cold...")
    scrolling_text("You see three doors in front of you...")
    scrolling_text("The middle door looks like you can just push open...")
    scrolling_text("The left door has a lock with a familiar pattern...")
    scrolling_text("The right door has a lock with a familiar pattern...")
    def inspect_doors():
        scrolling_text("Which door do you want to inspect?")
        path("Left Door", "Right Door", inspect_left_door, inspect_right_door)

    def inspect_left_door():
        if "Secret Coin" in items:
            scrolling_text("You take out the Secret Coin and insert it into the lock. The door opens!")
            scrolling_text("You enter the left door...")
            scrolling_text("You find that same slot machine you played earlier, but this time it's different...")
            scrolling_text("You insert the Secret Coin and pull the lever...")
            scrolling_text("The reels spin... 🍀 - 🍀 - 🍀")
            scrolling_text("You are stuck in eternal loop of gambling...")
            gameover("gambling addiction")
        else:
            scrolling_text("You are unable to enter the left door without the Secret Coin.")
        inspect_doors()

    def inspect_right_door():
        if "Secret Card" in items:
            scrolling_text("You take out the Secret Card and insert it into the lock. The door opens!")
            scrolling_text("You enter the right door...")
            scrolling_text("You find a blackjack table with a dealer waiting for you...")
            scrolling_text("You sit down and start playing...")
            scrolling_text("You play a few rounds and win some chips...")
            scrolling_text("You are stuck in eternal loop of gambling...")
            gameover("gambling addiction")
        else:
            scrolling_text("You are unable to enter the right door without the Secret Card.")
        inspect_doors()

    def middle_door():
        scrolling_text("You push open the middle door and continue your journey.")
        scrolling_text("You find yourself at the peak of the mountain, where a wise sage awaits you.")
        scrolling_text("Sage: 'Congratulations on making it this far. Your journey is almost complete.'")
        scrolling_text("Sage: 'But first, you must answer one final question about plastic pollution.'")
        final_quiz()

    def final_quiz():
        question = {
            "question": "What is the most effective way to reduce plastic pollution?",
            "choices": ["A. Recycling", "B. Reducing plastic use", "C. Cleaning up beaches", "D. Banning plastic"],
            "answer": "B"
        }
        scrolling_text(question["question"])
        for choice in question["choices"]:
            scrolling_text(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == question["answer"]:
            scrolling_text("Correct! The sage nods in approval and grants you passage to the final destination.")
            scrolling_text("You have completed your journey and helped spread awareness about plastic pollution!")
        else:
            scrolling_text("Wrong answer! The sage shakes his head and you are striked by lightning...")
            gameover("failing the final quiz")

    path("Inspect Doors", "Middle Door", inspect_doors, middle_door)

print("PLEASE IDEALLY PLAY IN LOCAL IDE INSTEAD OF REPLIT FOR THE BEST EXPERIENCE")
time.sleep(3)
beginning()