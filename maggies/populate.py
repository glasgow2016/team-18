import os
from datetime import datetime

def populate():
    if not User.objects.filter(username="test").exists():
        super_user = User.objects.create_user('test', 'test@test.com', 'test')
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()

    # Cancer Site values
    lung_site = add_cancer_site("Lung")
    breast_site = add_cancer_site("Breast")
    lowergi_site = add_cancer_site("Lower GI")
    uppergi_site = add_cancer_site("Upper GI")
    braincns_site = add_cancer_site("Brain/CNS")
    prostate_site = add_cancer_site("Prostate")
    headneck_site = add_cancer_site("Head/Neck")
    gynae_site = add_cancer_site("Gynae")
    haemat_site = add_cancer_site("Haemat")
    liver_site = add_cancer_site("Liver")
    pancreatic_site = add_cancer_site("Pancreatic")
    rare_site = add_cancer_site("Rare")
    sarcoma_site = add_cancer_site("Sarcoma")
    skinmel_site = add_cancer_site("Skin/Mel")
    testicular_site = add_cancer_site("Testicular")
    unknown_site = add_cancer_site("Unknown Primary")
    urolog_site = add_cancer_site("Urolog")
    notstated_site = add_cancer_site("Not Stated")

    # Visit Nature values
    booked_nature = add_visit_nature("Booked")
    dropin_nature = add_visit_nature("Drop-In")
    programme_nature = add_visit_nature("Programme")
    telephonesupport_nature = add_visit_nature("Telephone Support")
    emailsupport_nature = add_visit_nature("Email Support")
    fundraising_nature = add_visit_nature("Fundraising")
    outreach_nature = add_visit_nature("Outreach")

    # Journey Stage values
    prediagnosis_stage = add_journey_stage("Pre-Diagnosis")
    curativeintent_stage = add_journey_stage("Curative Intent")
    posttreatement_curativeintent_stage = add_journey_stage("Post Treatment - Curative Intent")
    palliative_stage = add_journey_stage("Palliative Care")
    endoflife_stage = add_journey_stage("End of Life")
    bereaved_stage = add_journey_stage("Bereaved")
    notstated_stage = add_journey_stage("Not Stated")

    # Centre values
    glasgow_centre = add_centre("Glasgow", "10 Dumbarton Road, Glasgow G11 6PA")

    add_pwc(visit_location=glasgow_centre, is_new_visitor=True, gender="M", nature_of_visit=booked_nature, cancer_info=add_cancer_info(sarcoma_site, curativeintent_stage))

def add_pwc(visit_location, is_new_visitor, gender, nature_of_visit, cancer_info):
    v = Visitor.objects.get_or_create(visit_date_time=datetime.now(),
                                        visit_location=visit_location,
                                        is_new_visitor=is_new_visitor,
                                        gender=gender,
                                        nature_of_visit=nature_of_visit)[0]

    p = PwC.objects.get_or_create(visitor=v,
                                        cancer_info=cancer_info)[0]
    return p

def add_carer(visit_location, is_new_visitor, gender, nature_of_visit, pwc_cancer_info, pwc_present, caring_for, relationship):
    v = Visitor.objects.get_or_create(visit_date_time=datetime.now(),
                                        visit_location=visit_location,
                                        is_new_visitor=is_new_visitor,
                                        gender=gender,
                                        nature_of_visit=nature_of_visit)[0]

    p = Carer.objects.get_or_create(visitor=v,
                                        pwc_cancer_info=pwc_cancer_info,
                                        pwc_present=pwc_present,
                                        caring_for=caring_for,
                                        relationship=relationship)[0]
    return p

def add_othervisitor(visit_location, description, is_new_visitor, gender, nature_of_visit):
    v = Visitor.objects.get_or_create(visit_date_time=datetime.now(),
                                        visit_location=visit_location,
                                        is_new_visitor=is_new_visitor,
                                        gender=gender,
                                        nature_of_visit=nature_of_visit)[0]

    p = OtherVisitor.objects.get_or_create(visitor=v,
                                        description=description)[0]
    return p

def add_cancer_info(cancerSite, journeyStage):
    c = CancerInfo.objects.get_or_create(cancer_site=cancerSite,
                                        journey_stage=journeyStage)[0]
    return c

def add_cancer_site(name):
    c = CancerSite.objects.get_or_create(name=name)[0]
    return c

def add_visit_nature(nature):
    c = VisitNature.objects.get_or_create(nature=nature)[0]
    return c

def add_journey_stage(stage):
    j = JourneyStage.objects.get_or_create(stage=stage)[0]
    return j

def add_staff_member(user, first_name, surname, role, work_location, clearance_level, assisted):
    p = StaffMember.objects.get_or_create(user=user,
                                        first_name=first_name,
                                        surname=surname,
                                        role=role,
                                        work_location=work_location,
                                        clearance_level=clearance_level,
                                        assisted=assisted)[0]
    return p

def add_centre(name, address):
    c = Centre.objects.get_or_create(name=name,
                                        address=address)[0]
    return c


if __name__ == '__main__':
    print("Starting population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maggies.settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    from maggies.models import Visitor, CancerSite, VisitNature, JourneyStage, PwC, Carer, OtherVisitor, CancerInfo, Centre
    from django.contrib.auth.models import User
    from django.conf import settings
    populate()
