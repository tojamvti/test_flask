# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dummy data for recipes
recipes = [
    {"title": "Pasta", "ingredients": "Water, Salt, Pasta", "instructions": "Boil water, add salt, cook pasta.", "image_path": "123.jpg"},
    {"title": "Salad", "ingredients": "Lettuce, Tomatoes, Cucumber", "instructions": "Chop vegetables, mix in a bowl.", "image_path": None},
    {"title": "Pizza", "ingredients": "Flour, Water, Tomato Sauce, Pepperoni, Cheese", "instructions": "Mix flour with water, spread sauce and add toppings.", "image_path": None},
]

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    ingredients = TextAreaField('Ingredients', validators=[InputRequired()])
    instructions = TextAreaField('Instructions', validators=[InputRequired()])
    image = FileField('Upload Image')

@app.route('/')
def recipe_list():
    return render_template('recipe_list.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()

    if form.validate_on_submit():
        title = form.title.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data

        # Save the uploaded image
        image_path = None
        if form.image.data:
            image_path = save_image(form.image.data, title)

        new_recipe = {"title": title, "ingredients": ingredients, "instructions": instructions, "image_path": image_path}
        recipes.append(new_recipe)

        return redirect(url_for('recipe_list'))

    return render_template('add_recipe.html', form=form)

def save_image(image, title):
    image_path = f"static/images/{title.lower().replace(' ', '_')}.jpg"
    image.save(image_path)
    return image_path

if __name__ == '__main__':
    app.run(debug=True)
