from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
import re
from .forms import CommentForm
from .forms import RatingForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "index.html"
    paginate_by = 6


def recipe_detail(request, slug):
    """
    Display an individual recipe post.

    **Context**

    ``recipe``
        An instance of :model:`recipe.Post`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """
    # Return all objects of the class Recipe
    queryset = Recipe.objects.filter(status=1)

    # Return recipe with the correct slug
    recipe = get_object_or_404(queryset, slug=slug)
    recipe_title = recipe.title
    

    # Split ingredients and preparation steps into se#veral strings 
    ingredients = recipe.ingredients.split('<br>')
    preparation = recipe.preparation.split('<br>')
    # Remove any HTML tags 
    ingredients = [re.sub('<[^<]+?>', '', ingredient) for ingredient in ingredients]
    preparation = [re.sub('<[^<]+?>', '', step) for step in preparation]

    
    # Set liked to false by default
    recipe_liked = False
    
    if recipe.likes.filter(id=request.user.id).exists():
        recipe_liked = True
    
    # Display only approved comments
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    # Display a form to users, so they can add comments to a recipe post
    # Make form functinal by adding POST method
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            print(comment_form)
            print(recipe)
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment will be submitted once approved.'
            )

    comment_form = CommentForm()
    

    return render(
        request,
        "recipe_detail.html",
        {"recipe": recipe,
        "recipe_title": recipe_title,
        "ingredients": ingredients,
        "preparation": preparation,
        "recipe_liked": recipe_liked,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
    )

def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    if form.is_valid():
            rating = form.cleaned_data['rating']
            # Calculate the new average rating
            current_rating = recipe.rating if recipe.rating else 0
            num_of_ratings = recipe.num_of_ratings if recipe.num_of_ratings else 0
            new_average_rating = ((current_rating * num_of_ratings) + int(rating)) / (num_of_ratings + 1)
            recipe.rating = round(new_average_rating, 2)
            recipe.num_of_ratings = num_of_ratings + 1
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RatingForm()
    
    return render(request, 'rate_recipe.html', {'form': form})
