from datetime import datetime
from django.db.models import Sum, Avg, Max, Min
from django.db.models.functions import Round
from django.shortcuts import HttpResponse, render
from .models import ClientForm
from .utils import convert_string_to_number

# Create your views here.
def index(request):
    if request.method == "POST":
        file = request.FILES.get("my_file")
        if file:
            file_contents = file.read().decode("utf-8")
            txt_data = file_contents.split("\n")
            for item in txt_data:
                ClientForm.objects.update_or_create(
                    type=item[0:1],
                    date=datetime.strptime(item[1:9], '%Y%m%d').strftime('%m/%d/%Y'),
                    value=convert_string_to_number(item[9:19]),
                    cpf=item[19:30],
                    card=item[30:42],
                    time=item[42:48],
                    hoster=item[48:62],
                    store=item[62:81],
                    name=file,
                )
            return HttpResponse("File uploaded and processed successfully!!")

    return render(request, "index.html")

def table(request):
    data = ClientForm.objects.aggregate(sum=Round(Sum('value')), max=Max('value'), min=Min('value'), avg=Round(Avg('value')))
    return render(request, 'table.html', {"data": data})


