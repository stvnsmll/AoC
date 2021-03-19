#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 06.01.21              #
#                       #
# Day 21, Part 2        #
#########################


def main(test):
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        testing = 1
        input_file = "./d21/ingredients_testing.txt"
    else:
        testing = 0
        input_file = "./d21/ingredients.txt"

    # Using readline()
    recipe_file = open(input_file, 'r')
    ingredients_data = []

    while True:
        # Get next line from file
        line = recipe_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        ingredients_data.append(line.strip())

    recipe_file.close()

    food_dict = {}

    counter = 0
    for i in ingredients_data:
        split1 = i.split(" (contains ")
        jarbled = split1[0].split()
        allergens = split1[1][:-1].split(", ")
        #print(f"Jarbled: {jarbled}\n  Allergens: {allergens}")
        food_dict[counter] = Food(jarbled, allergens)
        counter += 1

    print()

    all_ingredients = []
    all_ingredients_with_dupl = []
    all_allergens = []

    for i in food_dict:
        for ingreed in food_dict[i].myJarbled:
            all_ingredients_with_dupl.append(ingreed)
            if ingreed not in all_ingredients:
                all_ingredients.append(ingreed)
        for allergen in food_dict[i].myAllergens:
            if allergen not in all_allergens:
                all_allergens.append(allergen)

    print(f"All possible ingredients: {all_ingredients}")
    print()
    print(f"All possible allergens:   {all_allergens}")
    print()
    print(len(all_ingredients_with_dupl))

    #loop though each allergen, pull out the food items that list that allergen
    #  group each of those lists in a master list and use set.intersection to find common values
    unique_count = 0
    allergen_ingreed_dict = {}
    exit = 0
    while exit == 0:
        allergen_found = ""
        for allergen in all_allergens:
            my_set = []
            for j in food_dict:
                if allergen in food_dict[j].myAllergens:
                    my_set.append(food_dict[j].myJarbled)
            print(f"Allergen: {allergen}")
            #print(f"Sets: {my_set}")
            ingredients_in_all = list(set.intersection(*map(set, my_set)))
            print(ingredients_in_all)
            if len(ingredients_in_all) == 1:
                print("FOUND A UNIQUIE!!!\n")
                allergen_found = allergen
                allergen_ingreed_dict[allergen] = ingredients_in_all[0]
                break
            print()
        if allergen_found != "":
            unique_count += 1
            all_allergens.remove(allergen_found)
            #remove the ingredient from all lists
            for i in food_dict:
                if allergen_ingreed_dict[allergen_found] in food_dict[i].myJarbled:
                    food_dict[i].myJarbled.remove(allergen_ingreed_dict[allergen_found])
        else:
            exit = 1

    print(unique_count)
    for i in allergen_ingreed_dict:
        print(f"Allergen: {i}\n --> Ingr: {allergen_ingreed_dict[i]}")
        print()
    print()

    list_of_allergen_foods = []
    for i in allergen_ingreed_dict:
        list_of_allergen_foods.append(allergen_ingreed_dict[i])
    exit = 0
    print(list_of_allergen_foods)

    for i in list_of_allergen_foods:
        while i in all_ingredients_with_dupl:
            all_ingredients_with_dupl.remove(i)

    print(all_ingredients_with_dupl)
    print()

    for i in allergen_ingreed_dict:
        print(f"Allergen: {i}\n --> Ingr: {allergen_ingreed_dict[i]}")
        print()
    print()

    final_list = ""
    for i in sorted(allergen_ingreed_dict):
        final_list += str("," + str(allergen_ingreed_dict[i]))
    print(final_list)

    print(final_list[1:])

    answer = final_list[1:]


    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    print(f"Runtime Duration: {(datetime.now() - startTime)}")
    return answer


class Food:
    def __init__(self, jarbled, allergens):
        self.myJarbled = jarbled
        self.myAllergens = allergens
        self.myJarbled_Orig = jarbled


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += str(ele)
    # return string
    return str1



if __name__ == "__main__":
    main("r")