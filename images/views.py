from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import ImageCreateForm 

@login_required
def image_create(request):
	if request.method == 'POST':
		#Formularz został wysłany
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			#Dane formularza są prawidłowe
			cd = form.cleaned_data
			new_item = form.save(commit=False)
			#Przypisywanie bierzącego użytkownika do elementu
			new_item.user = request.user
			new_item.save()
			messages.succes(request, 'Obraz został dodany.')
			#Przekierowanie do widoku szczegółowego nowo dodanego obrazu.
			return redirect(new_item.get_absolute_url())
	else:
		#Utworzenie formularza na podstawie dancyh dostarczonych przez bookmarklet w żądaniu GET.
		form = ImageCreateForm(data=request.GET)
	return render(request, 'images/image/create.html', {'section': images, 'form': form})


