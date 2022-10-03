from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from .forms import DeepThoughtForm
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, DeepThought
# is this necessary?


from django.utils import timezone

# home view for when you open the page. Should have some buttons on there to lead you places around the site.
def homeView(request):
    return render(request, "polls/homeview.html")

#super basic view to show each deepthought polls/deepthought/<id:pk>
def viewDeepThought(request, DeepThought_id):
        d = DeepThought.objects.filter(id=DeepThought_id)
        print(d)
        
        # Check if you get the value
        return HttpResponse(d)
    

# super basic function to just show a list of all the deep thoughts in /polls/deepthoughts/list
def detail(request):

    deep_thought_list = DeepThought.objects.all()
    output = HttpResponse()
    output.write("Here is a list of DeepThoughts submitted!")
    output.write("<br>")
    for d in deep_thought_list:
        myTitle = d.title
        myThought = d.thought
        output.write("Title: ")
        output.write(myTitle)
        output.write(" Thought: ")
        output.write(myThought)
        output.write("<br>")
        
    return HttpResponse(output)

# some view for the user to input a new deepthought at /polls/deepthoughts
def SubmitDeepThought(request):
    context ={}
 
    # create object of form
    form = DeepThoughtForm(request.POST or None, request.FILES or None)
    context['form']= form
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return render(request, "polls/thanks.html")

    else:
        return render(request, "polls/name.html", context)




class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))