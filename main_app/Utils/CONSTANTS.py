EMAIL = 0
PHONE = 1
LINKEDIN = 2
GITHUB = 3

def GetName(contact_type):
    if contact_type == EMAIL:
        return "Email"
    if contact_type == PHONE:
        return "Phone"
    if contact_type == LINKEDIN:
        return "LinkedIn"
    if contact_type == GITHUB:
        return "GitHub"
