# promt user for weather input
weather = input("what's the weather like today?(sunny/rainy/cold);")

# provide clothing recommendations based on user input
if weather.lower() == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
