
from django.contrib import admin
# Register your models here.
from .models import Person, Award
from import_export.admin import ImportExportModelAdmin
from import_export import resources

def clear_isdone(modeladmin, request, queryset):
    queryset.update(is_done=False)
    for award in queryset:
     	award.person_set.clear()

clear_isdone.short_description = "Clear selected awards' winner"


class PersonResource(resources.ModelResource):
	class Meta:
		model = Person
		skip_unchanged =True
		report_skipped = True
		exclude = ('id',)
		import_id_fields = ('person_id',)

class AwardResource(resources.ModelResource):
	class Meta:
		model = Award
		skip_unchanged =True
		report_skipped = True
		exclude = ('id',)
		import_id_fields = ('award_id',)




#admin.site.register(Person)
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
	resource_class = PersonResource
	list_display = ['person_id','employee_id','name','company', 'department', 'seniority', 'is_attend','show_awards_id']
	search_fields = ('person_id','employee_id', 'name', 'company', 'department', )
	def show_awards_id(self, obj):
		return "\n".join([str(a.award_id) for a in obj.award.all()])


class PersonInline(admin.StackedInline):
    model = Person.award.through
    extra = 1


#admin.site.register(Award)
@admin.register(Award)
class AwardAdmin(ImportExportModelAdmin):
	resource_class = AwardResource
	list_display = ['award_id','award_name', 'award_content','award_amount','first_selection','is_done','show_person']
	ordering = ['award_id']
	inlines = [PersonInline]
	actions = [clear_isdone]
	def show_person(self, obj):
		return "\n".join([str(p.name) for p in obj.person_set.all()])

