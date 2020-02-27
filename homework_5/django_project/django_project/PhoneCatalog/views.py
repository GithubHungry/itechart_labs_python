from django.shortcuts import render

from .models import PhoneCatalog


# главная страница со списком загадок
def index(request):
	message = None
	if "message" in request.GET:
		message = request.GET["message"]
	# создание HTML-страницы по шаблону index.html
	# с заданными параметрами latest_riddles и message
	return render(
		request,
		"index.html",
		{
			"latest_phones":
				PhoneCatalog.objects.order_by('-reg_date')[:5],
			"message": message
		}
	)


def detail(request, phone_id):
	error_message = None
	if "error_message" in request.GET:
		error_message = request.GET["error_message"]
	person = PhoneCatalog.objects.get(id=phone_id)
	return render(request, 'full.html', {"error_message": error_message, "person": person})
