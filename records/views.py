from django.views.generic import TemplateView, CreateView
from .models import Owner, Vehicle
from .forms import OwnerForm, VehicleForm, RecognitionForm
from django.urls import reverse_lazy
from django.views.generic import FormView

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        number_of_vehicle = Vehicle.objects.count()
        clean_vehicles = Vehicle.objects.filter(status='Clean').count()
        dept_vehicles = Vehicle.objects.filter(status='Dept').count()

        dept_percentage = round((dept_vehicles / number_of_vehicle) * 100, 1)
        clean_percentage = round((clean_vehicles / number_of_vehicle) * 100, 1)

        context['number_of_vehicle'] = number_of_vehicle
        context['clean_vehicles'] = clean_vehicles
        context['dept_vehicles'] = dept_vehicles
        context['dept_percentage'] = dept_percentage
        context['clean_percentage'] = clean_percentage
        context['vehicles'] = Vehicle.objects.all()
        return context


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner_form.html'
    success_url = reverse_lazy('dashboard')


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy("dashboard")


class PlateNumberRecognitionView(FormView):
    template_name = 'recognition.html'
    form_class = RecognitionForm
    success_url = reverse_lazy('recognition')
    
    def form_valid(self, form):
        license_plate_image = form.cleaned_data['license_plate']
        # Process the image here, for example, save it to a directory and display it
        print(license_plate_image)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
