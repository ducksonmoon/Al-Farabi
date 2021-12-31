from account.forms import UniversityForm, TeamForm
from django.shortcuts import render


def university_create(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
            return render(request, 'account/university_create.html', {'form': form})
    else:
        form = UniversityForm()
    return render(request, 'account/university_create.html', {'form': form})