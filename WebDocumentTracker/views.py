from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from WebDocumentTracker.forms import LoginForm, EditProfileForm
from WebDocumentTracker.models import Profile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from WebDocumentTracker.forms import ProfileForm, EditProfileForm
class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'WebDocumentTracker/login.html'
    extra_context = {'title': 'Авторизация на сайте'}
    def get_success_url(self):
        return reverse_lazy('home')

# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'WebDocumentTracker/user_profile.html'
#
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context
def userpage(request):
	user_form = EditProfileForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="WebDocumentTracker/user_profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })

class CreateProfilePageView(CreateView):
    model = Profile

    template_name = 'WebDocumentTracker/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'WebDocumentTracker/edit_profile.html'
    success_url = reverse_lazy('tasks')

    def get_object(self):
        return self.request.user
def about(request):
    phones = (
        {'phone': '8(914) 141-56-98', 'state' : 'програмист'},
        {'phone': '8(914) 487-31-10', 'state' : 'администратор сайта'}
    )
    data = {'phones' : phones}
    return render(request, 'WebDocumentTracker/about.html', data)


def index(request):
    data = {
    }
    return render(request, 'WebDocumentTracker/index.html', data)
