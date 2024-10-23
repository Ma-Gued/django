from django.contrib import admin
from clairmarais.models import VoteOption, Poll

# Administration des VoteOptions

class VoteOptionInline(admin.TabularInline):
    model = VoteOption
    extra = 1
    exclude = ('user', )

    # Permet de filtrer les options de vote en fonction du sondage
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "poll":
            kwargs["queryset"] = Poll.objects.filter(id=request.resolver_match.kwargs.get('object_id'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)