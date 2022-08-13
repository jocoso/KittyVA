import tests.tell_a_joke as Joke
import re

def main():
    is_playing = True
    joke_regex = r'/tell?:jokes|joke' # If the sentence contains tell + joke or jokes

    while is_playing:
        actions = input("What do you need from me?\n")

        # Main Loop Logic
        if re.search(joke_regex, actions):
            print(Joke.get_joke())

        elif actions == 'quit':
            is_playing = False
            
        else:
            print("I am not sure what do you want from me.")
    
if __name__ == "__main__":
    main()
