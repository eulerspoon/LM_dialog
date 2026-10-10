import json

class Personality:
    def __init__(self, short_name):
        with open('personalities.json') as file:
            me = json.load(file)[short_name]

        self.short_name = short_name
        self.full_name = me.full_name
        self.age = me.age
        self.profession = me.profession
        self.language = me.language
        self.info = me.info

    def get_personality_info(self):
        return f"Name: {self.full_name}\nAge: {self.age}\nProfession: {self.profession}\nLanguage: {self.language}\nInfo: {self.info}"