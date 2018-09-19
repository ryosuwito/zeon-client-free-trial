from django.contrib import admin
from .models import Member, PackageGroup, Staff

class PackageGroupAdmin(admin.ModelAdmin):
    model = PackageGroup

class MemberAdmin(admin.ModelAdmin):
    model = Member
    exclude = ['slug']

class StaffAdmin(admin.ModelAdmin):
    model = Staff
    exclude = ['slug']

admin.site.register(PackageGroup, PackageGroupAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Staff, StaffAdmin)