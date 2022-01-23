from jira import JIRA

projects = {1: 'QC', 2: 'WIMG', 3: 'OPES'}


# For choosing the project and receiving his index
def choose_project():
    wantedProject = input("\nPlease choose the project that you want to use:\n1 - For QC\n2 - For WIMG\n3 - For OPES\n")
    check_input = digits_input_validation(wantedProject)
    while wantedProject != "1" and wantedProject != "2" and wantedProject != "3" and not check_input:
        print("Please enter a vaild option!\n")
        wantedProject = input(
            "\nPlease choose the project that you want to use:\n1 - For QC\n2 - For WIMG\n3 - For OPES\n")
        check_input = digits_input_validation(wantedProject)
    wantedProject = int(wantedProject)
    print("Your chosen project is {}".format(projects[wantedProject]))
    return wantedProject


# For choosing the mission type if needed
def choose_mission():
    mapping_jql = "\"isMapping[Short text]\" ~ \"True\""
    evidance_jql = "\"isEvidence[Short text]\" ~ \"True\""
    missionType = input(
        "Please choose the mission type that you want to search:\n0 - For mapping mission\n1 - For evidance mission\n")
    check_input = digits_input_validation(missionType)
    while missionType != "1" and missionType != "0" and not check_input:
        missionType = input(
            "Please choose a valid option!\nPlease choose the mission type that you want to search:\n0 - For mapping "
            "mission\n1 - For evidance mission\n")
        check_input = digits_input_validation(missionType)
    missionType = int(missionType)
    if missionType == 0:
        return mapping_jql
    elif missionType == 1:
        return evidance_jql


# For choosing the available issuetype per project
def chose_issuetype(wantedProject):
    issuetype = ""
    if wantedProject == 1:
        issuetype = "issuetype = Task"
    elif wantedProject == 3:
        wimgTask = input("Please choose the wanted task:\n1 - For Story tasks\n2 - For Bug tasks\n")
        check_input = digits_input_validation(wimgTask)
        while wimgTask != "1" and wimgTask != "2" and not check_input:
            wimgTask = input(
                "Please choose a valid option:\nPlease choose the wanted task:\n1 - For Story tasks\n2 - For Bug "
                "tasks\n")
            check_input = digits_input_validation(wimgTask)
        wimgTask = int(wimgTask)
        if wimgTask == 1:
            issuetype = "issuetype = Story"
        elif wimgTask == 2:
            issuetype = "issuetype = Bug"
    return issuetype


def final_JQL():
    wantedProject = choose_project()
    print("\nPlease note that the maximum amount of tickets in a single search is limited to 100 tickets!!!")
    if wantedProject == 1:
        jql = "project = {} AND {} AND {}".format(projects[wantedProject], chose_issuetype(wantedProject),
                                                  choose_mission())
    elif wantedProject == 2:
        jql = "project = {}".format(projects[wantedProject])
    elif wantedProject == 3:
        jql = "project = {} AND {}".format(projects[wantedProject], chose_issuetype(wantedProject))
    else:
        jql = "You gave me nothing!!"
        exit(1)
    print(jql)
    result = jira.search_issues(jql, expand='changelog', maxResults=100)
    for ticket in result:
        print(ticket)


def digits_input_validation(res):
    return res.isdigit()


def login():
    global jira

    email = str(input("Please enter your email:\n"))
    jira_token = str(input("\nPlease enter you jira api token:\n"))
    jira = JIRA(basic_auth=(email, jira_token),
                options={'server': "https://seetree.atlassian.net/"})


def main():
    login()
    final_JQL()


if __name__ == '__main__':
    main()
