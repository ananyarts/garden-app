# Garden Advice App
# Prints gardening advice based on the season and the type of plant.

# Hardcoded values for the season and plant type.
# Change these to get advice for a different season or plant.
season = "summer"
plant_type = "flower"

# Empty string that we add advice to as the program runs
advice = ""

# Season advice:
# check which season was chosen and add the matching tip.
# If the season isn't recognised, add a default message.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Plant type advice:
# check which plant type was chosen and add the matching tip.
# If the plant type isn't recognised, add a default message.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Show all the collected advice to the user
print(advice)
