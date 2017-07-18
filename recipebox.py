'''
The code below represents one way that one might hard-code recipes into a recipe box, but does not offer
solutions to the extensions.
'''

# 1st Recipe adapted from http://www.oliviascuisine.com/new-york-style-bacon-egg-and-cheese/
# New York-Style Bacon, Egg and Cheese Sandwich

// the name of the recipe
bec_name = 'New York-Style Bacon, Egg and Cheese Sandwich'

// create a dictionary for the recipe ingredients (keys) and the amount of them (values)
bec_ingredients = {'Sesame, Everything or Whole Wheat Bagel': '1', 'Butter': '3 tsp', 'Cooked Bacon':'2 slices', 'Eggs':'2', 'American Cheese':'2 slices', 'Salt and Pepper': 'to taste' }

// create an empty list
bec_instructions = []

// add the recipe instructions to the list
bec_instructions.append('1. Slice bagel in half and spread the butter on the cut sides.')
bec_instructions.append('2. Pre-heat your cast iron pan (or griddle) over medium heat. Once hot, toast the bagels until golden brown.')

/* ADD YOUR CODE HERE - Complete and add the rest of the recipe instructions to the list */




# Create list of qualities that designate a recipe
bec = [bec_name, bec_ingredients, bec_instructions]

# 2nd Recipe adapted from http://www.foodnetwork.com/recipes/ree-drummond/macaroni-and-cheese-recipe
# Macaroni and Cheese

// the name of the recipe
mc_name = 'Macaroni and Cheese'

// create a dictionary for the recipe ingredients (keys) and the amount of them (values)
mc_ingredients = {'Dried Macaroni':'4 cups', 'Egg':'1', 'Butter':'1/2 stick','All-purpose Flour':'1/4 cup', 'Whole Milk':'2 1/2 cups', 'Dry Mustard':'2 tsp', 'Cheddar Cheese':'1 pound', 'Salt':'to taste', 'Black Pepper':'1/2 tsp', 'Optional spices':'cayanne pepper, paprika, thyme'}

// create an empty list
mc_instructions = []

// add the recipe instructions to the list
mc_instructions.append('1. Pre-heat the oven to 350 degrees F.')
mc_instructions.append('2. Grate the Cheddar Cheese.')

/* ADD YOUR CODE HERE - Complete and add the rest of the recipe instructions to the list */



# Create list of qualities that designate a recipe
mc = [mc_name, mc_ingredients, mc_instructions]

# Add recipes to the recipe box, or list of recipes.
recipebox = [mc, bec]           # PLEASE PAY ATTENTION! "recipebox" IS A LIST OF LISTS!

# Print all recipes
for recipe in recipebox: 
                                # Print Recipe name
    
    /* ADD YOUR CODE HERE - to print "recipe" name */
    
                                # Print ingredients
    
    /* ADD YOUR CODE HERE - to print "recipe" ingredients by assigning recipe[1] list to the "ingredients" variable */
    
    for item, amount in ingredients.items(): 
                                # Print item, amount
    
     /* ADD YOUR CODE HERE - to print "recipe" ingredients */
    
                             
    for step in recipe[2]:       #Print instructions
    
    /* ADD YOUR CODE HERE - to print "recipe" instructions */
        

    print("")
    print("")
