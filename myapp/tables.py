import django_tables2 as tables
from .models import Employee
class Employeetable(tables.Table):
    actions=tables.TemplateColumn(template_name="actions.html",orderable=False,empty_values=())
    class Meta:
        model=Employee
        template_name="django_tables2/bootstrap5.html"
        fields=('id','name','gender','email','phone','place','department')
        