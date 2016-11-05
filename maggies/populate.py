import os

def populate():
    if not User.objects.filter(username="test").exists():
        super_user = User.objects.create_user('test', 'test@test.com', 'test')
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()

    lung_site = add_cancer_site("Lung")
    booked_nature = add_visit_nature("Booked")
    prediagnosis_stage = add_journey_stage("Pre-Diagnosis")

    add_visitor(isNew=True, gender="M", natureOfVisit=booked_nature)

def add_visitor(isNew, gender, natureOfVisit):
    p = Visitor.objects.get_or_create(is_new_visitor=isNew, gender=gender, nature_of_visit=natureOfVisit)[0]
    return p

def add_cancer_site(name):
    c = CancerSite.objects.get_or_create(name=name)[0]
    return c

def add_visit_nature(nature):
    c = VisitNature.objects.get_or_create(nature=nature)[0]
    return c

def add_journey_stage(stage):
    j = JourneyStage.objects.get_or_create(stage=stage)[0]
    return j

if __name__ == '__main__':
    print("Starting population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maggies.settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    from maggies.models import Visitor, CancerSite, VisitNature, JourneyStage
    from django.contrib.auth.models import User
    from django.conf import settings
    populate()
