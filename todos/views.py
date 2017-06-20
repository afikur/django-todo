from django.shortcuts import render, redirect
from .models import Todo

def index(request):
	todos = Todo.objects.all()[:10]
	context = {
		'todos': todos
	}
	return render(request, 'index.html', context)


def details(request, todo_id):
	todo = Todo.objects.get(id = todo_id)
	context = {
		'todo':todo
	}
	return render(request, 'details.html', context)


def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		body = request.POST['body']

		todo = Todo(title = title, body = body)
		todo.save()
		return redirect('/todos')
	else:
		return render(request, 'add.html')
