from .models import Distro

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

class DistroCreate(CreateView):
    model = Distro
    fields = ['nombre']
    success_url = reverse_lazy('distro_lista')
    #def form_valid(self, form):
    #    form.instance.created_by = self.request.user
    #    return super(DistroCreate, self).form_valid(form)

class DistroUpdate(UpdateView):
    model = Distro
    fields = ['nombre']
    success_url = reverse_lazy('distro_lista')

class DistroDelete(DeleteView):
    template_name_field = None
    model = Distro
    success_url = reverse_lazy('distro_lista')

class DistroList(ListView):
    model = Distro
    

