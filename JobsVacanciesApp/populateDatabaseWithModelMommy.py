from JobsVacanciesApp.models import Company, JobVacancy, JobApplication
from model_mommy import mommy
import pytz
from faker import Faker


	
# seed the pseudorandom number generator
from random import seed
from random import randint


def populateDatabaseWithModelMommy():
    faker = Faker()
    company_counter =0
    vacancy_counter =0
    application_counter =0
    for lp in range(randint(5,15)):
        company = mommy.make(Company, name=faker.company())
        company.save()
        company_counter = company_counter + 1
        for lp in range(randint(3,10)):
            vacancy_date = faker.date_time_between(
                start_date='-3y',
                end_date='now',
                tzinfo=pytz.UTC
            )
            vacancy = mommy.make(
                JobVacancy,
                name=faker.job(),
                company=company,
                requisites=faker.text(max_nb_chars=255)
            )
            vacancy.save()
            vacancy.create_date=vacancy_date
            vacancy.save()
            vacancy_counter = vacancy_counter + 1

            for lp in range(randint(0,5)):
                application_date = faker.date_time_between(
                    start_date=vacancy_date,
                    end_date='-1m',
                    tzinfo=pytz.UTC
                )
                application = mommy.make(JobApplication, job_vacancy=vacancy)
                application.save()
                application.create_date=application_date
                application.save()
                application_counter = application_counter + 1
    
    print(f"Created:")
    print(f"\t{company_counter} Companies")
    print(f"\t{vacancy_counter} Vacancies")
    print(f"\t{application_counter} Applications")
            



