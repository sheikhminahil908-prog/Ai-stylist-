import random

print("👗 Welcome to AI Fashion Stylist 👠")
print("Let's find your perfect outfit today!\n")

style = input("What’s your style today? (casual, formal, party, sporty): ").lower()

if style == "casual":
    suggestions = [
        "Light blue jeans with a white T-shirt and sneakers",
        "Pastel shirt with comfy trousers and flats",
        "Denim jacket with black leggings"
    ]
elif style == "formal":
    suggestions = [
        "Black trousers with white blouse and blazer",
        "Navy blue suit with minimal accessories",
        "Beige pencil skirt with silk top"
    ]
elif style == "party":
    suggestions = [
        "Shiny black dress with heels",
        "Red jumpsuit with gold jewelry",
        "Sparkly top with leather pants"
    ]
elif style == "sporty":
    suggestions = [
        "Track pants with tank top and running shoes",
        "Athleisure hoodie with leggings",
        "Loose tee with shorts and sneakers"
    ]
else:
    suggestions = ["Try something new today! Maybe mix your favorite colors 💖"]

print("\n✨ Fashion Suggestion:")
print(random.choice(suggestions))
