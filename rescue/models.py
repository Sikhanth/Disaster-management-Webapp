from django.db import models
from django.db.models import Q

class Guardian(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    village = models.CharField(max_length=100, db_index=True)  # area filter
    map_link = models.URLField(blank=True, null=True)
    mobile_number = models.CharField(max_length=15, unique=True)  # contact for lookup

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.village})"


class FamilyMember(models.Model):
    guardian = models.ForeignKey(
        Guardian, on_delete=models.CASCADE, related_name="members"
    )
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    medical_condition = models.CharField(max_length=255, blank=True, null=True)
    is_guardian = models.BooleanField(default=False)  # ✅ marks if this person is the guardian

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # allow only one guardian member per Guardian (optional but recommended)
        constraints = [
            models.UniqueConstraint(
                fields=["guardian"],
                condition=Q(is_guardian=True),
                name="unique_guardian_member_per_guardian",
            )
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["mobile_number"]),
        ]

    def __str__(self):
        tag = "Guardian" if self.is_guardian else "Member"
        return f"{self.name} — {tag}"
