
# print("Welcome to the special recruitment program, please answer the following questions:")

# name = input("What's your name ? ")
# print(name)

# age = input("How old are you ? ")
# print(age)




def get_skills():
    return ["1.\tPython", "2.\tC++", "3.\tJavascript", "4.\tJuggling", "5.\tRunning", "6.\tEating"]
def show_skills(skills):
    for skill in skills:
        print(skill)
def get_uer_skills(skills):
    skill1 = eval(input("\nChoose a skill from above by entering its number: "))
    skill2 = eval(input("Choose another skill from above by entering its number: "))
    return [skills[skill1 - 1], skills[skill1 - 2]]

def get_user_cv(skills):
    cv = {}
    name = input("What's your name? ")
    age = eval(input("How ald are you? "))
    experience = eval(input("How many years of experience do you have? "))
    cv["name"] = name
    cv["age"] = age
    cv["experience"] = experience
    print("Skills:")
    show_skills(skills)
    cv["skills"] = get_uer_skills(skills)
    return cv


def check_acceptance(cv, desired_skill):
    if cv["age"] > 25 and cv["age"] < 40 and cv["experience"] > 3:
        for skill in cv["skills"]:
            if skill not in desired_skill:
                return False
        return True
    else:
        return False
def main():
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    cv = get_user_cv(skills)
    if check_acceptance(cv, skills[2]):
        print("You have been accepted, ", cv["name"], ".")
    else:
        print("You have been rejected, ", cv["name"], ".")
if __name__ == "__main__":
    main()

