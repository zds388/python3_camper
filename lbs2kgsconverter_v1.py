print("How many pounds of fondue did you eat?")
pounds = input("Input your pound amount here: ")
kilos = float(pounds) * .453592
kilos = round(kilos, 2)
print(f"You ate {pounds}lbs of fondue?? That's {kilos}kgs of fondue!")
