from statistics import mode
from django.shortcuts import redirect, render
from .forms import ChoicesForm
# Create your views here.
import nlpcloud

def getAbstract(request):
    form = ChoicesForm()
    if request.method == 'POST':
        form = ChoicesForm(request.POST)

        if form.is_valid():
            #form.save()
            api_tocken = form.cleaned_data['api_tocken']
            language = form.cleaned_data['language']
            model = form.cleaned_data['model']
            use_gpu = form.cleaned_data['use_gpu']
            inpt_string = form.cleaned_data['inpt_string']
            question = form.cleaned_data['question']
            print('doneeeeeeeeeeeeee')
            ans = getAnswer(api_tocken,language,model,use_gpu,inpt_string,question)
            print(ans)
            return render(request, 'App/index2.html',{'ans':ans['answer'],'score':ans['score'],'start':ans['start'],'end':ans['end']})
        else:
            print('Nooooooooooo')
            return redirect('/')

    context = {'form':form}
    return render(request, 'App/index.html',context)


def getAnswer(api_tocken,language,model,use_gpu,inpt_string,question):
    if language != 'eng':
        client = nlpcloud.Client(model, api_tocken,gpu=False)
    else:
        client = nlpcloud.Client(model, api_tocken,gpu=False)
    return client.question(inpt_string,question)

