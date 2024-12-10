from gc import is_finalized

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
       "name" : "Cristeano Ronaldo",
        "follower_count" : 300,
        "description" : "Footballer",
        "country" : "Portugal"
    },
    {   "name" : "Lionel Messi",
        "follower_count" : 130,
        "description" : "Footballer",
        "country" : "Argentina"

    },
    {   "name" : "Neymar",
        "follower_count" : 190,
        "description" : "Footballer",
        "country" : "Brazil"
    },
    {
        "name" : "MUhammad Rizwan",
        "follower_count" : 500,
        "description" : "Footballer",
        "country" : "Pakistan"
    },
    {
        "name" : "Dwayne Johnson",
        "follower_count" : 181,
        "description" : "actor and professional wrestler ",
        "country" : "US"
    },
    {
        "name" : "Selena Gomez",
        "follower_count" : 175,
        "description" : "Musician and actress",
        "country" : "US"
    },
    {
        "name" : "Kylie Jenner",
        "follower_count" : 172,
        "description" : "Reality TV personality and businesswoman",
        "country" : "US"
    },
    {
        "name" : "Kim Kardashian",
        "follower_count" : 167,
        "description" : "Reality TV personality and businesswoman",
        "country" : "US"
    },
    {
        "name ": "Hania Amir",
        "follower_count" : 160,
        "description" : "Actress",
        "country" : "Pakistan"
    },
    {
        "name" : "Shah Rukh Khan",
        "follower_count" : 155,
        "description" : "actor and producer",
        "country" : "India"
    },
    {
        "name" : "Virat Kohli",
        "follower_count" : 150,
        "description" : "Cricketer",
        "country" : "India"
    },
]
import random

def format_data(account):
    """ Format account data into printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
should_continue = True
account_b = random.choice(data)
while should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct :
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

