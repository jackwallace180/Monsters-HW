class Monster():

    def __init__(self, name, fur, skills, cute, eyes = 4):
        self.name = name
        self.fur = fur
        self.skills = skills
        self.cute = cute
        self.nu_of_eyes = eyes



    def scare(self):
        return 'AHHHHHHH!!!!!! >:)'
    def eat(self, food):
        return 'NOM NOM NOM ' + food
    def transform(self, morph):
        return 'i am now a ' + morph
    def tired(self):
        return 'yawwwwwnnnnn -.-'
    def sleep(self):
        return 'v_v zzzzZZZZZZZ'
    def nightmare(self):
        return 'O.O AHHHHHHHHHHHH HELP!!!'
