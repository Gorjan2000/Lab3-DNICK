from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from Lab3.models import Blog, BlogUser, Komentari, Blokiran


class BlogUserAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and obj.user != request.user:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user != request.user:
            return False
        else:
            return True

    def has_view_or_change_permission(self, request, obj=None):
        if obj and obj.user != request.user:
            return False
        else:
            return True


class KomentarAdmin(admin.ModelAdmin):
    readonly_fields = ("komentator", "blog", "komentar",)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and obj.komentator.user != request.user:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.komentator.user != request.user:
            return False
        else:
            return True


class KomentarInline(admin.StackedInline):
    model = Komentari
    extra = 0


class BlogAdmin(admin.ModelAdmin):
    list_filter = (("datumKreiranje", DateRangeFilter),)
    list_display = ("naslov", "avtor")
    search_fields = ("naslov", "sodrzhina")
    inlines = [KomentarInline, ]
    exclude = ("avtor",)

    def save_model(self, request, obj, form, change):
        avtor = BlogUser.objects.get(user=request.user)
        if avtor:
            obj.avtor = avtor
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.avtor.user != request.user:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if obj and obj.avtor.user != request.user:
            return False
        else:
            return True

    def has_view_permission(self, request, obj=None):
        if obj:
            avtor = obj.avtor.user
            bloknat = request.user
            if Blokiran.objects.filter(blokiran=bloknat, bloker=avtor):
                return False
            else:
                return True


class BlokiranAdmin(admin.ModelAdmin):
    list_display = ("bloker", "blokiran")

    exclude = ("bloker",)

    def save_model(self, request, obj, form, change):
        bloker = BlogUser.objects.get(user=request.user)
        if bloker:
            obj.bloker = bloker
        super().save_model(request, obj, form, change)


admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Komentari, KomentarAdmin)
admin.site.register(Blokiran, BlokiranAdmin)
