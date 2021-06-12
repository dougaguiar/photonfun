import django_tables2 as tables
import itertools
from .models import Profile


class PlayerTable(tables.Table):
    row_number = tables.Column(empty_values=(), verbose_name='Rank')

    class Meta:
        model = Profile
        template_name = "django_tables2/bootstrap4.html"
        fields = ('row_number', 'user', 'single_points')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return "%d" % (next(self.counter)+1)


