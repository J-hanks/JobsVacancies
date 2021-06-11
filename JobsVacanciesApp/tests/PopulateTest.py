from django.test import TestCase

from JobsVacanciesApp.populateDatabaseWithModelMommy import  populateDatabaseWithModelMommy
from JobsVacanciesApp.models import JobApplication, JobVacancy

class PopulateTest(TestCase):
    def setUp(self):
        populateDatabaseWithModelMommy()

    def test_populate(self):

        self.assertGreaterEqual(JobApplication.objects.all().count(), 20)
        self.assertGreaterEqual(JobVacancy.objects.all().count(), 20)
