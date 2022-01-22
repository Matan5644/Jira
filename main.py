from jira import JIRA

projects = ["QC", "WIMG", "OPES"]

ops = {
    "Alignment": {"Anastasiia Rodak": ["anrod@ciklum.com", ""],
                  "Daryna Vozdihan": ["dvoz@ciklum.com", ""],
                  "Liliia Zadorozhna": ["liz@ciklum.com", ""],
                  "Natalia Didych": ["ndi@ciklum.com", ""],
                  "Oksana Levchenko": ["oksl@ciklum.com", ""],
                  "Yulia Krupa": ["yukru@ciklum.com", ""]},

    "Final_Review": {"Andrii Mandolina": ["anman@ciklum.com", ""],
                     "Iryna Kachmar": ["ikac@ciklum.com", ""],
                     "Iryna Kolida": ["ikol@ciklum.com", ""],
                     "Oleksandr Kukharchuk": ["okuk@ciklum.com", ""],
                     "Rostyslav Hasiuk": ["rhas@ciklum.com", ""],
                     "Yaryna Tkachyk": ["yatk@ciklum.com", ""]},

    "Index": {"Anastasiia Movchan": ["amov@ciklum.com", ""],
              "Anastasiia Shelkeyeva": ["ashel@ciklum.com", ""],
              "Dmytro Husakivskyi": ["dhus@ciklum.com", ""],
              "Inna Pas": ["inp@ciklum.com", ""],
              "Iryna Bolyukh": ["irbo@ciklum.com", ""],
              "Kateryna Hulchuk": ["khul@ciklum.com", ""],
              "Oksana Puchynska": ["okpu@ciklum.com", ""],
              "Olena Frankiv": ["ofr@ciklum.com", ""],
              "Tetiana Iarmoliuk": ["teia@ciklum.com", ""],
              "Valeriia Feshchenko": ["vafe@ciklum.com", ""]},

    "Labeling": {"Alisa Dobrovolska": ["aldob@ciklum.com", ""],
                 "Tetyana Tananayska": ["tta@ciklum.com", ""],
                 "Tetyana Tkachenko": ["ttka@ciklum.com", ""],
                 "Yuriy Bilyk ": ["yubil@ciklum.com", ""]},

    "Newcomers": {"Lidiia Fedorova": ["life@ciklum.com", ""],
                  "Olena Shkarpinets": ["olshk@ciklum.com", ""],
                  "Rostyslav Barabash": ["rbar@ciklum.com", ""],
                  "Tetiana Petriv": ["tatp@ciklum.com", ""],
                  "Uliana Komiakovych": ["uko@ciklum.com", ""]},

    "Refining": {"Andrii Nikolaiev": ["annik@ciklum.com", ""],
                 "Dmytro Bushtyn": ["dmbus@ciklum.com", ""],
                 "Khrystyna Marynovych": ["khrm@ciklum.com", ""],
                 "Lyubomyra Klymkovych": ["lykl@ciklum.com", ""],
                 "Oksana Moravska": ["oxm@ciklum.com", ""]},

    "Review_Reports": {"Inna Burlaka": ["inbu@ciklum.com", ""],
                       "Khrystyna Tsebak": ["khts@ciklum.com", ""],
                       "Lev Kuts": ["leku@ciklum.com", ""],
                       "Volodymyr Ploshchanskyi": ["vopl@ciklum.com", ""]},

    "Scoring": {"Alina Tsaruk": ["altsa@ciklum.com", ""],
                "Anastasiia Kauta": ["akau@ciklum.com", ""],
                "Anastasiya Ilnytska": ["anil@ciklum.com", ""],
                "Andrii Ilchyshyn": ["ailc@ciklum.com", ""],
                "Nazar Khibeba": ["khn@ciklum.com", ""],
                "Olga Kuzmyn": ["olgku@ciklum.com", ""],
                "Olga Martyniuk": ["olgma@ciklum.com", ""],
                "Sofia Kalanchova": ["soka@ciklum.com", ""],
                "Solomiia Zakharchyn": ["soza@ciklum.com", ""],
                "Vasyl Panko": ["vapan@ciklum.com", ""]},

    "Scoring_Diagnosis": {"Ivan Batiuchok": ["ibat@ciklum.com", ""],
                          "Kateryna Lys": ["klys@ciklum.com", ""],
                          "Marta Susulovska": ["msus@ciklum.com", ""],
                          "Olga Zhelem": ["olgz@ciklum.com", ""]},

    "Touchups": {"Hanna Ellanska": ["hel@ciklum.com", ""],
                 "Kateryna Buriak": ["kabu@ciklum.com", ""],
                 "Mariana Mrii": ["mmr@ciklum.com", ""],
                 "Mariia Bakush": ["mabak@ciklum.com", ""],
                 "Polina Osipchuk": ["poos@ciklum.com", ""],
                 "Roman Oliinyk": ["roli@ciklum.com", ""],
                 "Uliana Samotii": ["uls@ciklum.com", ""],
                 "Valeriia Piskunova": ["vpis@ciklum.com", ""],
                 "Vira Lyzohub": ["vvil@ciklum.com", ""],
                 "Vitaliya Lozynska": ["vloz@ciklum.com", ""],
                 "Yaroslav Tkachuk": ["ytka@ciklum.com", ""],
                 "Yurii Martsiv": ["yumar@ciklum.com", ""]}}


