from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from datetime import date


TEMPLATE_DIR = str(settings.BASE_DIR) + '/templates/music_yearbook/'
MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

class MusicYearbookView(TemplateView):
    template_name = TEMPLATE_DIR + 'index.html'
    
    def get_context_data(self, **kwargs):
        """Provide the current year to the index template."""
        context = super().get_context_data(**kwargs)
        context['current_year'] = date.today().year
        return context


class MonthView(TemplateView):
    template_name = TEMPLATE_DIR + 'month.html'

    def get(self, request, *args, **kwargs):
        """Validate year/month from the URL and normalize them to ints.

        If validation fails, raise Http404 so Django's normal handler runs.
        Otherwise put the normalized values back into kwargs so
        get_context_data receives validated ints.
        """
        try:
            year_val = kwargs.get('year')
            month_val = kwargs.get('month')
            if year_val is None or month_val is None:
                raise ValueError
            y = int(year_val)
            m = int(month_val)
        except (TypeError, ValueError):
            raise Http404("Year and month must be integers.")

        if not (2000 <= y <= 2100 and 1 <= m <= 12):
            raise Http404("Invalid year or month.")

        # normalize values for downstream code
        kwargs['year'] = y
        kwargs['month'] = m

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # kwargs come from get(...) and will contain validated ints
        context = super().get_context_data(**kwargs)
        context['year'] = kwargs.get('year')
        context['month'] = kwargs.get('month')
        if context['month'] is not None:
            context['month_name'] = MONTH_NAMES[context['month'] - 1]
        return context