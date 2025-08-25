from django.contrib import admin
from .models import Guardian, FamilyMember

@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    list_display = ("name", "village", "mobile_number")
    search_fields = ("name", "village", "mobile_number")
    list_filter = ("village",)

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile_number", "is_guardian", "guardian", "medical_condition")
    list_filter = ("is_guardian", "guardian__village")
    search_fields = ("name", "mobile_number", "medical_condition")
