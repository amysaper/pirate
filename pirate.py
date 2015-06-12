import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def question ()
"""I ask the user what types of drinks he or she likes and return a dictionary of the results"""
recipe = []
for questions.keys()
  favorite = raw_input (questions.values())
  if favorite = 'y' or 'yes'
    recipe [questions.keys()] = True
return recipe

def drinkmaker(recipe)
drink= []
for recipe.keys()
  if recipe.values() = 'True'
    drink.append(ingredients.values(recipe.keys())
return drink
if _name_=='_main_'
                 question()
                 drinkmaker(recipe)
                 print drink
              