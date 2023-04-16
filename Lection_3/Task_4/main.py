import requests


def checkRequests(links):
    for link in links:
        response = requests.get(link)
        response.raise_for_status()
        if response.status_code == 200 or response.status_code == 302:
            print("OK")
        else:
            print("FAIL")


def main():
    links = [
        "https://google.com",
        "https://careers.epam.ua",
        "https://tasks.ngcourses.net",
    ]
    checkRequests(links)


main()
