from flask import Flask, render_template, request, redirect, url_for,g
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
import sqlite3

app_info = {
    'db_file' : r"D:\Studia\Python\test_flask\data\recipies.db"
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

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired("Enter recipe title")])
    ingredients = TextAreaField('Ingredients', validators=[InputRequired("Enter ingredients")])
    instructions = TextAreaField('Instructions', validators=[InputRequired("Enter instrucions")])
    image = FileField('Upload Image')

@app.route("/")
def index():
    return render_template('index.html', active_menu='')

@app.route('/recipe_list')
def recipe_list():
    db = get_db()
    sql_command = 'select id, title, ingredients, instructions from recipies;'
    cur = db.execute(sql_command)
    recipies = cur.fetchall()

    return render_template('recipe_list.html', active_menu='recipe_list', recipies=recipies)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()

    if form.validate_on_submit():
        title = form.title.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data

        image_path = None
        if form.image.data:
            image_path = save_image(form.image.data, title)

        db = get_db()
        sql_command = 'insert into recipies(title, ingredients, instructions) values(?, ?, ?)'
        db.execute(sql_command, [title, ingredients, instructions])
        db.commit()

        return redirect(url_for('recipe_list'))

    return render_template('add_recipe.html', active_menu='add_recipe', form=form)

def save_image(image, title):

    image_path = f"static/images/{title.lower().replace(' ', '_')}.jpg"
    image.save(image_path)
    return image_path

@app.route('/best_recipe')
def best_recipe():
    return render_template('best_recipe.html', active_menu='best_recipe')




class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Handle the form submission logic here
        # Access form data using form.name.data, form.email.data, form.message.data
        # Perform any necessary actions with the form data

        return render_template('thank_you.html')

    return render_template('contact.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html', active_menu='other')

@app.route('/faq')
def faq():
    return render_template('faq.html', active_menu='other')

@app.route('/recipe_delete/<int:recipe_id>')
def recipe_delete(recipe_id):

    db = get_db()
    sql_command = 'delete from recipies where id = ?;'
    db.execute(sql_command, [recipe_id])
    db.commit()

    return redirect(url_for('recipe_list'))




if __name__ == '__main__':
    app.run(debug=True)
