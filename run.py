import tests.actions as Actions
import re

def main():
    is_playing = True
    verb = {}
    verb['joke'] = r'/tell?:jokes|joke' # If the sentence contains tell + joke or jokes
    verb['opendir'] = r'open|dir'
    
    while is_playing:
        actions = input("What do you need from me?\n")

        # Main Loop Logic

        #Tells you a joke
        if re.search(verb['joke'], actions):
            print(Actions.get_joke())

        # Opens A Given Directory
        elif re.search(verb['opendir'], actions):
            directory = input("What directory do you want to open?\n")
            if(Actions.open_directory(directory)):
                print("Directory opened")
            else:
                print("Sorry, I couldn't open that directory\n")
                
        # Bye
        elif actions == 'quit':
            is_playing = False
            
        else:
            print("I am not sure what do you want from me.")
    
if __name__ == "__main__":
    main()
