import random
import time

space = """










































"""
glad_shop = {"STEEL GREATSWORD":
                {"Type":"Weapon", "Gold Cost":1000, "Damage":70, "Health":0, "Required Strength":85, "Required Dexterity":40},
            "STEEL WARHAMMER":
                {"Type":"Weapon", "Gold Cost":1000, "Damage":60, "Health":20, "Required Strength":110, "Required Dexterity":10},
            "STEEL DAGGER":
                {"Type":"Weapon", "Gold Cost":500, "Damage":50, "Health":0, "Required Strength":20, "Required Dexterity":65},
            "IRON DAGGER":
                {"Type":"Weapon", "Gold Cost":200, "Damage":25, "Health":0, "Required Strength":20, "Required Dexterity":45},
            "THORS HAMMER":
                {"Type":"Weapon", "Gold Cost":10000, "Damage":300, "Health":100, "Required Strength":250, "Required Dexterity":20},
            "STEEL BREASTPLATE":
                {"Type":"Armour", "Gold Cost":2000, "Damage":10, "Health":200, "Required Strength":100, "Required Dexterity":10},
            "STEEL HELMET":
                {"Type":"Helmet", "Gold Cost":1000, "Damage":5, "Health":100, "Required Strength":90, "Required Dexterity":10}
            }

inventory = {"RUSTY DAGGER":
                {"Type":"Weapon", "Gold Cost":10, "Damage":15, "Health":0, "Required Strength":0, "Required Dexterity":0}
            }

equipment = {"CAP":
                {"Type":"Helmet", "Gold Cost":10, "Damage":0, "Health":40, "Required Strength":0, "Required Dexterity":0},
            "BONE CLUB":
                {"Type":"Weapon", "Gold Cost":10, "Damage":10, "Health":10, "Required Strength":0, "Required Dexterity":0},
            "TUNIC":
                {"Type":"Armour", "Gold Cost":10, "Damage":0, "Health":80, "Required Strength":0, "Required Dexterity":0}}
count = 0
battles_won = 0
people_killed = 0
player_level = 1
player_gold = 500
gold_earnt = 0
gold_reward = 0
new_train = True
new_fight = True

class Player(object):
    def __init__(self, name, strength, dexterity, health, damage):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.health = health
        self.damage = damage
# player = Player("john", 50, 50, 100, 20)

def playerStats():
    player.health = 100+(player_level*10)
    player.damage = 100+(player_level*10)
    for i in equipment:
        print("")
        print ("______________________________",i)
        print(equipment[i]["Health"])
        player.health += equipment[i]["Health"]
        player.damage += equipment[i]["Damage"]
    return player

def intro():
    print(space)
    print("______________________________THE ARENA______________________________\n\n")
    input("Greetings gladiator, it is time to choose your Name, Strength and Dexterity. Press Enter to continue...")
    input("Remember, your total Strength and Dexterity must exceed no more than 100 points when combined...\n")

def char_creation():
    while True:
        input("Press Enter to Create your Gladiator...\n")
        try:
            player = Player(input("Name: "), int(input("Strength: ")), int(input("Dexterity: ")), 100, 20)
            if len(player.name) < 3:
                input("Name too short. Try Again...\n")
                continue
            if player.strength + player.dexterity != 100:
                input("Strength and Dexterity do not add up to 100. Try Again...\n")
                continue
            return player
        except(ValueError):
            input("Invalid Strength or Dexterity Input. Try Again...\n")

def training():
    print("\n_____________________________BEGIN")
    time.sleep(1)
    print("\n O_/ \_O - CLASH")
    time.sleep(1)
    print("\n \_O-\ \__O_ - CLING")
    time.sleep(1)
    print("\n __O-| <O_/ - BASH")
    time.sleep(1)
    print("\n <O_/\_O_ - BING")
    time.sleep(1)
    print("\n \_O-||-O> - BONG")
    time.sleep(1)

def jimmy_intro():
    input("\nCongratulation %s, you have been picked out from a wide variety of slaves to have the honor of fighting in the SNEINTON PITS!.." % (player.name.capitalize()))
    input("\nIm the Arena Master Jimbo, let me give you a brief introduction of how these things work...")
    input("We're in the Barracks right now, this is where we will return after every Fight. That is if you survive of course...")
    input("Here in the barracks you have five options...")
    input("1) Manage your Inventory...")
    input("2) Train in the Courtyard...")
    input("3) Purchase items from the Shop...")
    input("4) View Stats and Equipment...")
    input("5) Fight in the Pits...")
    input("You may need to win a fight before you have much gold however...")
    input("You can also choose to enter the SNEINTON PITS at anytime, be warned however, the more matches you win the tougher Gladiators you'll face...")
    input("Well that just about wraps things up here. I got a feeling your gonna make us both a lot of money...")
    input("I'll leave you to decide what you do next, however i suggest taking part in some training, then leaving your mark on the pits! Goodluck...\n\n")

