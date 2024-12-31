from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404



def index(request):
    """the home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics' : topics} #a dictionary in which the keys are names we'll use in the tamplate to acces the data we want
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id): #Accepts the value captured by /<int:topic_id>/
    topic = Topic.objects.get(id = topic_id) # this is a query, they query the database for specific information.

    # make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added') #the - displays them in reverse order, showing most recently added on top
    context = {'topic': topic, 'entries': entries} # then we store the topic and entry to the context dictionary.
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add new topic"""

    if request.method != 'POST': # OR if request.method == 'GET';
        #no data submitted; creat a blank form
        form = TopicForm()

    else:
        #POST data is submitted; process data
        form = TopicForm(data=request.POST) # give data entered by the user to the TopicForm (empty form)
        if form.is_valid(): #data cant be saved in the database until we check if it was valid
            #is valid checks if all form fields have been filled & that the data types entered matches the required
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save() # after we check and make sure that everything is valid, we save that data
            return redirect('learning_logs:topics') # takes you back to the page associated with topic u submitted, where the user will see the topic they entered in the list of topics
        
    #This will run if reuquest == GET or the form is invalid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)



@login_required
def new_entry(request, topic_id): #gets topic_id from the url.
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) #commit=False, tells Django to create a new form and assign it to new_entry, without saving to the database yet.
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id) #redirects to a view (in this case topic), and def topic needs a topic id, hence we added topic_id = topic_id
        
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)



@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic #.topic comes from the models functions.

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)  #instance tells Django to create the form prefilled with existing entry object.

    else:
        # post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        

    context = {'entry': entry,'topic':topic, 'form':form} #if form is invalid, or the user didn't edit it yet.
    return render(request, 'learning_logs/edit_entry.html', context)

        

def remove_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()

    return redirect('learning_logs:topics')


def remove_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    entry.delete()

    return redirect('learning_logs:topic', topic_id= topic.id)
    