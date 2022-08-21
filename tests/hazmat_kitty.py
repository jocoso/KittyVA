from pet_displayer import Pet
import os
import actions

class HazmatKitty(Pet):
    def __init__(self):
        Pet.__init__(self, os.path.realpath("../resources") + '\\cat_idle_cropped.gif', 5)

        # add actions
        self.add_action('Say Hello', self.say_hello)
        self.add_action('Tell me a joke', self.tell_me_a_joke)
        self.add_action('ask', self.ask)
        
    def say_hello(self):
        self.say("hello")
        
    def tell_me_a_joke(self):
        joke = actions.get_joke()
        self.say(joke)

    def ask(self):
        self.get_user_input()

#impath = os.path.realpath("../resources") + '\\'
#catimagepath = impath + 'cat_idle_cropped.gif'

pet = HazmatKitty()
pet.run()