def destination():
    is_true = True
    while is_true == True:
        print(space)
        decision = input("\n****************************************************************************************\n\n______________________________THE BARRACKS\n\n______________________________SHOP\n______________________________INVENTORY\n______________________________STATS AND EQUIPMENT\n______________________________TRAIN\n______________________________FIGHT\n\nWhere do you want to go: ")
        if decision.lower() == "shop":
            count = 1
            return count
        elif decision.lower() == "inventory":
            count = 2
            return count
        elif decision.lower() == "train":
            count = 3
            return count
        elif decision.lower() == "fight":
            count = 4
            return count
        elif decision.lower() == "stats":
            count = 5
            return count
        else:
            input("\nPlease type in either 'Shop', 'Inventory', 'Stats', 'Train' or 'Fight'. Press Enter to Try Again...\n")

def shop(x):
    print(space)
    randGreet = random.randint(1,5)
    input("Entering Shop...\n")
    if randGreet == 1:
        input("Alan The Shopkeep: Hey there %s, come take a look at my wares..." % (player.name.capitalize()))
    elif randGreet == 2:
        input("Alan The Shopkeep: Well well, if it isnt my main man %s, come check out my goods..." % (player.name.capitalize()))
    elif randGreet == 3:
        input("Alan The Shopkeep: %s! Good to see you again, lets have a look at what ive got today..." % (player.name.capitalize()))
    elif randGreet == 4:
        input("Alan The Shopkeep: Hey Chad. I meaan errrr %s? Yea %s! Lets have a look at what ive got today..." % (player.name.capitalize(), player.name.capitalize()))
    else:
        input("Alan The Shopkeep: Hello %s, come take a look at what ive got today..." % (player.name.capitalize()))
    input("\nHit Enter to display Shop...\n")
    while True:
        print(space)
        global player_gold
        print("****************************************************************************************")
        print ("\n______________________________ BARRACKS SHOP")
        for i in x:
            print ("\n______________________________",i)
            for p in x[i]:
                print ("______________________________",p,':',x[i][p])
        print("\n______________________________ Available Gold: %s" % (player_gold))
        print("\n****************************************************************************************")
        decision = input("\nType in the Item you would like to buy, or alternatively type EXIT to leave: ")
        if decision.lower() == "exit":
            input("\nYou turn around and walk back to the Barracks...\n")
            count = 0
            playerStats()
            return player_gold, player, inventory, glad_shop, count
        elif decision.upper() in glad_shop.keys():
            if player_gold >= glad_shop[decision.upper()]["Gold Cost"]:
                ans = input("\nAre you sure you want to purchase the %s for %s Gold?\nType Y or N: " % (decision, glad_shop[decision.upper()]["Gold Cost"]))
                if ans.lower() == "y":
                    player_gold = (player_gold - glad_shop[decision.upper()]["Gold Cost"])
                    inventory[decision.upper()] = glad_shop.get(decision.upper())
                    glad_shop.pop(decision.upper())
                    input("\nCongratulations! You have bought your very own %s." % (decision.upper()))
                    input("You can view and equip your %s from your Inventory." % (decision.upper()))
                    input("\nBack to Shop...")
            else:
                input("\nYou dont have enough Gold for that! Pick a different item...")
        else:
            rand2 = random.randint(1,3)
            if rand2 == 1:
                input("\nWhat!? Pick one i have or exit my shop...")
            elif rand2 == 2:
                input("\nChoose your item, and spell it out to me...")
            else:
                input("\nAre you mad? Either buy something i have or leave...")
                continue

def inv(inventory):
    while True:
        print(space)
        print("\n****************************************************************************************\n")
        print("______________________________Your Inventory______________________________")
        for i in inventory:
            print("")
            print ("______________________________",i)
            for p in inventory[i]:
                print ("______________________________",p,':',inventory[i][p])

        decision = input("\nTo Equip one of these items type its Name, alternatively type EXIT to go back to The Barracks: ")
        if decision.lower() == "exit":
            input("\nYou turn around and walk back to the Barracks...\n")
            count = 0
            playerStats()
            return player, inventory, equipment, count
        elif decision.upper() in inventory.keys():
            replace = input ("\nYou have selected your %s, please type in the item from your equipment you wish to exchange it for: " % (decision.upper()))
            if replace.upper() in equipment.keys():
                if (inventory[decision.upper()]["Type"]) == (equipment[replace.upper()]["Type"]):
                    if player.strength >= (inventory[decision.upper()]["Required Strength"]) and player.dexterity >= (inventory[decision.upper()]["Required Dexterity"]):
                        equipment[decision.upper()] = inventory.get(decision.upper())
                        inventory[replace.upper()] = equipment.get(replace.upper())
                        equipment.pop(replace.upper())
                        inventory.pop(decision.upper())
                        input("\nYou have exchanged your %s for your %s, hit Enter to go back to your Inventory..." % (decision.upper(), replace.upper()))
                    else:
                        print("\nYou cannot equip %s because you do not meet the requirements.\n|Required Strength: %d | Player Strength: %d \n|Required Dexterity: %d | Player Dexterity: %d" % (decision.upper(), inventory[decision.upper()]["Required Strength"], inventory[decision.upper()]["Required Dexterity"], player.strength, player.dexterity))
                        input("\nPress Enter to go back to Inventory...")
                else:
                    input("\nYou must select two items of the same Type, you are trying to replace %s with %s. Press Enter to go back to Inventory..." % (inventory[decision.upper()]["Type"], equipment[replace.upper()]["Type"]))
            else:
                input("\nSorry, you dont have %s in your Equipment. Press enter to review your Inventory..." % (replace.upper()))
        else:
            input("\nSorry, you dont have that item. Press enter to review your Inventory...")

