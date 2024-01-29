// add_recipe.js

document.addEventListener('DOMContentLoaded', function () {
    const recipeForm = document.getElementById('recipeForm');

    recipeForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Add any additional logic or validation if needed

        // Submit the form using JavaScript
        this.submit();
    });
});
