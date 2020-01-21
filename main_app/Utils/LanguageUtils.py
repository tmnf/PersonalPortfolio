def get_base_words(request):
    if request.session['lang'] == 'en':
        main_page = 'Home Page'
        curr_job = 'Computer Science Student'
        home = 'Home'
        porfolio = 'Portfolio'
        skills = 'Technical Skills'
        contacts = 'Contacts'
        contact = 'Contact'
        attachments = 'Attachments'
        name = 'Name'
        contact_email = 'Email Contact'
        subject = 'Subject'
        message = 'Message'
        send = 'Send'
        references = 'References'
        languages_text = 'Programming Languages'
        spoken_languages_text = 'Spoken Languages'
        other_skills_text = 'Other Skills'
        phone_text = 'Phone'
    else:
        main_page = 'Página Inicial'
        curr_job = 'Estudante de Engenharia Informática'
        home = 'Início'
        porfolio = 'Portfólio'
        skills = 'Competências Técnicas'
        contacts = 'Contactos'
        contact = 'Contacto'
        attachments = 'Anexos'
        name = 'Nome'
        contact_email = 'Contacto de Email'
        subject = 'Assunto'
        message = 'Mensagem'
        send = 'Enviar'
        references = 'Referências'
        languages_text = 'Linguagens de Programação'
        spoken_languages_text = 'Idiomas Falados'
        other_skills_text = 'Outras Competências'
        phone_text = 'Telemóvel'

    return {"main_page": main_page, "curr_job": curr_job, "home": home, "portfolio": porfolio, "skills": skills,
            "contacts": contacts,
            "contact": contact, "attachments": attachments, "name": name, "contact_email": contact_email,
            "subject": subject, "message": message, "send": send, "references": references,
            "languages_text": languages_text,
            "other_skills_text": other_skills_text, "phone_text": phone_text,
            "spoken_languages_text": spoken_languages_text}
