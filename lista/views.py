# Create your views here.
from lista.models import Goal, Lista
from follow.models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from sorl.thumbnail import get_thumbnail
from django.conf import settings

def inicio(request):
	listas = Lista.objects.all()
	usuarios = User.objects.all()
	return render_to_response('list_view.html', {'list':listas, 'usuarios':usuarios})

def lista(request, id):
	listas = get_object_or_404(Lista, pk=id)
	usuario = Profile.objects.get(user_id=listas.usuario)
	return render_to_response('listas_view.html', {'list':listas, 'usuario':usuario})

def usuario(request, user):
	usuario = get_object_or_404(User, username=user)
	listas = Lista.objects.filter(usuario=usuario.id)
	user = get_object_or_404(Profile, user=usuario.id)
	followers = Profile.objects.filter(follows=Profile.objects.get(user=usuario.id))
	im = get_thumbnail(user.avatar.url, '150x150', crop='center', quality=99)
	return render_to_response('user_view.html', {'user':usuario, 'listas':listas, 'user_data':user, 'avatar':im, 'followers':followers,})

def goal(request, id):
	goal = get_object_or_404(Goal, pk=id)
	listas = Lista.objects.filter(goals=Goal.objects.get(pk=id))
	usuarios = Profile.objects.filter(user__in=Lista.objects.filter(goals=Goal.objects.get(pk=id)))
	return render_to_response('goal_view.html', {'goal':goal, 'listas':listas, 'usuarios':usuarios})