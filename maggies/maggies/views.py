from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.forms.formsets import formset_factory
from .forms import VisitorForm, PWC, CARER, OTHER, ActivityForm
from .models import PwC, Carer, OtherVisitor, CancerInfo, Visitor, DailyIdentifier, Activity
from django.http import JsonResponse

from datetime import datetime

@login_required
def home(request):
    ActivityFormSet = formset_factory(ActivityForm)
    if request.method=="POST":
        form = VisitorForm(request.POST)
        activity_formset = ActivityFormSet(request.POST)
        if form.is_valid() and activity_formset.is_valid():
            print("Form is valid.")
            form_has_been_seen_today = form.cleaned_data["has_been_seen_today"]
            form_dailyid_id = form.cleaned_data["dailyid_id"]
            if form_has_been_seen_today:
                # Dont add new visitor stuff.
                # Just update activities
                dailyID = DailyIdentifier.objects.get(pk=form_dailyid_id)
                visitor = dailyID.visitor
                for activity_form in activity_formset:
                    form_activity_name = activity_form.cleaned_data["activity_name"]
                    activity = Activity.objects.get_or_create(name=form_activity_name)[0]
                    activity.participants.add(visitor)
            else:
                form_visitor_name = form.cleaned_data["visitor_name"]
                form_visitor_type = form.cleaned_data["visitor_type"]
                form_is_new_visitor = form.cleaned_data["is_new_visitor"]
                form_visitor_gender = form.cleaned_data["visitor_gender"]
                form_nature_of_visit = form.cleaned_data["nature_of_visit"]
                form_cancer_site = form.cleaned_data["cancer_site"]
                form_journey_stage = form.cleaned_data["journey_stage"]

                print("Form details:",
                        form_visitor_name,
                        form_visitor_type,
                        form_is_new_visitor,
                        form_visitor_gender,
                        form_nature_of_visit,
                        form_cancer_site,
                        form_journey_stage)

                visitor = Visitor.objects.create(
                            visit_date_time = datetime.now(),
                            is_new_visitor = form_is_new_visitor,
                            gender = form_visitor_gender,
                            nature_of_visit = form_nature_of_visit)

                dailyIdentifier = DailyIdentifier.objects.get_or_create(first_name = form_visitor_name,
                                                                        time_first_seen = datetime.now(),
                                                                        visitor = visitor)

                if form_visitor_type == PWC:
                    #create PWC object
                    cancer_info = CancerInfo.objects.create(
                                    cancer_site = form_cancer_site,
                                    journey_stage = form_journey_stage)

                    pwc = PwC.objects.create(
                                    cancer_info = cancer_info,
                                    visitor=visitor)[0]

                elif form_visitor_type == CARER:
                    #create visitor object
                    pwc_cancer_info = CancerInfo.objects.create(
                                    cancer_site = form_cancer_site,
                                    journey_stage = form_journey_stage)

                    #TODO get pwc_present when appropriate
                    carer = Carer.objects.create(
                                    pwc_cancer_info = pwc_cancer_info,
                                    pwc_present = False,
                                    relationship = "FILL ME",
                                    visitor = visitor)

                elif form_visitor_type == OTHER:
                    other = OtherVisitor.objects.create(
                                    description = "FILL ME",
                                    visitor = visitor)


            form = VisitorForm()
            activityFormSet = ActivityFormSet()
            return render(request, "home.html", {"form": form,
                                        "activityFormSet": activityFormSet,
                                        "message": "Successfully submitted."})
        else:
            print("Form is not valid.")

    form = VisitorForm()
    activityFormSet = formset_factory(ActivityForm)
    return render(request, "home.html", {"form": form, "activityFormSet": activityFormSet})

def ajax_check_for_daily_ids(request):
    if request.method == "POST":
        if "visitor_name" in request.POST:
            matching_ids = DailyIdentifier.objects.filter(first_name__icontains = request.POST["visitor_name"])
            print("Found " + str(len(matching_ids)) + " matching ids")
            print( matching_ids)
            dictionaries = [ obj.as_dict() for obj in matching_ids ]
            return JsonResponse({"success": True, "items": dictionaries})
    return JsonResponse({"success": False})

def findChildFromVisitor(visitor):
    matching_pwc = PwC.objects.filter(visitor=visitor)
    if len(matching_pwc) > 0:
        return matching_pwc[0]
    matching_carer = Carer.objects.filter(visitor=visitor)
    if len(matching_carer) > 0:
        return matching_carer[0]
    matching_other = OtherVisitor.objects.filter(visitor=visitor)
    if len(matching_other) > 0:
        return matching_other[0]
    return None


def ajax_get_autofill_details(request):
    if request.method == "POST":
        if "dailyid_id" in request.POST:
            dailyid_id = request.POST["dailyid_id"]
            dailyid_obj = DailyIdentifier.objects.filter(pk=dailyid_id)[0]
            visitor = dailyid_obj.visitor
            visitor_child_instance = findChildFromVisitor(visitor)
            if isinstance(visitor_child_instance, PwC):
                return JsonResponse({"success":True, "type": "PwC",
                    "obj": visitor_child_instance.as_dict()})
            elif isinstance(visitor_child_instance, Carer):
                return JsonResponse({"success":True, "type": "Carer",
                    "obj": visitor_child_instance.as_dict()})
            elif isinstance(visitor_child_instance, OtherVisitor):
                return JsonResponse({"success":True, "type": "OtherVisitor",
                    "obj": visitor_child_instance.as_dict()})
    return JsonResponse({"success":False})



def login_page(request):
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            user = authenticate(username=request.POST["username"],
                                password=request.POST["password"])
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect(request.POST.get('next', '/'))
            else:
                # No backend authenticated the credentials
                context = {"showError": True, "message": "Login Failed - Please try again."}
                return render(request, "login.html", context)
        else:
            print("check failed")
    print("Falling back to basic page")
    return render(request, "login.html")

@login_required
def logout_page(request):
    logout(request)
    return redirect('/')

@login_required
def reports(request):
    return render(request, "reports.html")

@login_required
def recent(request):
    return render(request, "recent.html")

@login_required
def activities(request):
    return render(request, "activities.html")

@login_required
def ajax_report_visitor_count(request):
    if request.method == "POST":
        startDate = datetime.strptime(request.POST['start_date'], '%Y-%m-%d')
        endDate = datetime.strptime(request.POST['end_date'], '%Y-%m-%d')
        allWithinDates = Visitor.objects.filter(visit_date_time__range=(startDate,endDate))
        dictOfDates = {}
        for visitor in allWithinDates:
            curDate = visitor.visit_date_time.date()
            if curDate not in dictOfDates:
                dictOfDates[curDate] = 1
            else:
                dictOfDates[curDate] += 1
        listOfDictOfDates = []
        for date in dictOfDates:
            listOfDictOfDates.append({'date': date, 'count': dictOfDates[date]})

        return JsonResponse({"success": True, "leDates": listOfDictOfDates})
    return JsonResponse({"success": False})
