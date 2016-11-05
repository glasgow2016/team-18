import os

def populate():
    lung_site = add_cancer_site("Lung")
    booked_nature = add_visit_nature("Booked")
    prediagnosis_stage = add_journey_stage("Pre-Diagnosis")

    add_visitor(isNew=True, gender="M", cancerSite=lung_site, natureOfVisit=booked_nature)

def add_visitor(isNew, gender, cancerSite, natureOfVisit):
    p = Visitor.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
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
    print "Starting population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maggies.settings')
    from maggies.models import Visitor, CancerSite, VisitNature, JourneyStage
    populate()
