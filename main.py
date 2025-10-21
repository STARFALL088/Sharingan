import requests
import json
ans={}
LOW_RATING=1500
HIGH_RATING=1700

url = "https://codeforces.com/api/user.status"
handle=[
    "daud04",
    "iloveoru",
    "being_mysterious"
]

my_handle=[
    "SHADOW088",
    "copycat69"
]

def get_data(h):
    params = {

        "handle": h,
        "from": 1,  
        "count": 5000,
        }

    response = requests.get(url, params=params)

    return response.json()

def get_problem_set(h):
    data=get_data(h)
    #   print(data)
    for i in range(1,5000):
        if(len(data['result'])<=i):
            continue
        if(data['result'][i]['verdict']!='OK'):
            continue
        prob=data["result"][i]["problem"];
        if  prob.get('rating') and prob['rating']>=LOW_RATING and prob['rating']<=HIGH_RATING :

            z=(
                prob['index'],
                prob['name'],
                prob['rating'],
            )
            ans[z]=ans.get(z,0)+1

def remove_my_solved(h):
    data=get_data(h)
    for i in range(1,5000):
        if(len(data['result'])<=i):
            continue
        if(data['result'][i]['verdict']!='OK'):
            continue
        prob=data["result"][i]["problem"];
        if  prob.get('rating') and prob['rating']>=LOW_RATING and prob['rating']<=HIGH_RATING :

            z=(
                prob['index'],
                prob['name'],
                prob['rating']
            )
            if(z not in ans):
                continue
            ans[z]=0
 
for h in handle:
    get_problem_set(h)
for h in my_handle:
    remove_my_solved(h)
for key,val in ans.items():
    if val>0:
        print(f"{key} solve_count: {val}")
