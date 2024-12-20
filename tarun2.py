import pyautogui
import time
import requests
import random

# Fetch random quotes from a reliable API
def fetch_random_quotes():
    url = "https://type.fit/api/quotes"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        quotes = response.json()  # Load the JSON response
        return [quote["text"] for quote in quotes if "birthday" not in quote["text"]]  # Filter for general quotes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quotes: {e}")
        # Fallback to a predefined list of quotes
        return [
            "Happy Birthday, buddy! Cheers to another awesome year ahead!",
            "Wishing you endless happiness on your special day!",
            "Hope your birthday is as fantastic as you are!",
            "Happy Birthday! Let’s make it a day to remember!",
            "Here’s to a year full of adventures and success!",
            "Happy Birthday, my friend! Stay blessed always!",
            "May your birthday bring you lots of joy and laughter!",
            "Cheers to you on your birthday! Have a blast!",
            "Happy Birthday! You’re one of a kind!",
            "Hope all your dreams come true this year!",
            "Wishing you a birthday as fun and amazing as you!",
            "Celebrate big today—you deserve it!",
            "Happy Birthday! Stay awesome, my friend!",
            "Here’s to your best year yet!",
            "Happy Birthday! You deserve the best today and always!",
            "May your birthday be filled with endless fun and surprises!",
            "Hope you have a fabulous day full of cake and laughter!",
            "Happy Birthday to my incredible friend!",
            "Celebrate today because you’re truly special!",
            "Happy Birthday! Let’s make it unforgettable!",
            "Here’s to celebrating you, my amazing fri friend anyone could ask for!",
            "May your birthday bring you closer to your dreams!",
            "Happy Birthday! Keep shining bright!",
            "Wishing you a fantastic day filled with love and joy!",
            "Happy Birthday! Let’s party like there’s no tomorrow!",
            "You’re the life of the party—happy birthday!",
            "Happy Birthday! Your friendship means the world to me!",
            "Here’s to another year of great memories!",
            "Happy Birthday! Let’s make it legendary!",
            "May your birthday be as awesome as you are!",
            "Happy Birthday! Time to eat, laugh, and celebrate!",
            "Hope your special day is full of unforgettable moments!",
            "Happy Birthday! You make life so much better!",
            "Let’s make your birthday a day to remember!",
            "Happy Birthday! You’re the reason we celebrate today!",
            "Here’s to the most amazing friend—happy birthday!",
            "Wishing you a day as special as your heart!",
            "Happy Birthday! Let’s create memories that last forever!",
            "Cheers to you, my wonderful friend!",
            "Happy Birthday! Keep being your awesome self!",
            "May your birthday be full of laughter and love!",
            "Happy Birthday! The world is better with you in it!",
            "Hope your birthday is as bright and beautiful as you!",
            "Happy Birthday! Let’s make it one for the books!",
            "You’re a rockstar—happy birthday!",
            "Happy Birthday! Thanks for being an incredible friend!",
            "Let’s celebrate your awesomeness today!",
            "Happy Birthday! May this year be your best one yet!",
            "Your birthday is a celebration of how amazing you are!",
            "Happy Birthday! Keep chasing your dreams!",
            "May this year bring you everything you’ve been wishing for!",
            "Happy Birthday! Time to make unforgettable memories!",
            "Here’s to celebrating your awesomeness today!",
            "Happy Birthday! You’re truly one in a million!",
            "Wishing you a year full of love, laughter, and adventure!",
            "Happy Birthday! You make the world brighter just by being in it!",
            "Let’s raise a toast to you—happy birthday!",
            "Happy Birthday! Keep spreading positivity and joy!",
            "Wishing you a birthday as wonderful as you are!",
            "Happy Birthday! Stay happy, healthy, and amazing!",
            "Here’s to the best friend anyone could ask for!",
            "Happy Birthday! You’re a true gem!",
            "Hope your birthday is filled with magic and joy!",
            "Happy Birthday! Let’s make it a day to remember forever!",
            "May your birthday bring you endless smiles!",
            "Happy Birthday! You deserve all the good things life has to offer!",
            "Cheers to another year of fabulous friendship!",
            "Happy Birthday! You’re the definition of amazing!",
            "Here’s to a year of laughter, love, and success!",
            "Happy Birthday! You make the world a better place!",
            "Wishing you a day filled with cake, friends, and happiness!",
            "Happy Birthday! You’re the best thing that ever happened to me!",
            "Let’s make your birthday epic!",
            "Happy Birthday! You’re an inspiration to us all!",
            "Hope your special day is as special as you are!",
            "Happy Birthday! You’re the reason we smile today!",
            "Wishing you a birthday full of love and laughter!",
            "Happy Birthday! The world is lucky to have you!",
            "Let’s make your birthday unforgettable!",
            "Happy Birthday! Here’s to another amazing year ahead!",
            "You’re one of a kind—happy birthday, my friend!",
            "Hope your birthday is full of surprises and joy!",
            "Happy Birthday! Life’s better with friends like you!",
            "May your birthday be filled with peace and happiness!",
            "Happy Birthday! You’ve got so much to celebrate!",
            "Cheers to a birthday as cool as you are!",
            "Happy Birthday! Wishing you endless good vibes!",
            "May your day be as sweet as your birthday cake!",
            "Happy Birthday! The world is brighter because of you!",
            "Let’s make today all about you—happy birthday!",
            "Happy Birthday! You’re loved more than words can say!",
            "May this birthday be your best one yet!",
            "Happy Birthday! Let’s make it a masterpiece! ",
           ]

def send_prank_messages(quotes, count):
    time.sleep(5)  # Wait 5 seconds to switch to the WhatsApp Web chat window
    for i in range(count):
        random_quote = random.choice(quotes)  # Select a random quote from the list
        message = f"︻デ═一 \n :){i+1}\n🎉🎂 Happy Birthday Tarun! \n {random_quote}  "  # Create the message
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press("enter")  # Press Enter to send
        time.sleep(0.5)  # Reduce delay between messages to 0.5 seconds

if __name__ == "__main__":
    quotes = fetch_random_quotes()  # Fetch a list of random quotes
    count = 20  # Number of times to send the message
    print("Switch to WhatsApp Web and select the chat within 5 seconds...")
    send_prank_messages(quotes, count)
