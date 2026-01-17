from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        role = request.POST.get("role")

        if role == "hospital":
            return redirect("/waste/userdashboard/")
        elif role == "ca":
            return redirect("/ca/")
        elif role == "tf":
            return redirect("/tf/")
        elif role == "rp":
            return redirect("/rp/")
        else:
            return render(request, "login.html", {
                "error": "Please select a role"
            })

    return render(request, "login.html")
