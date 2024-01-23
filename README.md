The Recipe Book web application allows users to manage and explore various recipes. Users can view a list of recipes, each displayed in a card format with details such as title, ingredients, instructions, and an optional image. The application provides functionality to add new recipes, including uploading images. Additionally, users can search for recipes based on keywords.

Functionality and Function Naming:

get_db():

    Description: Opens database if it wasn't open before

close_db():

    Description: After closing application ensures that database is closed if not it closes it

index():

    Description: Renders main paige displaying welcome message with photo.

recipe_list():

    Description: Renders Recipe List page displaying a list of recipes.
    Functionality:
    Retrieves all recipes from the database.
    Organizes recipes into table with show image, edit and delete option.

add_recipe():

    Description: Renders the page for adding a new recipe.
    Functionality:
    Handles both GET and POST requests.
    Displays a form for users to input recipe details (title, ingredients, instructions, and image).
    Validates and saves the submitted form data to the database.

save_image(image, title):

    Description: Saves an uploaded image with a filename derived from the recipe title.
    Functionality:
    Takes an image file and the title of the associated recipe.
    Generates a filename based on the title and saves the image in the "static/images/" folder.
    Returns the path to the saved image.

best_recipe():

    Description: Renders Best Recipe page.

contact():

    Description: Renders Contact page with form where user can input name, e-mail and message.
    
    Functionality: Form saves message into database.

about():

    Description: Renders About page.

faq():

    Description: Renders FAQ page.

recipe_delete():

    Description: Deletes recipe record from database.
    
    Functionality: Takes recipe_id which is uniqe id of recipe and deletes record from database with this exact id.

about.html:

    Description: Template for About page, that contains basic information about app.

add_recipe.html:

    Description: Template for Add Recipe page.
    Includes a form for users to input recipe details.
    Provides a button to go back to the main recipe list.

base.html:

    Description: Base template that other templates extend from.

best_recipe.html:

    Description: Template for Best Recipe page that  prints pizza recipe.

recipe_list.html:

    Description: HTML template for rendering the main recipe list page.
    Functionality:
    Utilizes Jinja templating to dynamically display recipe details.
    Organizes recipes into a responsive layout with cards.
    Includes links for adding recipes and searching.

style.css:

    Description: CSS file for styling the web application.
    Functionality:
    Defines styles for various elements, such as cards, images, buttons, and layout.
    Enhances the visual appearance and responsiveness of the application.
