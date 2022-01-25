from jira import JIRA
import json

# ops = {
#     "Alignment": {"Anastasiia Rodak": ["anrod@ciklum.com", ""],
#                   "Daryna Vozdihan": ["dvoz@ciklum.com", ""],
#                   "Liliia Zadorozhna": ["liz@ciklum.com", ""],
#                   "Natalia Didych": ["ndi@ciklum.com", ""],
#                   "Oksana Levchenko": ["oksl@ciklum.com", ""],
#                   "Yulia Krupa": ["yukru@ciklum.com", ""]},
#
#     "Final_Review": {"Andrii Mandolina": ["anman@ciklum.com", ""],
#                      "Iryna Kachmar": ["ikac@ciklum.com", ""],
#                      "Iryna Kolida": ["ikol@ciklum.com", ""],
#                      "Oleksandr Kukharchuk": ["okuk@ciklum.com", ""],
#                      "Rostyslav Hasiuk": ["rhas@ciklum.com", ""],
#                      "Yaryna Tkachyk": ["yatk@ciklum.com", ""]},
#
#     "Index": {"Anastasiia Movchan": ["amov@ciklum.com", ""],
#               "Anastasiia Shelkeyeva": ["ashel@ciklum.com", ""],
#               "Dmytro Husakivskyi": ["dhus@ciklum.com", ""],
#               "Inna Pas": ["inp@ciklum.com", ""],
#               "Iryna Bolyukh": ["irbo@ciklum.com", ""],
#               "Kateryna Hulchuk": ["khul@ciklum.com", ""],
#               "Oksana Puchynska": ["okpu@ciklum.com", ""],
#               "Olena Frankiv": ["ofr@ciklum.com", ""],
#               "Tetiana Iarmoliuk": ["teia@ciklum.com", ""],
#               "Valeriia Feshchenko": ["vafe@ciklum.com", ""]},
#
#     "Labeling": {"Alisa Dobrovolska": ["aldob@ciklum.com", ""],
#                  "Tetyana Tananayska": ["tta@ciklum.com", ""],
#                  "Tetyana Tkachenko": ["ttka@ciklum.com", ""],
#                  "Yuriy Bilyk ": ["yubil@ciklum.com", ""]},
#
#     "Newcomers": {"Lidiia Fedorova": ["life@ciklum.com", ""],
#                   "Olena Shkarpinets": ["olshk@ciklum.com", ""],
#                   "Rostyslav Barabash": ["rbar@ciklum.com", ""],
#                   "Tetiana Petriv": ["tatp@ciklum.com", ""],
#                   "Uliana Komiakovych": ["uko@ciklum.com", ""]},
#
#     "Refining": {"Andrii Nikolaiev": ["annik@ciklum.com", ""],
#                  "Dmytro Bushtyn": ["dmbus@ciklum.com", ""],
#                  "Khrystyna Marynovych": ["khrm@ciklum.com", ""],
#                  "Lyubomyra Klymkovych": ["lykl@ciklum.com", ""],
#                  "Oksana Moravska": ["oxm@ciklum.com", ""]},
#
#     "Review_Reports": {"Inna Burlaka": ["inbu@ciklum.com", ""],
#                        "Khrystyna Tsebak": ["khts@ciklum.com", ""],
#                        "Lev Kuts": ["leku@ciklum.com", ""],
#                        "Volodymyr Ploshchanskyi": ["vopl@ciklum.com", ""]},
#
#     "Scoring": {"Alina Tsaruk": ["altsa@ciklum.com", ""],
#                 "Anastasiia Kauta": ["akau@ciklum.com", ""],
#                 "Anastasiya Ilnytska": ["anil@ciklum.com", ""],
#                 "Andrii Ilchyshyn": ["ailc@ciklum.com", ""],
#                 "Nazar Khibeba": ["khn@ciklum.com", ""],
#                 "Olga Kuzmyn": ["olgku@ciklum.com", ""],
#                 "Olga Martyniuk": ["olgma@ciklum.com", ""],
#                 "Sofia Kalanchova": ["soka@ciklum.com", ""],
#                 "Solomiia Zakharchyn": ["soza@ciklum.com", ""],
#                 "Vasyl Panko": ["vapan@ciklum.com", ""]},
#
#     "Scoring_Diagnosis": {"Ivan Batiuchok": ["ibat@ciklum.com", ""],
#                           "Kateryna Lys": ["klys@ciklum.com", ""],
#                           "Marta Susulovska": ["msus@ciklum.com", ""],
#                           "Olga Zhelem": ["olgz@ciklum.com", ""]},
#
#     "Touchups": {"Hanna Ellanska": ["hel@ciklum.com", ""],
#                  "Kateryna Buriak": ["kabu@ciklum.com", ""],
#                  "Mariana Mrii": ["mmr@ciklum.com", ""],
#                  "Mariia Bakush": ["mabak@ciklum.com", ""],
#                  "Polina Osipchuk": ["poos@ciklum.com", ""],
#                  "Roman Oliinyk": ["roli@ciklum.com", ""],
#                  "Uliana Samotii": ["uls@ciklum.com", ""],
#                  "Valeriia Piskunova": ["vpis@ciklum.com", ""],
#                  "Vira Lyzohub": ["vvil@ciklum.com", ""],
#                  "Vitaliya Lozynska": ["vloz@ciklum.com", ""],
#                  "Yaroslav Tkachuk": ["ytka@ciklum.com", ""],
#                  "Yurii Martsiv": ["yumar@ciklum.com", ""]},
#
#     "Open": {"Aman Abo Roken": ["aman@seetree.co", ""],
#              "Enab Halabi": ["enab@seetree.co", ""],
#              "Haifa Mansour": ["haifa@seetree.co", ""],
#              "Noor Wehbi": ["noor@seetree.co", ""],
#              "Weam Wehbi": ["weam@seetree.co", ""]}}

