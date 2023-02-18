class Lion():
    color = "yellow"
    classification = "animal"

    def hunting(self):
        print("Lion is hunting")

    def attack_claw(self):
        print("Claw attack")


class Eagle():
    color = "brown"
    classification = "bird"

    def hunting(self):
        print("Eagle is hunting")

    def attack_beak(self):
        print("Beak attack")


class Shark():
    color = "blue"
    classification = "fish"

    def hunting(self):
        print("Shark is hunting")

    def attack_teeth(self):
        print("Teeth attack")


class Monster(Lion, Eagle, Shark):
    color = "green"
    classification ="beast"

    def playing(self):
        print("Monster is playing")

    def attack_tail(self):
        print("Tail attack")


monster = Monster()     # Class instance generating
monster.playing()       # monster instance playing method calling
monster.hunting()       # monster instance 'Lion' class 'hunting' method by inheritance
monster.attack_teeth()  # monster instance 'Shark' class 'attack_teeth' method by inheritance


