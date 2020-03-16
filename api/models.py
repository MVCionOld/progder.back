from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Engagement(models.Model):
    STATES_CHOICES = (
        ('RR', 'RECRUITER_REJECTED'),
        ('RA', 'RECRUITER_ACCEPTED'),
        ('CR', 'CANDIDATE_REJECTED'),
        ('CA', 'CANDIDATE_ACCEPTED')
    )
    recruiter = models.ForeignKey(
        'Recruiter',
        on_delete=models.DO_NOTHING
    )
    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.DO_NOTHING
    )
    state = models.CharField(
        max_length=2,
        choices=STATES_CHOICES
    )
    last_change_date = models.DateTimeField(default=datetime.now)

    def change_state(self, new_state):
        self.state = new_state


class Recruiter(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    company_name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        default='StartUp'
    )

    def get_accepted_engagements(self):
        return Engagement.objects \
            .filter(recruiter=self) \
            .filter(state='CA')

    def interview_candidates(self):
        all_candidates = Candidate.objects.all()
        known_candidates_id = Engagement.objects \
            .filter(recruiter=self) \
            .select_related() \
            .values_list('candidate')
        known_candidates = Candidate.objects \
            .filter(user_id__in=known_candidates_id)
        return all_candidates.difference(known_candidates)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.company_name}"


class Candidate(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    personal_info = models.TextField()
    skills_info = models.TextField()
    wishes_info = models.TextField()
    extra_info = models.TextField()
    personal_info_extended = models.TextField()
    skills_info_extended = models.TextField()
    wishes_info_extended = models.TextField()
    extra_info_extended = models.TextField()

    def get_engagements(self):
        return Engagement.objects \
            .filter(candidate=self) \
            .filter(state='RA')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