# For choosing the project and receiving his index
def choose_project():
    wantedProject = int(
        input("\nPlease choose the project that you want to use:\n1 - For QC\n2 - For WIMG\n3 - For OPES\n")) - 1
    print("Your chosen project is {}".format(projects[wantedProject]))
    return wantedProject


# For choosing the mission type if needed
def choose_mission():
    mapping_jql = "\"isMapping[Short text]\" ~ \"True\""
    evidance_jql = "\"isEvidence[Short text]\" ~ \"True\""
    missionType = int(input(
        "Please choose the mission type that you want to search:\n1 - For mapping mission\n2 - For evidance mission\n")) - 1
    while missionType != 1 and missionType != 0:
        missionType = int(input(
            "Please choose a valid option!\nPlease choose the mission type that you want to search:\n1 - For mapping "
            "mission\n2 - For evidance mission\n")) - 1

    if missionType == 0:
        return mapping_jql
    elif missionType == 1:
        return evidance_jql


# For choosing the available issuetype per project
def chose_issuetype(wantedProject):
    issuetype = ""
    if wantedProject == 0:
        issuetype = "issuetype = Task"
    elif wantedProject == 2:
        wimgTask = int(input("Please choose the wanted task:\n1 - For Story tasks\n2 - For Bug tasks\n"))
        while wimgTask != 1 and wimgTask != 2:
            wimgTask = int(input(
                "Please choose a valid option:\nPlease choose the wanted task:\n1 - For Story tasks\n2 - For Bug "
                "tasks\n"))
        if wimgTask == 1:
            issuetype = "issuetype = Story"
        elif wimgTask == 2:
            issuetype = "issuetype = Bug"
    return issuetype


# For getting userID by his email
def get_user_ID(team):
    print("\n")
    for worker in ops[team]:
        ops[team][worker][1] = jira._get_user_id(ops[team][worker][0])
        print(ops[team][worker])


# For choosing the relevant team
def choose_team():
    teams = ["Alignment", "Final Review", "Index", "Labeling", "Newcomers", "Refining", "Review Reports", "Scoring",
             "Scoring diagnosis", "Touchups"]
    user_choose = int(input(
        f"Please choose the relevant team:\n0 - Alignment\n1 - Final_Review\n2 - Index\n3 - Labeling\n4 - Newcomers\n"
        f"5 - Refining\n6 - Review_Reports\n7 - Scoring\n8 - Scoring_Diagnosis\n9 - Touchups\n"))

    return teams[user_choose]

# For removing the absent people from the "ops" dict
def absent_people(team):
    absent = []
    for worker in ops[team]:
        res = int(input("\nIs {} is missing today?\n1 for No \n0 for Yes\n".format(worker)))
        if res == 0:
            absent.append(worker)
    for name in absent:
        print("Removing {}!!!\n".format(name))
        ops[team].pop(name)
    if not ops[team]:
        print("No one is available today!")
        exit(1)
    print("The team today:")
    for worker in ops[team]:
        print(worker)

# For login into Jira api
def login():
    global jira

    email = str(input("Please enter your email:\n"))
    jira_token = str(input("Please enter you jira api token:\n"))
    jira = JIRA(basic_auth=(email, jira_token),
                options={'server': "https://seetree.atlassian.net/"})


def final_JQL():
    projects = {'QC' : 0, 'WIMG' : 1, 'OPES' : 2}

    wantedProject = choose_project()
    print("Please note that the maximum amount of tickets in a single search is limited to 100 tickets\n")
    if wantedProject == projects['QC']:
        jql = "project = QC AND {} AND {}".format(chose_issuetype(wantedProject), choose_mission())
    elif wantedProject == projects['WIMG']:
        jql = "project = WIMG".format(projects[wantedProject])
    elif wantedProject == projects['OPES']:
        jql = "project = OPES AND {}".format(chose_issuetype(wantedProject))
    else:
        jql = "You gave me nothing!!"
        exit(1)
    print(jql)
    result = jira.search_issues(jql, expand='changelog', maxResults=100)
    for ticket in result:
        print(ticket)


def main():
    login()
    team = choose_team()
    absent_people(team)
    get_user_ID(team)
    final_JQL()

if __name__ == '__main__':
    main()
