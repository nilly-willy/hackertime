import os
from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json 

# app = Flask(__name__)
# CORS(app)
app = Flask(__name__)
CORS(app)

client = Groq(
    api_key="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",
)


# extracting ingredients from recipe
def get_ingredients(user_input_recipe):
    get_ingredients = client.chat.completions.create(
        messages=[
            {
  "role": "user",
  "content": f"""Please extract the ingredients and their corresponding quantities, 
  including measurements (e.g., cups, grams, teaspoons, etc.), from the following 
  recipe: {user_input_recipe}. Ensure to list each ingredient on a new line."""
}

        ],
        model="llama3-8b-8192",
    )
    get_ingredients_output = get_ingredients.choices[0].message.content
    print(get_ingredients.choices[0].message.content)
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
                    "content": f"""Given the following ingredient quantities: {ingredients}, please multiply each quantity by a factor of {scaling_factor}. 
                Return only the new ingredient quantities without showing any calculations or the original amounts."""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(scaling.choices[0].message.content)
        scaling_output = scaling.choices[0].message.content
        return scaling_output

# food restrictions
def food_restrictions(scaled_ingredients, food_restrictions):
    if food_restrictions == []:
        return scaled_ingredients
    else:
        restrictions = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""Please adjust the following ingredient list: {scaled_ingredients} to comply with these food restrictions: {food_restrictions}. 
                Ensure that all modifications are suitable and clearly indicate any changes made to the ingredients."""
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
                    "content": f"""Adjust the following ingredients: {modified_ingredients} to help me achieve my protein goal of {str(protein_goal)} grams for this meal. 
                Please specify any changes made to the ingredient quantities to meet the protein requirement."""
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
                    "content": f"""Here is the original recipe: {original_user_input}. Please replace the ingredients with my modified ones: {new_ingredients}. 
                Format the response so that the ingredients and their quantities are listed first, with each ingredient on a new line. 
                After the ingredients, include each step of the recipe on a new line as well. Return the newly modified recipe in this format."""
                }
            ],
            model="llama3-8b-8192",
        )
        #print(restrictions.choices[0].message.content)
    final_output = final_recipe.choices[0].message.content
    return final_output

original_recipe = ""
modified_ingredients = ""
scaling_factor = 2
food_restriction = "vegetarian"
health_problems = "high cholesterol"
protein_goal = 30

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "intializing..."

@app.route('/api/process_input', methods=['POST', 'OPTIONS'])
def process_input():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success'}), 200
    data = request.get_json()
    if data is None:
        return jsonify({'status': 'error', 'message': 'No input data received'}), 400
    #print('got original data')
    data_input = data.get('input')
    global original_recipe
    original_recipe = data_input
    #print('Received raw data:', data_input) 
    global modified_ingredients
    modified_ingredients = get_ingredients(data_input)
    #print(modified_ingredients)

    results = {
    'status': 'success',
    'input': data_input,
    'result': modified_ingredients
    }
    #print(results)
    return jsonify(results), 200

@app.route('/api/scaling', methods=['POST', 'OPTIONS'])
def scaling_input():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success'}), 200
    data = request.get_json()
    if data is None:
        return jsonify({'status': 'error', 'message': 'No input data received'}), 400
    #print('got scaling data')
    data_input = data.get('input')
    #print('Received raw data:', data_input)
    int_data = int(data_input)
    global modified_ingredients
    modified_ingredients = scaling_ingredients(modified_ingredients,int_data)
    results = {
    'status': 'success',
    'input': int_data,
    'result': modified_ingredients
    }
    print(results)
    return jsonify(results), 200

#food restriction function
#dietary restriction function
@app.route('/api/submit-selections', methods=['POST'])
def submit_selections():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success'}), 200
    data = request.get_json()
    if data is None:
        return jsonify({'status': 'error', 'message':'No input data received'}), 400
    # Get the JSON data from the request

    # Populate HEALTH_PROBLEMS 
    global health_problems
    health_problems = data[0]

    # Populate DIETARY_RESTRICTIONS
    global food_restriction
    food_restriction = data[1]

    global modified_ingredients
    modified_ingredients = food_restrictions(modified_ingredients, food_restriction)
    modified_ingredients = health_modifications(modified_ingredients, health_problems, food_restriction)

    results = {
        'status': 'success',
        'input' : health_problems, 
        'result' : modified_ingredients
    }

    print(results)
    return jsonify(results), 200

@app.route('/api/proteinGoals', methods=['POST', 'OPTIONS'])
def protein_input():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success'}), 200
    data = request.get_json()
    if data is None:
        return jsonify({'status': 'error', 'message': 'No input data received'}), 400
    #print('got protein data')
    data_input = data.get('input')
    #print('Received raw data:', data_input)
    int_data = int(data_input)
    global modified_ingredients
    modified_ingredients = protein_goals(modified_ingredients,int_data)
    
    results = {
    'status': 'success',
    'input': int_data,
    'result': modified_ingredients
    }
    print(results)
    return jsonify(results), 200

@app.route('/api/submit-recipe', methods=['POST', 'OPTIONS'])
def submit_recipe():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success'}), 200
    global modified_ingredients
    global original_recipe
    if modified_ingredients is None or original_recipe is None:
        return jsonify({'status': 'error', 'message': 'No modified ingredients or original recipe found'}), 400

    final = new_recipe(modified_ingredients, original_recipe)
    results = {
        'status': 'success',
        'input': original_recipe,
        'result': final
    }
    print(results)
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True, port = 5000)








    





