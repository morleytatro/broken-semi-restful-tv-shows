from django.shortcuts import render

from .models import Show
# Create your views here.

def new_show_page(request):
    return render(request, "new-show.html")

def all_shows_page(request):
    user_id = request.session["user_id"]

    context = {
        "shows": Show.objects.all()
    }

    return render(request, "all-shows.html")

def edit_show_page(request):
    context = {
        "show_to_edit": Show.objects.get(id=show_id)
    }

    return render(request, "edit-show.html")

def show_details_page(request):
    context = {
        "this_show": Show.objects.get(id=show_id)
    }

    return render("view-show.html")

def create_show():
    Show.objects.create(
        title=request.POST["title"],
        network=request.POST["network"],
        description=request.POST["description"],
        release_date=request.POST["release_date"],
    )

    return redirect(f"/shows/{show_id}")

def delete_show(request):
    Show.objects.get(id=show_id).delete()

    return redirect("/dashboard")

def update_show(request):
    show_to_edit = Show.objects.get(request.POST["show_id"])

    show_to_edit.title = request.POST["title"]
    show_to_edit.network = request.POST["network"]
    show_to_edit.release_date = request.POST["release_date"]
    show_to_edit.description = request.POST["description"]

    return redirect(f"/shows/{show_id}")