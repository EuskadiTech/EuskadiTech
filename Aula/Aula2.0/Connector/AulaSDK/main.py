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


def classroom_list(aut):
    response = requests.get(BASE_URL + "/classroom/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def classroom_get(aut, id: int):
    response = requests.get(BASE_URL + "/classroom/" + str(id), headers=aut)
    print(response.json())
    return response.json()["result"]


def food_cal_list(aut):
    response = requests.get(BASE_URL + "/food_cal/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def food_cal_get(aut, id: int):
    response = requests.get(BASE_URL + "/food_cal/" + str(id), headers=aut)
    return response.json()["result"]


def food_menu_list(aut):
    response = requests.get(BASE_URL + "/food_menu/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def food_menu_get(aut, id: int):
    response = requests.get(BASE_URL + "/food_menu/" + str(id), headers=aut)
    return response.json()["result"]


def school_list(aut):
    response = requests.get(BASE_URL + "/school/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def school_get(aut, id: int):
    response = requests.get(BASE_URL + "/school/" + str(id), headers=aut)
    return response.json()["result"]


def student_list(aut):
    response = requests.get(BASE_URL + "/student/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def student_get(aut, id: int):
    response = requests.get(BASE_URL + "/student/" + str(id), headers=aut)
    return response.json()["result"]

def taskassign_list(aut):
    response = requests.get(BASE_URL + "/task_assign/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def taskassign_get(aut, id: int):
    response = requests.get(BASE_URL + "/task_assign/" + str(id), headers=aut)
    return response.json()["result"]

def taskgroup_list(aut):
    print(aut)
    response = requests.get(BASE_URL + "/task_group/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def taskgroup_get(aut, id: int):
    response = requests.get(BASE_URL + "/task_group/" + str(id), headers=aut)
    return response.json()["result"]

def tasktype_list(aut):
    response = requests.get(BASE_URL + "/task_type/", headers=aut)
    res = []
    for i in range(len(response.json()["result"])):
        res.append(response.json()["result"][i])
        res[i]["id"] = response.json()["ids"][i]
    return res


def tasktype_get(aut, id: int):
    response = requests.get(BASE_URL + "/task_type/" + str(id), headers=aut)
    return response.json()["result"]


def student_filter(aut, id: int, classroom: int):
    r = student_list(aut)
    return [k for k in r if k["classroom"]["id"] == classroom]
def check(k,q):
    for w in q:
        if w["id"] == k["foodmenu"]["id"]:
            return True
    return False

def food_filter(aut, classroom: int):
    s = classroom_get(aut, classroom)["school"]["id"]
    fp = school_get(aut, s)["foodplace"]["id"]
    fm = food_menu_list(aut)
    q = [m["id"] for m in fm if m["foodplace"]["id"] == fp]
    r = food_cal_list(aut)
    return [k for k in r if k["foodmenu"]["id"] in q]
def taskassign_filter(aut, classroom: int):
    x = taskgroup_list(aut)
    X = [tg["id"] for tg in x if tg["classroom"]["id"] == classroom]
    y = tasktype_list(aut)
    Y = [tt["id"] for tt in y if tt["taskgroup"]["id"] in X]
    z = taskassign_list(aut)
    Z = [ta for ta in z if ta["tasktype"]["id"] in Y]
    return Z