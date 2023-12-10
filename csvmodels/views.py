
from django.shortcuts import HttpResponse, render
from .models import ClientForm
from datetime import datetime
# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    if request.method == "POST":
        file = request.FILES["my_file"]
        if file:
            file_contents = file.read().decode("utf-8")
            txt_data= file_contents.split("\n")
            for item in txt_data:
                fileup = ClientForm.objects.update_or_create(
                    type=item[0:1],
                    date= datetime.strptime(item[1:9], '%Y%m%d').strftime('%m/%d/%Y'),
                    value=item[9:19],
                    cpf=item[19:30],
                    card=item[30:42],
                    time=item[42:48],
                    hoster=item[48:62],
                    store=item[62:81],
                    name=file,
                    )
            return HttpResponse("File uploaded and processed successfully!!")
    return(request, "index.html", {'fileup': fileup})


