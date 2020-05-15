from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.shortcuts import render, redirect

from main_app.models import Contact, Project, Profile, File, Languages, Frameworks, OtherSkills, SpokenLanguage, \
    Download
from .Utils import CONSTANTS, EmailUtils
from .Utils import LanguageUtils


def index(request):
    check_language(request)

    profile = Profile.objects.get(pk=1)

    birth = date(profile.birthday.year, profile.birthday.month, profile.birthday.day)
    age = relativedelta(date.today(), birth).years

    info = {"profile": profile,
            "age": age,
            "active": "home",
            "files": File.objects.all(),
            "spoken_languages": SpokenLanguage.objects.all()
            }

    info = {**info, **LanguageUtils.get_base_words(request)}

    return render(request, "index.html", info)


def check_language(request):
    try:
        request.session['lang']
    except KeyError:
        request.session['lang'] = 'pt'


def change_lang(request):
    check_language(request)

    if request.session['lang'] == 'pt':
        request.session['lang'] = 'en'
        messages.success(request, "Some texts might be in another language...")
    else:
        request.session['lang'] = 'pt'

    return redirect('home_view')


def send_email(request):
    check_language(request)

    name = request.POST.get('name')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = request.POST.get('email')

    if subject and message and from_email and name:
        try:
            EmailUtils.send_message(name, from_email, subject, message)
            messages.success(request, 'Mensagem Enviada com Sucesso!')
        except:
            messages.error(request, 'Erro ao Enviar a Mensagem')

        return redirect('home_view')

    messages.error(request, 'Campos Vazios')
    return redirect('home_view')


def contacts(request):
    check_language(request)
    conts = {
        "email": Contact.objects.get(contact_type=CONSTANTS.EMAIL).contact_info,
        "phone": Contact.objects.get(contact_type=CONSTANTS.PHONE).contact_info,
        "linkedin": Contact.objects.get(contact_type=CONSTANTS.LINKEDIN).contact_info,
        "github": Contact.objects.get(contact_type=CONSTANTS.GITHUB).contact_info,
        "active": "contacts"
    }

    conts = {**conts, **LanguageUtils.get_base_words(request)}

    return render(request, "contacts.html", conts)


def skills(request):
    check_language(request)

    skill_list = {"languages": Languages.objects.all().order_by('priority'),
                  "frameworks": Frameworks.objects.all().order_by('priority'),
                  "other_skills": OtherSkills.objects.all().order_by('priority'),
                  "active": "skills",
                  }

    skill_list = {**skill_list, **LanguageUtils.get_base_words(request)}

    return render(request, "skills.html", skill_list)


def downloads(request):
    check_language(request)

    downs = Download.objects.all()

    return render(request, "downloads.html",
                  {'active': 'downloads', 'downloads': downs, **LanguageUtils.get_base_words(request)})


def portfolio(request):
    check_language(request)
    projects = {
        "projects": Project.objects.all().order_by('priority'),
        "active": "portfolio"
    }

    projects = {**projects, **LanguageUtils.get_base_words(request)}

    return render(request, "portfolio.html", projects)


def project(request, title=""):
    check_language(request)
    projects = {
        "proj": Project.objects.get(project_name=title),
        "active": "portfolio"
    }

    projects = {**projects, **LanguageUtils.get_base_words(request)}

    return render(request, "project.html", projects)
