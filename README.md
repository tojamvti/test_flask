The Recipe Book web application allows users to manage and explore various recipes. Users can view a list of recipes, each displayed in a card format with details such as title, ingredients, instructions, and an optional image. The application provides functionality to add new recipes, including uploading images. Additionally, users can search for recipes based on keywords.

Functionality and Function Naming:

recipe_list():

    Description: Renders the main page displaying a list of recipes.
    Functionality:
    Retrieves all recipes from the database.
    Organizes recipes into cards with a responsive layout.

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

recipe_list.html:

    Description: HTML template for rendering the main recipe list page.
    Functionality:
    Utilizes Jinja templating to dynamically display recipe details.
    Organizes recipes into a responsive layout with cards.
    Includes links for adding recipes and searching.

add_recipe.html:

    Description: HTML template for rendering the add recipe page.
    Functionality:
    Includes a form for users to input recipe details.
    Utilizes Jinja templating for form rendering.
    Provides a button to go back to the main recipe list.

style.css:

    Description: CSS file for styling the web application.
    Functionality:
    Defines styles for various elements, such as cards, images, buttons, and layout.
    Enhances the visual appearance and responsiveness of the application.
