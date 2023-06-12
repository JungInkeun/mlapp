from django.shortcuts import render, redirect
from regression.models import BikeData
from regression.forms import BikeDataForm

# Create your views here.
def reg_index(request):
    if request.method=="POST":
        form = BikeDataForm(request.POST)
        if form.is_valid():
            instance = form.save()
            if instance.predict_count:
                predict_count = instance.predict_count
            else:
                predict_count = "^^"
            return render(request, "regre/regre.html", {"form": form, "predict_count": predict_count})
    else:
        form = BikeDataForm()

    context = {
        "form":form
    }
    return render(request, "regre/regre.html", context)