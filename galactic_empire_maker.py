# Amir Abu Hani
import random

# Here the list contains 20 materials
materials_list = ["xenolithium", "chrono-matter", "plasmatic resin", "nebulium alloy", "quasar silk", "cryo-gel",
                  "etheric glass", "voidestonr", "biolumnial fluid", "gravitic ore", "psychocrustal", "plasma coral",
                  "arcane metal", "hyperfiber", "quantum foam", "psionic alloy", "tachyon fabric", "polymorphic resin",
                  "antimatter glass", "chronal sand"]
# Creating dictionary of dictionaries that include 4 alien delegations. Each alien delegation has the following details:
# needed materials that randomly selected from materials list and suggestions number
alien_delegations = {"delegation1": {"needed_materials": random.sample(materials_list, 3), "suggestions_number": 4},
                     "delegation2": {"needed_materials": random.sample(materials_list, 2), "suggestions_number": 2},
                     "delegation3": {"needed_materials": random.sample(materials_list, 3), "suggestions_number": 3},
                     "delegation4": {"needed_materials": random.sample(materials_list, 2), "suggestions_number": 5},
                     }

# This variable will be the successful alien delegation convince
number_of_convince = 0


def negotiation():
    global number_of_convince
    for item in alien_delegations:
        # At first, printing the alien delegation name
        alien_name = item
        print(alien_name)
        # This variable will be the number of convincing from me to the alien delegation
        i = 0
        # Extricate the suggestions number for the alien delegation in alien delegation dictionary
        suggeset_number = alien_delegations[item]["suggestions_number"]
        # Randomly, I choose one material from the list materials
        my_suggestion = random.choice(materials_list)
        # as long as the suggesting number for me is smaller than the alien delegation suggestions_number
        while i < suggeset_number:
            # If my suggestion is existing in the list of the alien delegation material
            if my_suggestion in alien_delegations[item]["needed_materials"]:
                print(
                    f"{alien_name} is agree to cooperate with you!. The {my_suggestion} material is exists in the demand")
                number_of_convince += 1
                break
            else:
                # my suggestion is not existing in the list of the alien delegation material, try to choose another
                # material from the list
                remaining_items = [item for item in materials_list if item != my_suggestion]
                my_suggestion = random.choice(remaining_items)
                i += 1
    # The rate of the successful convince
    successful = number_of_convince / len(alien_delegations)
    if successful > 0.7:
        print(f"The rate of successful convince of alien delegations is: {successful} ")
        print("You succeeded in the negotiation!")
    else:
        print(f"The rate of successful convince of alien delegations is: {successful} ")
        print("You failed in the negotiation!")


negotiation()
