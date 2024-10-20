import os
from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# app = Flask(__name__)
# CORS(app)
app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

original_recipe = ""

# extracting ingredients from recipe
def get_ingredients(user_input_recipe):
    get_ingredients = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Extract the ingredients from this recipe{user_input_recipe}"
    ,
            }
        ],
        model="llama3-8b-8192",
    )
    get_ingredients_output = get_ingredients.choices[0].message.content
    #print(get_ingredients.choices[0].message.content)
    return get_ingredients_output

# scaling ingredients based on user defined serving size
def scaling_ingredients(ingredients, scaling_factor):
    if scaling_factor == 1:
        return ingredients
    else:
        scaling = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Multiply the quantity of all these {ingredients} by {scaling_factor} and return the
                    new ingredient quantities. Don't show me the multiplication, just return the new quantities"""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(scaling.choices[0].message.content)
        scaling_output = scaling.choices[0].message.content
        return scaling_output

# food restrictions
def food_restrictions(food_restrictions, scaled_ingredients):
    if food_restrictions == []:
        return scaled_ingredients
    else:
        restrictions = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Given these food restrictions: {food_restrictions}, modify my ingredients: {scaled_ingredients} to fit 
                     within these restrictions"""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(restrictions.choices[0].message.content)
        restrictions_output = restrictions.choices[0].message.content
        return restrictions_output

# health issue modifications
def health_modifications(altered_ingredients, health_issues, food_restrictions):
    if health_issues == []:
        return altered_ingredients
    else:
        health_modifications = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Given these health issues: {health_issues}, modify my ingredients and/or quantities to address these
                    health concerns. Here is a list of my ingredients: {altered_ingredients}. Please ensure the modified recipe considers the following:
                    Limit or remove ingredients that exacerbate these health issues.
                    Suggest suitable substitutions for ingredients if necessary.
                    Ensure the recipe remains balanced, flavorful, and enjoyable.
                    Return a list of modified ingredients. Make sure these modifications do not class with these food restrictions: {food_restrictions}. 
                    If they do, find alternatives"""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(health_modifications.choices[0].message.content)
        modifications_output = health_modifications.choices[0].message.content
        return modifications_output

# protein goal modifications
def protein_goals(modified_ingredients, protein_goal):
    if protein_goal == 0:
        return modified_ingredients
    else:
        protein_goals = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Given these ingredients: {modified_ingredients}, modify them so I can reach my protein goal of {str(protein_goal)} grams  in this meal."""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(restrictions.choices[0].message.content)
        protein_modified = protein_goals.choices[0].message.content
        return protein_modified

# final modified recipe
def new_recipe(new_ingredients, original_user_input):

    final_recipe = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Here is the original recipe: {original_user_input}. Replace the ingredients with my modified ones {new_ingredients} 
                    and return the newly modified recipe.
                    """
                }
            ],
            model="llama3-8b-8192",
        )
        #print(restrictions.choices[0].message.content)
    final_output = final_recipe.choices[0].message.content
    return final_output


scaling_factor = 2
food_restriction = "vegetarian"
health_problems = "high cholesterol"
protein_goal = 30

@app.route('/')
def index():
    return "sdf"

@app.route('/api/process_input', methods=['POST', 'OPTIONS'])
def process_input():
    print("hello its meee, the backend")
    global original_recipe
    data = request.get_json()
    original_recipe = data['input']
    print("printing from backend", original_recipe)
    # a = get_ingredients(original_recipe)
    # b = scaling_ingredients(a,scaling_factor)
    # c = food_restrictions(food_restriction, b)
    # d = health_modifications(c, health_problems, food_restriction)
    # e = protein_goals(d, protein_goal)
    # f = new_recipe(e, original_recipe)
    return "hello"

@app.route('/api/submit-selections', methods=['POST'])
def submit_selections():
    # Get the JSON data from the request
    data = request.get_json()

    # Populate HEALTH_PROBLEMS 
    global health_problems
    health_problems = data[0]

    # Populate DIETARY_RESTRICTIONS
    global food_restriction
    food_restriction = data[1]

    # d = health_modifications(c, health_problems, food_restriction

    # Return a response
    print("message Selections received!", data)
    # print(health_problems)
    return "message Selections received!"

if __name__ == '__main__':
    app.run(debug=True)








    





