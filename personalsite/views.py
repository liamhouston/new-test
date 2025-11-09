from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from music_yearbook.forms import SignupForm

class IndexView(TemplateView):
    template_name = 'personalsite/index.html'

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = '/accounts/login/'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        response = super().form_valid(form)
        return redirect(self.get_success_url())

class CustomLoginView(LoginView):
    """Custom login view that redirects to the user's stream page after login"""
    def get_success_url(self):
        # Redirect to the user's own stream page after successful login
        from django.urls import reverse
        # After successful login, redirect to the current user's stream
        if self.request.user.is_authenticated:
            return reverse('music_yearbook:user_index', kwargs={'id': self.request.user.pk})
        # Fallback if user is somehow not authenticated
        return super().get_success_url()
     
    def get(self, request, *args, **kwargs):
        """If user is already authenticated, redirect to their stream"""
        if request.user.is_authenticated:
            from django.urls import reverse
            return redirect(reverse('music_yearbook:user_index', kwargs={'id': request.user.pk}))
        return super().get(request, *args, **kwargs)