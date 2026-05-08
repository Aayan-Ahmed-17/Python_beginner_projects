name = input("Enter Your First Name: ").strip().title().replace(" ", "")
profession = input("Enter Your Profession: ").strip().title().replace(" ", "")
keyword = input("Enter Keyword Here: ").strip().upper().replace(" ", "")


def generate_names(name, keyword=None, profession=None):
    """Generates multiple names for linkedin account

    Args:
        name (str): for eg: "Hamza"
        profession (str): for eg:  "Developer
        keyword (str): for eg: "AI"
    """
    "if vars empty or none"
    keyword = keyword or "AI"
    profession = profession or "Developer"
    
    usernames = []

    """
    Pattern 1 — Name + Profession
    Pattern 2 — Name + Keyword
    Pattern 3 — “The” + Name
    Pattern 4 — Dots
    Pattern 5 — Underscores
    """

    usernames.append(name + profession)
    usernames.append(name + keyword)
    usernames.append("The" + name + "Coder")
    usernames.append(name + ".dev")
    usernames.append(name + "_" + keyword)

    print(usernames)


generate_names(name=name, keyword=keyword, profession=profession)
