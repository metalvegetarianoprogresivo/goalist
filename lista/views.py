# Create your views here.
from lista.models import Goal, Lista
from follow.models import Profile
from lista.forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from sorl.thumbnail import get_thumbnail
from django.conf import settings, urls
from django.template import RequestContext

def inicio(request):
	listas = Lista.objects.all()
	usuarios = Profile.objects.all()
	return render_to_response('list_view.html', {'list':listas, 'usuarios':usuarios,})

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

def search(request):
	s = request.GET.get('s')
	if s == '':
		# No busca
		search = {}
		usuarios = {}
	else:
		# Busca
		search = Goal.objects.filter(nombre__icontains=s)
		usuarios = Profile.objects.filter(user__in=Lista.objects.filter(goals__in=search))
	return render_to_response('search_view.html', {'goals':search, 'keyword':s, 'usuarios':usuarios,})

def register(request):
	# Vista de registro de usuarios.
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			mail = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(username, mail, password)
			user.save()
			return HttpResponseRedirect('/register/'+username)
	else:
		form = RegisterForm()
	return render_to_response('register_view.html', {'form':form,}, context_instance=RequestContext(request))

def registerProfile(request, username):
	try:
		usuario = User.objects.get(username=username)
	except Exception, e:
		return HttpResponseRedirect('/register')
	try:
		perfil = Profile.objects.get(user=usuario.id)
		return HttpResponseRedirect('/'+username)
	except Exception, e:
		if request.method == 'POST':
			form = ProfileForm(request.POST, request.FILES)
			if form.is_valid():
				bio = form.cleaned_data['bio']
				place = form.cleaned_data['place']
				website = form.cleaned_data['website']
				profile = Profile(user=usuario, bio=bio, ubicacion=place, website=website, avatar=request.FILES['avatar'])
				profile.save()
				return HttpResponseRedirect('/'+username)
		else:
			form = ProfileForm()
	return render_to_response('registerprofile_view.html', {'form':form, 'user':usuario}, context_instance=RequestContext(request))