filters = {"Alignment": "11111",  # TODO: Add all the filters to each team
           "Final_Review": "",
           "Index": "",
           "Labeling": "",
           "Refining": "",
           "Review_Reports": "",
           "Scoring": "",
           "Scoring_Diagnosis": "",
           "Touchups": "",
           "Open": ""}

workers = {"Alignment": [],
           "Final_Review": [],
           "Index": [],
           "Labeling": [],
           "Newcomers": [],
           "Refining": [],
           "Review_Reports": [],
           "Scoring": [],
           "Scoring_Diagnosis": [],
           "Touchups": [],
           "Open": []}


class Worker:
    def __init__(self, name, team, email, key, amount_of_tickets):
        self.name = name
        self.team = team
        self.email = email
        self.key = key
        self.amount_of_tickets = amount_of_tickets


class Team(Worker):
    def __init__(self, name, team, email, key, amount_of_tickets):
        Worker.__init__(self, name, team, email, key, amount_of_tickets)


# For getting userID by his email
def get_user_id(team):
    for worker in ops[team]:
        ops[team][worker][1] = jira._get_user_id(ops[team][worker][0])
        print(ops[team][worker])


# For choosing the relevant team - return a string with the wanted team name
def choose_team():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    teams = ["Alignment", "Final Review", "Index", "Labeling", "Newcomers", "Refining", "Review Reports", "Scoring",
             "Scoring diagnosis", "Touchups", "Open"]
    user_choose = input(
        f"\nPlease choose the relevant team:\n0 - Alignment\n1 - Final_Review\n2 - Index\n3 - Labeling\n4 - Newcomers\n"
        + "5 - Refining\n6 - Review_Reports\n7 - Scoring\n8 - Scoring_Diagnosis\n9 - Touchups\n10 - Open\n")
    check_input = digits_input_validation(user_choose)
    while user_choose not in numbers and not check_input:
        print("\nPlease enter a valid option!")
        user_choose = input(
            f"Please choose the relevant team:\n0 - Alignment\n1 - Final_Review\n2 - Index\n3 - Labeling\n4 - "
            f"Newcomers\n "
            f"5 - Refining\n6 - Review_Reports\n7 - Scoring\n8 - Scoring_Diagnosis\n9 - Touchups\n10 - Open\n")
        check_input = digits_input_validation(user_choose)
    user_choose = int(user_choose)
    return teams[user_choose]


