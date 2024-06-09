from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from freelance_site.models import Performer, Customer


# Список всех исполнителей
class PerformerListView(ListView):
    model = Performer


# Детальное представление одного исполнителя
class PerformerDetailView(DetailView):
    model = Performer


# Создание нового исполнителя
class PerformerCreateView(LoginRequiredMixin, CreateView):
    model = Performer
    fields = ['name', 'profile_pic', 'mobile', 'email', 'experience']
    success_url = reverse_lazy('performer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PerformerCreateView, self).form_valid(form)


# Создание нового заказчика
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['name', 'profile_pic', 'mobile', 'email']
    success_url = reverse_lazy('performer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CustomerCreateView, self).form_valid(form)


# Обработка входа в систему
@login_required
def handle_login(request):
    if request.user.get_performer() or request.user.get_customer():
        return redirect(reverse_lazy('performer-list'))

    return render(request, 'freelance_site/choose_account.html', {})


# Просмотр профиля пользователя
@login_required
def profile(request):
    if hasattr(request.user, 'performer'):
        return render(request, 'freelance_site/performer_profile.html',
                      {'object': request.user.performer})
    elif hasattr(request.user, 'customer'):
        return render(request, 'freelance_site/customer_profile.html',
                      {'object': request.user.customer})
    else:
        return HttpResponse("No profile found.")
