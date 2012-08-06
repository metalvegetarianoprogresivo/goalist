# Create your views here.
from lista.models import Goal, Lista, Usuario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404

def inicio(request):
	listas = Lista.objects.all()
	usuarios = User.objects.all()
	return render_to_response('list_view.html', {'list':listas, 'usuarios':usuarios})

def lista(request, id):
	listas = get_object_or_404(Lista, pk=id)
	goals = Goal.objects.filter(lista=id)
	usuarios = User.objects.all()
	return render_to_response('listas_view.html', {'list':listas, 'goal':goals, 'usuarios':usuarios})

def usuario(request, user):
	usuario = get_object_or_404(User, username=user)
	listas = Lista.objects.filter(usuario=usuario.id)
	user = get_object_or_404(Usuario, user_id=usuario.id)
	usuarios = User.objects.all()
	return render_to_response('user_view.html', {'user':usuario, 'listas':listas, 'usuarios':usuarios, 'user_data':user})