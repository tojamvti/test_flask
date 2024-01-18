# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Dummy data for recipes
recipes = [
    {"title": "Pasta", "ingredients": "Water, Salt, Pasta", "instructions": "Boil water, add salt, cook pasta."},
    {"title": "Salad", "ingredients": "Lettuce, Tomatoes, Cucumber", "instructions": "Chop vegetables, mix in a bowl."},
    {"title": "Pizza", "ingredients": "Dough, Tomatoes, Cucumber", "instructions": "Chop vegetables, mix in a bowl."},
]

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    ingredients = TextAreaField('Ingredients', validators=[InputRequired()])
    instructions = TextAreaField('Instructions', validators=[InputRequired()])

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

        new_recipe = {"title": title, "ingredients": ingredients, "instructions": instructions}
        recipes.append(new_recipe)

        return redirect(url_for('recipe_list'))

    return render_template('add_recipe.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
