from django.contrib import admin
from django.contrib.auth.models import User

from knigiapp.models import Book, Translator, BookTranslator, Rating, Genre, BookRating


class GenreAdmin(admin.ModelAdmin):
   def has_add_permission(self, request, obj=None):
       if request.user.is_superuser:
           return True
       else:
           return False
   def has_delete_permission(self, request, obj=None):
       if request.user.is_superuser:
           return True
       else:
           return False

class BookAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class RatingInline(admin.TabularInline):
    model = BookRating
    extra = 0

class RatingAdmin(admin.ModelAdmin):
    inlines = [RatingInline, ]
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

admin.site.register(Book, BookAdmin)
admin.site.register(Translator)
admin.site.register(BookTranslator)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Genre, GenreAdmin)

