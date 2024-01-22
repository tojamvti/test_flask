# app.py
from flask import Flask, render_template, request, redirect, url_for, g
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
import sqlite3

app_info = {
    'db_file' : r"E:\Flask\test_flask\data\recipies.db"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

def get_db():

    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info["db_file"])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):

    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# Dummy data for recipes
recipes = [
    {"title": "Pasta", "ingredients": "Water, Salt, Pasta", "instructions": "Boil water, add salt, cook pasta.", "image_path": "123.jpg"},
    {"title": "Salad", "ingredients": "Lettuce, Tomatoes, Cucumber", "instructions": "Chop vegetables, mix in a bowl.", "image_path": None},
    {"title": "Pizza", "ingredients": "Flour, Water, Tomato Sauce, Pepperoni, Cheese", "instructions": "Mix flour with water, spread sauce and add toppings.", "image_path": None},
]

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired("Enter recipe title")])
    ingredients = TextAreaField('Ingredients', validators=[InputRequired("Enter ingredients")])
    instructions = TextAreaField('Instructions', validators=[InputRequired("Enter instrucions")])
    image = FileField('Upload Image')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/recipe_list')
def recipe_list():
    db = get_db()
    sql_command = 'select id, title, ingredients, instructions from recipies;'
    cur = db.execute(sql_command)
    recipies = cur.fetchall()

    return render_template('recipe_list.html', recipies=recipies)

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

        db = get_db()
        sql_command = 'insert into recipies(title, ingredients, instructions) values(?, ?, ?)'
        db.execute(sql_command, [title, ingredients, instructions])
        db.commit()

        #new_recipe = {"title": title, "ingredients": ingredients, "instructions": instructions, "image_path": image_path}
        #recipes.append(new_recipe)

        return redirect(url_for('recipe_list'))

    return render_template('add_recipe.html', form=form)

def save_image(image, title):

    image_path = f"static/images/{title.lower().replace(' ', '_')}.jpg"
    image.save(image_path)
    return image_path

@app.route('/best_recipe')
def best_recipe():
    return render_template('best_recipe.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)
