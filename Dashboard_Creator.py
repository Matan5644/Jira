from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Free\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Profile 2")
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', chrome_options=options)
driver.get("https://seetree.atlassian.net/jira/your-work")
driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/header/nav/div[2]/div[4]/button/span[2]/span")


# options = Options()
# options.add_argument("user-data-dir=C:\\Users\\AtechM_03\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', chrome_options=options)
# driver.get("https://accounts.google.com/o/oauth2/auth/identifier?state=eyJzb3VyY2UiOiJsb2dpblNjcmVlbiIsInVzZXJGbG93IjpudWxsLCJpc1NsYWNrQXBwU291cmNlIjpudWxsLCJxdWVyeSI6Ij9hcHBsaWNhdGlvbj1qaXJhJmNvbnRpbnVlPWh0dHBzOi8vc2VldHJlZS5hdGxhc3NpYW4ubmV0L2xvZ2luP3JlZGlyZWN0Q291bnQlM0QxJTI2ZGVzdC11cmwlM0RodHRwcyUyNTNBJTI1MkYlMjUyRnNlZXRyZWUuYXRsYXNzaWFuLm5ldCUyNTJGamlyYSUyNTJGeW91ci13b3JrJTI2YXBwbGljYXRpb24lM0RqaXJhJmxvZ2luVHlwZT1nb29nbGVCdXR0b24mbG9naW5faGludD0mcHJvbXB0PXNlbGVjdF9hY2NvdW50JnNvdXJjZT1sb2dpblNjcmVlbiIsImNzcmZUb2tlbiI6IjY1OWE1MWIxMjQ4NDAyNWM4NDE3MzVlZThkMzIwMTQzNjczMDA3ZmNlYjJjZjhjZGYyZjBhZTcyY2M3ZDJhNTIiLCJsb2dpblR5cGUiOiJnb29nbGVCdXR0b24iLCJhbm9ueW1vdXNJZCI6ImU2YTUwZTNmLTRhMzYtNDk4Mi1iOWExLTI0NTliOTUwYzllMCIsIm1hcmtldGluZ0NvbnNlbnQiOm51bGwsImV4cGVyaW1lbnQiOm51bGx9&scope=profile%20email&prompt=select_account&redirect_uri=https%3A%2F%2Fid.atlassian.com%2Flogin%2Fgoogle&client_id=596149463257-9oquqfivs9on8t8erq23c8qso6vk3cp1.apps.googleusercontent.com&code_challenge=-83j-rMV4rrwtiNZ_3ezWb7M3hWjxfsLL0e588GcrOo&code_challenge_method=S256&response_type=code&flowName=GeneralOAuthFlow")
# jira_login = driver.find_element_by_id("identifierId")
# time.sleep(3)
# jira_login.send_keys("matan@seetree.co")
# jira_login.send_keys(Keys.RETURN)
# time.sleep(3)
# jira_login2 = driver.find_element_by_name("password")
# jira_login2.send_keys("Seetree12345")
# jira_login2.send_keys(Keys.RETURN)