# For removing the absent people from the "ops" dict
def absent_people(team):
    absent = []
    absence = input("\nSomeone is missing today from the {} team?\n0 for No\n1 for Yes\n".format(team))
    input_check = digits_input_validation(absence)
    while absence != "0" and absence != "1" and not input_check:  # For checking invalid inputs
        print("\nPlease enter a valid option!")
        absence = input("Someone is missing today from the {} team?\n0 for No\n1 for Yes\n".format(team))
        input_check = digits_input_validation(absence)
    absence = int(absence)
    if absence == 1:  # If someone is missing
        for worker in ops[team]:
            res = input("\nIs {} is missing today?\n0 for No\n1 for Yes\n".format(worker))
            input_check = digits_input_validation(res)
            while res != "0" and res != "1" and not input_check:  # For checking invalid inputs
                print("\nPlease enter a valid option!")
                res = input("Is {} is missing today?\n0 for No\n1 for Yes\n".format(worker))
                input_check = digits_input_validation(res)
            res = int(res)
            if res == 1:
                absent.append(worker)
        for name in absent:  # Removing the missing people from ops dictionary
            print("Removing {}!!!\n".format(name))
            ops[team].pop(name)
        if not ops[team]:
            print("No one is available today!")
            exit(1)
    print("\nThe team today:")
    for worker in ops[team]:
        print(worker)
    print("\n")
    return ops


# For login into Jira api
def login():
    global jira

    email = str(input("Please enter your email:\n"))
    jira_token = str(input("\nPlease enter you jira api token:\n"))
    jira = JIRA(basic_auth=(email, jira_token),
                options={'server': "https://seetree.atlassian.net/"})


# Checks if res is digit
def digits_input_validation(res):
    return res.isdigit()


# Return filer jql by filterID
def get_jql(filter_id):
    jql = jira.filter(filter_id).raw["jql"]
    return jql


# Receiving jql string and returning list of the tickets in the jql
def get_tickets(jql):
    i = 0
    ticket_list = []
    res = jira.search_issues(jql)
    if not res:
        print("There are no tickets here!")
    else:
        print("These are the tickets the jql:")
        for issue in res:  # Creates list of the tickets in the input jql
            ticket_list.append(issue)
            print(ticket_list[i])
            i += 1
    return ticket_list


# Receives username, user key, jql and return the amount of tickets for the person
def get_tickets_amount(user_name, user_key, team_jql):
    print("\n" + user_name)
    jql = team_jql.split(" assignee = EMPTY")
    user_tickets = get_tickets(jql[0] + f" assignee = {user_key}")
    user_tickets_amount = len(user_tickets)
    if user_tickets_amount == 0:
        print(f"{user_name} has no tickets!")
    else:
        print(str(user_name) + f"'s amount of tickets: {user_tickets_amount}")
    return user_tickets_amount


# Receives team name and return the amount of tickets of each user in the team
def get_team_assignments_amounts(team_name, team_jql):
    for user in ops[team_name]:
        user["amount_of_tickets"] = get_tickets_amount(user["name"], user["key"], team_jql)
        print(f"\n{user['name']} has:")
        print(str(user["amount_of_tickets"]) + " assigned tickets")


# Builds the Analysis Center File in case of need
def workers_constructor():
    for team in ops:
        for name in ops[team]:
            email = ops[team][name][0]
            key = jira._get_user_id(email)
            print(name)
            print(team)
            print(email)
            print("\n")
            x = Worker(name, team, email, key, 0)
            workers[team].append(x.__dict__)


# Transforms the workers' dict to json file
def workers_to_json():
    json_workers = json.dumps(workers)
    f = open("Analysis_Center.txt", "x")
    f.write(json_workers)
    f.close()


# Creates the ops dictionary
def read_analisys_center():
    f = open("Analysis_Center.txt")
    analysis = json.load(f)
    f.close()
    return analysis


# TODO: Add function that will assignee the tickets by the amount of tickets

def main():
    global ops
    login()
    ops = read_analisys_center()
    team = choose_team()
    absent_people(team)
    team_jql = get_jql(filters[team])
    get_team_assignments_amounts(team, team_jql)


if __name__ == '__main__':
    main()
