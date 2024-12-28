Simplest way to build a form in Django is to use a ModelForm, which uses information from the models we defined in models.py to build a form automatically. Should be in the same directory as models.py

```
class TopicForm(forms.ModelForm):
		class Meta:
			model = Topic
			fields = ['text']
			labels = ['text':'']

```

***Creating anything Django***:
	1- make model/form
	2- make url in urls.py
	3- create view function

	The model is the empty skeleton (ex. empty text field), then the url is created to call the views function and the views function is what calls the model and puts the data in it.


***Creating form template***:
	<form> defines an HTML form.
	 the *action* argument tells the browser where to send the data submitted in the form, in this case (new_topic.html), we send it to the view function new_topic(). And then the method = 'post' tells it to save the data as a POST request. 

In this case the view function has to handle two situations: initial requests for the new_topic page, so it should show a blank form; and the processing of data after it was submitted in the form.


==Creating a Views function for adding new topic==

```
 <!-- def new_topic(request):
    """Add new topic"""

    if request.method != 'POST': # OR if request.method == 'GET';
        #no data submitted; creat a blank form
        form = TopicForm()

    else:
        #POST data is submitted; process data
        form = TopicForm(data=request.POST) # give data entered by the user to the TopicForm (empty form)
        if form.is_valid(): #data cant be saved in the database until we check if it was valid
            #is valid checks if all form fields have been filled & that the data types entered matches the required
            form.save() # after we check and make sure that everything is valid, we save that data
            return redirect('learning_logs:topics') # takes you back to the page associated with topic u submitted, where the user will see the topic they entered in the list of topics
        
    #This will run if reuquest == GET or the form is invalid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context) -->

```


<!-- {{ }} is used to output data 
        {% %} is used for logic and actions-->

