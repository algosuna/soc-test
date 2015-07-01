from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
    FormView, ListView, UpdateView, DetailView, DeleteView
)

from .models import Contact
from .forms import UploadForm, ContactUpdateForm


class UploadView(FormView):
    template_name = 'upload.html'
    form_class = UploadForm
    success_url = reverse_lazy('contactmgr:contact_list')

    def form_valid(self, form):
        form.save()
        return super(UploadView, self).form_valid(form)


class ContactList(ListView):
    model = Contact
    paginate_by = 20
    template_name = 'list.html'
    context_object_name = 'contacts'
    queryset = model.objects.order_by('name')


class ContactDetail(DetailView):
    model = Contact
    template_name = 'detail.html'


class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactUpdateForm
    template_name = 'update.html'

    def get_success_url(self):
        return reverse('contactmgr:contact_detail', args=[self.object.id])


class ContactDelete(DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = reverse_lazy('contactmgr:contact_list')