def train():
    global new_train
    global player_gold
    print(space)
    input("Welcome to the Training Arena...\n")
    if (new_train == True):
        input("Here you can spend Gold to increase your Strength and Dexterity Attributes...")
        input("Each training session will cost 100 Gold and can improve each stat up to 10 times...")
        new_train = False
    if player_gold >= 100:
        while True:
            input("\n_____________________________Available Gold: %s" % (player_gold))
            ans = input("\nDo you want to train with a random fellow Gladiator for 100 Gold? Type Y/N: ")
            if ans.lower() == "y":
                input("\nFinding available Gladiator...")
                time.sleep(2)
                player_gold -= 100
                rand = random.randint(1,6)
                if rand == 1:
                    input("\nYou will be training with Sparticus! A true honor, he will surely improve your Skill significantly. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(5,10)
                    rand_str = random.randint(5,10)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))
                elif rand == 2:
                    input("\nYou will be training with Crixus! A great Swordsman, he will improve your Strength significantly. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(3,7)
                    rand_str = random.randint(5,10)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))
                elif rand == 3:
                    input("\nYou will be training with Gannicus! A fast and agile fighter, he will improve your Dexterity significantly. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(5,10)
                    rand_str = random.randint(3,7)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))
                elif rand == 4:
                    input("\nYou will be training with Varro! Not the greatest of warriors, but skillful enough for you to learn. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(2,6)
                    rand_str = random.randint(4,8)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))
                elif rand == 5:
                    input("\nYou will be training with Asher! An unfortunate partner, lacking skill and can teach you very little. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(1,4)
                    rand_str = random.randint(1,4)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))
                elif rand == 6:
                    input("\nYou will be training with Barca! An agile gladiator, but not the strongest. He can still teach you a thing or two. Press Enter to begin your training...")
                    training()
                    rand_dex = random.randint(4,8)
                    rand_str= random.randint(2,6)
                    input("\nTraining Complete. Press Enter to see how you've improved...\n")
                    input("Your Strength Rating has increased from %s to %s!" % (player.strength, (player.strength+rand_str)))
                    input("Your Dexterity Rating has increased from %s to %s!" % (player.dexterity, (player.dexterity+rand_dex)))

                player.strength += rand_str
                player.dexterity += rand_dex
                input("Return to Barracks...")
                count = 0
                return new_train, player_gold, player, count
            elif ans.lower() == "n":
                input("\nReturning to Barracks...")
                count = 0
                return new_train, player_gold, player, count
            else:
                input("\nInvalid input, press Enter to try again...")
                continue
    else:
        input("\nSorry %s, you only have %s gold. You need 100 gold to train with another Gladiator..." % (player.name.capitalize(), player_gold))

    input("\nBack to The Barracks...")
    count = 0
    return new_train, player_gold, player, count

def fight():
    global new_fight
    global player_gold
    global player_level
    print(space)
    if (new_fight == True):
        input("Tutorial")
        new_fight = False
    if (new_fight == False):
        input("War is coming")

    input("Back to The Barracks...")
    count = 0
    return new_fight, player_level, player_gold, gold_reward, player, count

def stats():
    playerStats()
    print(space)
    print("______________________________ATTRIBUTES")
    print ("______________________________Name: ", player.name.capitalize())
    print ("______________________________Strength Rating: ", player.strength)
    print ("______________________________Dexterity Rating: ", player.dexterity)
    print ("______________________________Health Rating: ", player.health)
    print ("______________________________Damage Rating: ", player.damage)
    print("\n______________________________Battles Won: ", battles_won)
    print("______________________________People Killed: ", people_killed)
    print("______________________________Gold Earnt: ", gold_earnt)
    print("\n______________________________Gold: ", player_gold)
    input("\nPress Enter to see Equipment...\n")
    print("______________________________EQUIPMENT")
    for i in equipment:
        print("")
        print ("______________________________",i)
        for p in equipment[i]:
            print ("______________________________",p,':',equipment[i][p])

    input("\nPress Enter to go back to The Barracks...")
    count = 0
    return player, count



intro()
player = char_creation()
jimmy_intro()
while True:
    if count == 0:
        count = destination()
        continue
    if count == 1:
        player_gold, player, inventory, glad_shop, count = shop(glad_shop)
        continue
    if count == 2:
        player, inventory, equipment, count = inv(inventory)
        continue
    if count == 3:
        new_train, player_gold, player, count = train()
        continue
    if count == 4:
        new_fight, player_level, player_gold, gold_reward, player, count = fight()
        continue
    if count == 5:
        player, count = stats()
        continue
