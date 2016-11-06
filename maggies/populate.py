import os
from datetime import datetime, timedelta
from random import choice

def populate():
    if not User.objects.filter(username="test").exists():
        super_user = User.objects.create_user('test', 'test@test.com', 'test')
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()

    # Some datetimes
    now_datetime = datetime.now()
    yesterday_datetime = now_datetime - timedelta(days=-3)
    last_week_datetime = now_datetime - timedelta(days=-7)
    last_month_datetime = now_datetime - timedelta(days=-30)
    half_a_year_ago_datetime = now_datetime - timedelta(days=-364/2)
    one_year_ago_datetime = now_datetime - timedelta(days=-365)

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
    london_centre = add_centre("London", "3, Thames Wharf, Rainville Rd, London W6 9HA")

    # Activities
    yoga = add_activity("Yoga", [], [], [])

    datetimes = [now_datetime, yesterday_datetime, last_week_datetime, last_month_datetime, half_a_year_ago_datetime, one_year_ago_datetime]
    centres = [glasgow_centre, london_centre]
    news = [0,1]
    genders = ["M", "F"]
    natures = [booked_nature, dropin_nature, programme_nature, telephonesupport_nature,
                emailsupport_nature, fundraising_nature, outreach_nature]
    sites = [lung_site, breast_site, lowergi_site, uppergi_site, braincns_site, prostate_site, headneck_site,
                gynae_site, haemat_site, liver_site, pancreatic_site, rare_site, sarcoma_site, skinmel_site, testicular_site,
                unknown_site, urolog_site, notstated_site]
    stages = [prediagnosis_stage, curativeintent_stage, posttreatement_curativeintent_stage, palliative_stage,
                endoflife_stage, bereaved_stage, notstated_stage]

    #add_pwc(visit_location=glasgow_centre, is_new_visitor=True, gender="M", nature_of_visit=booked_nature, cancer_info=add_cancer_info(sarcoma_site, curativeintent_stage))
    random_pwcs(10, datetimes, centres, news, genders, natures, sites, stages)


    bob_pwc = add_pwc(visit_location=glasgow_centre, is_new_visitor=True, gender="M", nature_of_visit=booked_nature, cancer_info=add_cancer_info(sarcoma_site, curativeintent_stage))

    add_daily_identifier("Bob", datetime.now(), visitor=bob_pwc.visitor)

    elizabeth_pwc = add_pwc(visit_location=glasgow_centre, is_new_visitor=True, gender="F", nature_of_visit=booked_nature, cancer_info=add_cancer_info(testicular_site, endoflife_stage))

    add_daily_identifier("Elizabeth", datetime.now(), visitor=elizabeth_pwc.visitor)

    billy_pwc = add_pwc(visit_location=glasgow_centre, is_new_visitor=True, gender="M", nature_of_visit=booked_nature, cancer_info=add_cancer_info(sarcoma_site, curativeintent_stage))

    add_daily_identifier("Billy", datetime.now(), visitor=billy_pwc.visitor)


def random_pwcs(n, datetimes, centres, news, genders, natures, sites, stages):
    for i in range(0,n):
        rCentre = choice(centres)
        rNew = choice(news)
        rGender = choice(genders)
        rNature = choice(natures)
        rSite = choice(sites)
        rStage = choice(stages)
        add_pwc(visit_location=rCentre, is_new_visitor=rNew, gender=rGender, nature_of_visit=rNature, cancer_info=add_cancer_info(rSite, rStage))

def add_daily_identifier(first_name, time_first_seen, visitor):
    d = DailyIdentifier.objects.get_or_create(first_name=first_name,
                                            time_first_seen=time_first_seen,
                                            visitor=visitor)
    return d

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

def add_activity(name, locations, participants, coordinators):
    a = Activity.objects.get_or_create(name=name)[0]

    for location in locations:
        a.location.add(locations)

    for participant in participants:
        a.participants.add(participant)

    for coordinator in coordinators:
        a.coordinators.add(coordinator)

    a.save()

    return a


if __name__ == '__main__':
    print("Starting population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maggies.settings')
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    from maggies.models import Visitor, CancerSite, VisitNature, JourneyStage, PwC, Carer, OtherVisitor, CancerInfo, Centre, DailyIdentifier, Activity
    from django.contrib.auth.models import User
    from django.conf import settings
    populate()
