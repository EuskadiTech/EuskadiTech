import requests

BASE_URL = "http://127.0.0.1:5000/api/v1"


def auth(user, password):
    data = {"password": password, "provider": "db", "refresh": True, "username": user}
    response = requests.post(BASE_URL + "/security/login", json=data)
    if response.status_code != 200:
        raise ValueError(
            "The credentials are invalid or the endpoint is having trouble, http code "
            + str(response.status_code)
            + "."
        )
    at = response.json()["access_token"]
    rt = response.json()["refresh_token"]
    return {"Authorization": "Bearer " + at}


def classroom_list(auth):
    response = requests.get(BASE_URL + "/classroom/", headers=auth)
    return response.json()["result"]


def classroom_get(auth, id: int):
    response = requests.get(BASE_URL + "/classroom/" + str(id), headers=auth)
    return response.json()["result"]


def food_cal_list(auth):
    response = requests.get(BASE_URL + "/food_cal/", headers=auth)
    return response.json()["result"]


def food_cal_get(auth, id: int):
    response = requests.get(BASE_URL + "/food_cal/" + str(id), headers=auth)
    return response.json()["result"]


def food_menu_list(auth):
    response = requests.get(BASE_URL + "/food_menu/", headers=auth)
    return response.json()["result"]


def food_menu_get(auth, id: int):
    response = requests.get(BASE_URL + "/food_menu/" + str(id), headers=auth)
    return response.json()["result"]


def school_list(auth):
    response = requests.get(BASE_URL + "/school/", headers=auth)
    return response.json()["result"]


def school_get(auth, id: int):
    response = requests.get(BASE_URL + "/school/" + str(id), headers=auth)
    return response.json()["result"]


def student_list(auth):
    response = requests.get(BASE_URL + "/student/", headers=auth)
    return response.json()["result"]


def student_get(auth, id: int):
    response = requests.get(BASE_URL + "/student/" + str(id), headers=auth)
    return response.json()["result"]


def student_filter(auth, id: int, classroom: int):
    r = student_list(auth)
    return [k for k in r if k["classroom"]["id"] == classroom]
def check(k,q):
    for w in q:
        if w["notes"] == k["foodmenu"]["notes"] and k["foodmenu"]["name"] == w["name"]:
            return True
    return False

def food_filter(auth, classroom: int):
    s = classroom_get(auth, classroom)["school"]["id"]
    fid = school_get(auth, s)["foodplace"]["id"]
    fl = food_menu_list(auth)
    q = [m for m in fl if m["foodplace"]["id"] == fid]
    r = food_cal_list(auth)
    return [k for k in r if check(k,q)]