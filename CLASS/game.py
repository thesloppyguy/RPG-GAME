import random
#from CLASS.magic import spell
#from CLASS.inventory import items
#from main import player_list

class bcolours:
    HEADER = '\033[95m'
    OKBLUE ='\033[94m'
    OKGREEN ='\033[92m'
    WARNING ='\033[93m'
    FAIL ='\033[91m'
    ENDC ='\033[0m'
    BOLD ='\033[1m'
    UNDERLINE ='\033[4m'


class person:
    def __init__(self,name,hp,mp,atk,df,magic,items):
        self.name=name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["ATTACK","MAGIC","ITEMS"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def take_dmg(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def heal(self,heal):
        self.hp+=heal
        if  self.hp>self.maxhp:
            self.hp=self.maxhp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp-=cost

    def chose_action(self):
        i=1
        print("Actions :")
        for item in self.actions:
            print(str(i)+":",item)
            i+=1

    def chose_spell(self):
        i=0
        print("Spells :")
        for item in self.magic:
            print(str(i+1)+":",item.name,"cost : ", item.cost)
            i+=1

    def chose_item(self):
        i=0
        print("ITEMS :")
        for pp in self.items:
            print(str(i+1)+":", pp["item"].name ,"/  ITEM DESCRIPTION :",pp["item"].description,"(x"+str(pp["quantity"])+")")
            i+=1


    def status(self):

            hp_to_unit=round((self.hp/self.maxhp)*25)
            hp_out = hp_to_unit *"█"
            space_units = 25-hp_to_unit
            space_out=space_units*" "

            mp_to_unit=round((self.mp/self.maxmp)*10)
            mp_out=mp_to_unit*"█"
            mp_space = 10-mp_to_unit
            mp_space_out=mp_space*" "

            print("                     _________________________                __________")
            print(str(self.name) + ":    " + str(self.hp) + "/" + str(self.maxhp) + " |" + bcolours.OKGREEN + hp_out + space_out + bcolours.ENDC + "|      " + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolours.OKBLUE + mp_out+mp_space_out + bcolours.ENDC + "|")

    def enemey_status(self):

            hp_to_unit = round((self.hp / self.maxhp) * 25)
            hp_out = hp_to_unit * "█"
            space_units = 25 - hp_to_unit
            space_out = space_units * " "

            mp_to_unit = round((self.mp / self.maxmp) * 10)
            mp_out = mp_to_unit * "█"
            mp_space = 10 - mp_to_unit
            mp_space_out = mp_space * " "

            print("                     _________________________                __________")
            print(str(self.name) + ":    " + str(self.hp) + "/" + str(self.maxhp) + "   |" + bcolours.FAIL + hp_out + space_out + bcolours.ENDC + "|      " + str(self.mp) + "/" + str(self.maxmp) + "   |" + bcolours.OKBLUE + mp_out+mp_space_out + bcolours.ENDC + "|")

