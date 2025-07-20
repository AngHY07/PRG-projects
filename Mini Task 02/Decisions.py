# Ang Hao Yi (10273989D)
import random
Bot_Mood = ["happy", "sad", "excited", "angry","bored"]

temperature = float(input("Enter current temperature: "))

random_value = random.randint(0,4)

if temperature < 0 :
    out_or_in = "go to the moon to escape the cold"
elif temperature > 30: 
    out_or_in = "go to the beach to enjoy the sun"
else : 
    out_or_in = "stay home and relax with a cup of coffee"

print (f"The temperature for today is {temperature} degree celsius so i will {out_or_in}. I am feeling very {Bot_Mood[random_value]} now.")