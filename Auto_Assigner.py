import time
from datetime import datetime
from jira import JIRA
import json

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
def team_selector():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    teams = ["Alignment", "Final_Review", "Index", "Labeling", "Newcomers", "Refining", "Review_Reports", "Scoring",
             "Scoring_Diagnosis", "Touchups", "Open"]
    # Validation of the user input
    user_choose = input(
        f"\nPlease choose the relevant team:\n0 - Alignment\n1 - Final_Review\n2 - Index\n3 - Labeling\n4 - Newcomers\n"
        + "5 - Refining\n6 - Review_Reports\n7 - Scoring\n8 - Scoring_Diagnosis\n9 - Touchups\n10 - Open\n")
    check_input = digits_input_validation(user_choose)
    while user_choose not in numbers or not check_input:  # For checking invalid inputs
        print("\nPlease enter a valid option!")
        user_choose = input(
            f"\nPlease choose the relevant team:\n0 - Alignment\n1 - Final_Review\n2 - Index\n3 - Labeling\n4 - "
            f"Newcomers\n "
            f"5 - Refining\n6 - Review_Reports\n7 - Scoring\n8 - Scoring_Diagnosis\n9 - Touchups\n10 - Open\n")
        check_input = digits_input_validation(user_choose)
    user_choose = int(user_choose)
    return teams[user_choose]


# For removing the absent people from the "ops" dict
def absent_people(team):
    absence = input("\nSomeone is missing today from the {} team?\n0 for No\n1 for Yes\n".format(team))
    input_check = digits_input_validation(absence)
    team_amount = len(ops[team])
    i = 0

    # Validation of the user input
    while (absence != "0" and absence != "1") or not input_check:
        print("\nPlease enter a valid option!")
        absence = input("Someone is missing today from the {} team?\n0 for No\n1 for Yes\n".format(team))
        input_check = digits_input_validation(absence)
    absence = int(absence)
    if absence == 1:  # If someone is missing
        while i < team_amount:
            res = input("\nIs {} is missing today?\n0 for No\n1 for Yes\n".format(ops[team][i]['name']))
            input_check = digits_input_validation(res)
            while (res != "0" and res != "1") or not input_check:  # For checking invalid inputs
                print("\nPlease enter a valid option!")
                res = input("Is {} is missing today?\n0 for No\n1 for Yes\n".format(ops[team][i]['name']))
                input_check = digits_input_validation(res)
            res = int(res)
            if res == 0:
                i += 1
            else:
                print("Removing {}!!!\n".format(ops[team][i]['name']))  # Removing the chosen worker
                ops[team].pop(i)
            team_amount = len(ops[team])
        if not ops[team]:
            print("No one is available today!")
            exit(1)
    else:  # If no-one missing
        print("\nThe team today:")
        for worker in ops[team]:
            print(worker['name'])


# For adding guys from other teams to the relevant team
def get_new_guys(team):
    new_guys = []
    new_ppl = input("\nWill you have guys from other teams today?\n0 for No\n1 for Yes\n")
    input_check = digits_input_validation(new_ppl)

    while (new_ppl != "0" and new_ppl != "1") or not input_check:
        print("\nPlease enter a valid option!")
        new_ppl = input("\nYou will have guys from other teams today?\n0 for No\n1 for Yes\n")
        input_check = digits_input_validation(new_ppl)
    new_ppl = int(new_ppl)

    if new_ppl == 1:  # If someone from other team is joining
        print("\nPlease choose the new guy's team:")
        new_guy_team = team_selector()
        for worker in ops[new_guy_team]:  # Iterate through the new guy's team
            new_guy = input("\nWill {} join to your team?\n0 for No\n1 for Yes\n".format(worker["name"]))
            input_check = digits_input_validation(new_guy)
            while (new_guy != "0" and new_guy != "1") or not input_check:  # For checking invalid inputs
                print("\nPlease enter a valid option!")
                new_guy = input("\nWill {} join to your team?\n0 for No\n1 for Yes\n".format(worker["name"]))
                input_check = digits_input_validation(new_guy)
            new_guy = int(new_guy)
            if new_guy == 1:  # Adding the new guy to the new_guys lists.
                new_guys.append(worker)
            elif new_guy == 0:
                continue
        for worker in new_guys:  # Adding all the new guys from the new_guys list to the user team
            ops[team].append(worker)
        other_team = input("\nWill someone from another team will join to your team?\n0 for No\n1 for Yes\n")
        input_check = digits_input_validation(other_team)
        while (other_team != "0" and other_team != "1") or not input_check:  # For checking invalid inputs
            print("\nPlease enter a valid option!")
            new_ppl = input("\nWill someone from another team will join to your team?\n0 for No\n1 for Yes\n")
            input_check = digits_input_validation(new_ppl)
        other_team = int(other_team)
        if other_team == 0:
            return
        else:
            get_new_guys(team)
    else:
        return


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
def get_jql_tickets(jql):
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
def get_users_tickets_amount(user_name, user_key, team_jql):
    print("\n" + user_name)
    jql = team_jql.split(" assignee = EMPTY")
    print(jql[0] + f" assignee = {user_key}")
    user_tickets = get_jql_tickets(jql[0] + f" assignee = {user_key}")
    user_tickets_amount = len(user_tickets)

    if user_tickets_amount == 0:  # While worker has no tickets
        print(f"{user_name} has no tickets!")
        time.sleep(2)
    else:
        print(str(user_name) + f"'s amount of tickets: {user_tickets_amount}")
        time.sleep(2)
    return user_tickets_amount


# Receives team name and return the amount of tickets of each user in the team
def get_team_assignments_amounts(team_name, team_jql):
    for user in ops[team_name]:
        user["amount_of_tickets"] = get_users_tickets_amount(user["name"], user["key"], team_jql)


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


# Transforms the workers dict to json file
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


# Returns the email of the worker with the least amount of tickets
def find_least_assignments_man(team):
    min_worker = ops[team][0]
    for worker in ops[team]:
        if worker['amount_of_tickets'] < min_worker['amount_of_tickets']:
            min_worker = worker
    print(
        f"\n{min_worker['name']} has the lowest amount of tickets! She has {min_worker['amount_of_tickets']} tickets.")
    return min_worker['email']


# Assigns the ticket with the highest latency to the person with the least amount of tickets
def assignee_oldest_ticket(worker_email, team_jql):
    unassignee_issues_list = get_jql_tickets(team_jql)
    if not unassignee_issues_list:
        print("\nCurrently, there are no unassigned tickets.")
        return
    highest_days_since_shooting_ticket = str(unassignee_issues_list[0])
    jira.assign_issue(highest_days_since_shooting_ticket, worker_email)


# Auto assigner every 5 min
def auto_assigner(team, team_jql):
    five_minutes = 300
    second = 0
    get_team_assignments_amounts(team, team_jql)
    min_worker = find_least_assignments_man(team)
    assignee_oldest_ticket(min_worker, team_jql)
    while second < five_minutes:
        print(f"Checking again in {five_minutes - second} seconds\n")
        time.sleep(1)
        second += 1


# For getting the current time
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    int_current_time = int(current_time[0:2])
    return int_current_time


# For recreate Analysis Center json file
def recreate_analysis_centre():
    workers_constructor()


def main():
    global ops

    login()
    ops = read_analisys_center()
    team = team_selector()
    absent_people(team)
    get_new_guys(team)
    team_jql = get_jql(filters[team])
    current_time = get_current_time()
    while (current_time >= 9) and (current_time <= 18):
        auto_assigner(team, team_jql)


if __name__ == '__main__':
    main()
