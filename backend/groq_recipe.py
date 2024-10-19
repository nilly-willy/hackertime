import os
from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

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

#test case
original_recipe = """
Classic Chicken Stir-Fry

Ingredients:
- Chicken:
  - 1 lb boneless, skinless chicken breast, thinly sliced
- Vegetables:
  - 1 red bell pepper, sliced
  - 1 yellow bell pepper, sliced
  - 1 medium carrot, thinly sliced
  - 1 cup broccoli florets
  - 1 cup snap peas
- Sauce:
  - 3 tbsp soy sauce (or low-sodium soy sauce)
  - 2 tbsp oyster sauce (optional)
  - 1 tbsp sesame oil
  - 1 tbsp cornstarch (to thicken)
  - 1 tbsp rice vinegar
  - 1 tbsp honey (optional, for sweetness)
  - 2 cloves garlic, minced
  - 1 inch fresh ginger, minced
- Optional garnish:
  - Sesame seeds
  - Green onions, chopped

Instructions:
1. In a small bowl, mix together soy sauce, oyster sauce, sesame oil, cornstarch, rice vinegar, honey (if using), garlic, and ginger.
2. Heat a large skillet or wok over medium-high heat with a little oil. Add the sliced chicken and cook until browned, about 4-5 minutes. Remove the chicken and set aside.
3. In the same pan, add a little more oil and cook the vegetables for 3-5 minutes, stirring occasionally until they’re tender but still crisp.
4. Return the chicken to the pan and pour in the sauce mixture. Stir well to combine, and cook for an additional 2-3 minutes until the sauce thickens.
5. Serve hot with rice or noodles and garnish with sesame seeds and green onions if desired.
"""
scaling_factor = 2
food_restriction = "vegetarian"
health_problems = "high cholesterol"
protein_goal = 30

a = get_ingredients(original_recipe)
b = scaling_ingredients(a,scaling_factor)
c = food_restrictions(food_restriction, b)
d = health_modifications(c, health_problems, food_restriction)
e = protein_goals(d, protein_goal)
f = new_recipe(e, original_recipe)
print(f)










    





