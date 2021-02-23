'''
✅step 1 -> Total number of person according to the team
✅step 2 -> Total number of pizzas
✅step 3 -> Total number of unique pizzas
✅step 4 -> Prepare a nested list of team size and number of present team
✅Calculate total number of pizzas distributed with team size
Distribute unique pizza in a team
'''
from more_pizza import main as process

def logic(li):
    data_present = {}
    data_present["total_pizza"] = int(li[0][0])
    data_present["two"] = int(li[0][1])*2
    data_present["three"] = int(li[0][2])*3
    data_present["four"] = int(li[0][3])*4
    print(data_present)
    total_no_people = (int(li[0][1])*2) + (int(li[0][2])*3) + (int(li[0][3])*4)
    print("total number of people",total_no_people)
    print("total number of pizzas",data_present["total_pizza"])
    temp = [tuple(sorted(sub)) for sub in li[1:]] 
    res = list(set(temp))
    print("total number of unique pizzas",len(res))
    list_outer = []
    for i in range(4):
        if i==0:
            n = int(li[0][i])
        else:
            list_inner = []
            list_inner.append(i+1)
            list_inner.append(int(li[0][i]))
            list_outer.append(list_inner)
    print("Nested list of team size and number of team of that particular size",list_outer)
    
    i = 0
    result_dict = {}
    for i in range(len(list_outer)):
        k = 0
        multiplier = list_outer[i][k] * list_outer[i][k+1]
        if (n-multiplier >= 0):
            result_dict[list_outer[i][k]]= multiplier//list_outer[i][k]

        elif(n-multiplier < 0):
            if (n-(multiplier//list_outer[i][k+1]) > 0) and (n-(multiplier//list_outer[i][k+1])%list_outer[i][k]):
                result_dict[list_outer[i][k]]= multiplier//list_outer[i][k]
        if n > 0:
            n = n-(multiplier//list_outer[i][k])
        else:
            break

    print("Resultant Dictionary of Possible districution",result_dict)
        

func_call = process()
logic(func_call)
