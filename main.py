import argparse
import requests
import json
ans={}


parser=argparse.ArgumentParser(
    description="Here we go again"
)


parser.add_argument("--max",type=int,default=1700,help="Max rating")
parser.add_argument("--min",type=int,default=1400,help="Min rating")

parser.add_argument("--myID",type=str,default="SHADOW088 copycat69",help="My IDs")
parser.add_argument("--target",type=str,default="daud04 iloveoru being_mysterious",help="My IDs")
args=parser.parse_args()
#print(args.myID)
LOW_RATING=args.min
HIGH_RATING=args.max
MAX_TIME_SOLVED=0
url = "https://codeforces.com/api/user.status"
handle=[
    list(args.target.split())
]

my_handle=[
    # "SHADOW088",
    # "copycat69"
    list(args.myID.split())
]
#print(my_handle)
#print(handle)
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
                prob['contestId']
            )
            ans[z]=ans.get(z,0)+1
            global MAX_TIME_SOLVED
            MAX_TIME_SOLVED=max(ans[z],MAX_TIME_SOLVED) 

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
                prob['rating'],
                prob['contestId']
            )
            if(z not in ans):
                continue
            ans[z]=0
 
for h in handle:
    get_problem_set(h)
for h in my_handle:
    remove_my_solved(h)
for key,val in ans.items():
    if val==MAX_TIME_SOLVED:
        #print(f"{key} solve_count: {val}")
        print(f"https://codeforces.com/problemset/problem/{key[3]}/{key[0]}")

