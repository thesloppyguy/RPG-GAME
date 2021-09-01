import random
from CLASS.game import person, bcolours
from CLASS.magic import spell
from CLASS.inventory import items

#ATTACK SPELLS
fire = spell("FIRE",10,100,"DARK")
thunder = spell("THUNDER",10,100,"DARK")
blizzard = spell("BLIZZARD",10,100,"DARK")
meteor = spell("METEOR",20,200,"DARK")
quake = spell("QUAKE",14,140,"DARK")

#HEALING SPELLS
cure = spell("CURE",12,120,"WHITE")
cura = spell("CURA",18,200,"WHITE")

#RECOVERY ITEM
potion = items("POTION","POTION","HEALS 50 HP",50)
hipotion = items("HI-POTION","POTION","HEALS 100 HP",100)
superpotion = items("SUPER POTION","POTION","HEALS 500 HP",500)
elixer = items("ELIXER","ELIXER","FULLY RESTORES HP/MP OF ONE PARTY MEMBER",9999)
hielixer = items("HI-ELIXER","ELIXER","FULLY RESTORES HP/MP OF ALL PARTY MEMBERS",9999)

#DAMAGE ITEM
granade = items("GRANADE","ATTACK","DEALS 500 DMG",500)

#PLAYER FILES
player_spells = [fire,thunder,blizzard,meteor,cura,cure]
player_items =  [{"item":potion, "quantity": 4},
                 {"item":hipotion, "quantity": 4},
                 {"item":superpotion, "quantity": 4},
                 {"item":elixer, "quantity": 4},
                 {"item":hielixer, "quantity": 2},
                 {"item":granade, "quantity": 4}]

#PLAYERS
player1 = person("sahil",4600,185,180,34,player_spells,player_items)
player2 = person("waffl",3200,150,400,34,player_spells,player_items)
player3 = person("panca",7300,135,200,10,player_spells,player_items)

player_list=[player1,player2,player3]

#ENEMIES
enemey1 = person("rak",9999,60,45,25,[meteor,quake,cura],[])
enemey2 = person("bob",2500,60,45,25,[meteor,quake,cura],[])
enemey3 = person("tim",2500,60,45,25,[meteor,quake,cura],[])

enemey_list=[enemey1,enemey2,enemey3]

#MAIN
running =True
i=0

print(bcolours.FAIL + bcolours.BOLD + "AN ENEMEY ATTACKS!" + bcolours.ENDC)

while running:
        print("=============================================================================")
        print("\n")
        print("PLAYER :")
        print("NAME                             HP                               MP")
        for player in player_list:
                player.status()

        print("\n")
        print("ENEMEY :")
        print("NAME                             HP                               MP")
        for enemey in enemey_list:
                enemey.enemey_status()

        for player in player_list:
                player.chose_action()
                choice=input("choose")
                act_choice=int(choice)-1

                #ATTACK
                if act_choice==0:
                        player_choice=int(input("which enemey do you want to attack"))-1
                        dmg=player.generate_damage()
                        enemey_list[player_choice].take_dmg(dmg)
                        print("you attacked for ", dmg, "HP new enemy HP is ", enemey_list[player_choice].get_hp())
                #MAGIC
                elif act_choice==1:
                        player_choice = int(input("which enemey do you want to attack")) - 1
                        player.chose_spell()
                        val = input("choose spell")
                        spell_number = int(val)-1
                        spell = player.magic[spell_number]
                        dmg = spell.generate_damage()
                        cost = spell.cost
                        if spell_number == -1:
                                continue

                        if cost> player.get_mp():
                                print(bcolours.FAIL+bcolours.BOLD+ "low mp"+bcolours.ENDC)

                        elif cost<player.get_mp():
                                player.reduce_mp(cost)
                                print("your choice is ", spell.name)
                                if spell.type == "WHITE":
                                        player.heal(dmg)
                                        print("you have healed for ",dmg)
                                elif spell.type == "DARK":
                                        enemey_list[player_choice].take_dmg(dmg)
                                        print("you attacked for ", dmg, "HP new enemy HP is ", enemey_list[player_choice].get_hp())

                #ITEMS
                elif act_choice==2:
                        player.chose_item()
                        val1=input("enter choice")
                        item_number=int(val1)-1
                        inv_item = player.items[item_number]

                        if item_number == -1:
                                continue

                        if inv_item["quantity"] == 0:
                                print(bcolours.FAIL+"\n"+"NO ITEM LEFT TRY ANOTHER ITEM"+bcolours.ENDC)
                                continue
                        else:

                                inv_item["quantity"]-=1



                        if inv_item["item"].type == "POTION":
                                player.heal(inv_item["item"].properties)
                                print(bcolours.OKGREEN + bcolours.BOLD +"POTION HEALED PLAYER FOR :" + str(inv_item["item"].properties)+bcolours.ENDC)

                        elif inv_item["item"].type == "ATTACK":
                                player_choice=int(input("which  enemey would you like to attack "))-1
                                enemey_list[player_choice].take_dmg(inv_item["item"].properties)
                                print(bcolours.FAIL + bcolours.BOLD +"GRANADE DELT DAG FOR :"+ str(inv_item["item"].properties)+bcolours.ENDC)

                        elif inv_item["item"].type == "ELIXER":
                                player.mp=player.maxmp
                                player.hp=player.maxhp
                                print(bcolours.FAIL + bcolours.BOLD + "ELIXER RESTORED HEALTH AND MP FULLY " + bcolours.ENDC)

#ENEMEY ATTACK

        for enemy in enemey_list:
                        enemy_choice = random.randrange(0, 2)

                        if enemy_choice == 0:
                                # Chose attack
                                target = random.randrange(0, 3)
                                enemy_dmg = enemy.generate_damage()

                                player_list[target].take_dmg(enemy_dmg)
                                print(enemy.name.replace(" ", "") + " attacks " + player_list[target].name.replace(" ","") + " for",enemy_dmg)

                        elif enemy_choice == 1:

                                spell_number=random.randrange(0,3)
                                spell = player.magic[spell_number]
                                magic_dmg=spell.generate_damage()
                                enemy.reduce_mp(spell.cost)
                                if spell.type == "WHITE":
                                        enemy.heal(magic_dmg)
                                        print(bcolours.OKBLUE + spell.name + " heals " + enemy.name + " for",
                                              str(magic_dmg), "HP." + bcolours.ENDC)
                                elif spell.type == "DARK":

                                        target = random.randrange(0, 3)

                                        player_list[target].take_dmg(magic_dmg)

                                        print(bcolours.OKBLUE + "\n" + enemy.name.replace(" ","") + "'s " + spell.name + " deals",str(magic_dmg), "points of damage to " + player_list[target].name.replace(" ","") + bcolours.ENDC)

                                        if player_list[target].get_hp() == 0:
                                                print(player_list[target].name.replace(" ", "") + " has died.")
                                                del player_list[player]

#CHECK STATUS
        player_defeated =0
        enemey_defeated =0
        for player in player_list:
                if player.get_hp()==0:
                        print("PLAYER :",player.name," has died")
                        player_defeated+=1

        for enemey in enemey_list:
                if enemey.get_hp()==0:
                        print("PLAYER :",enemey.name," has died")
                        enemey_defeated+=1

        if enemey_defeated==3:
                print(bcolours.OKGREEN + bcolours.BOLD + "YOU WON" + bcolours.ENDC)
                running=False
        elif player_defeated==3:
                print(bcolours.FAIL + bcolours.BOLD + "YOU LOST" + bcolours.ENDC)
                running= False
