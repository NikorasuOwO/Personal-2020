
def are_next(p1, p2):
    """
    finds if two points (x1, y1) and (x2, y2) are next
    """
    print(p1)
    print(p2)
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) == 1

    #return (abs(px)==1 and py == 0) or (abs(py)==1 and px == 0)

def joinable(point, set_tuple):
    """
    finds if a point is elligeable to be in a set of points (based on are_next)
    """
    
    for set_point in set_tuple[1]:
        if (are_next(point, set_point)):
            print("joinable:\tpoint TRUE: ", point, " | ", "set_tuple: ", set_tuple)
            return True
    print("joinable:\tpoint FALSE: ", point, " | ", "set_tuple: ", set_tuple)
    return False

def fbg_in_coin(list):
    """
    finds the bigger group in a coin's set of points. returns (elem_set, point_of_the_set)
    """


    max_var = ()

    for point in list:
        for set_tuple in sets:
            if joinable(point, set_tuple):
                set_tuple[1].append(point) #adds poin to set
                set_tuple[0] += 1
                break
        sets.append( (1, [point]) ) # makes new group
        break
    
    print("sets: ", sets)
    max_var = max(sets)
    print("max_var: ", max_var)
    b = max_var[0][0]
    return (a, b)


def find_bigger_group(json):

    """
    Finds the bigger group of coins that are joint in the grid an returns the position of one of its elements
    """

    bestNum = 0
    best_point = (-1, -1)

    for coin_name in json.keys():
        res = fbg_in_coin(json[coin_name]["grid_index"])
        if res[0] > best_point[0]:
            best_point[1] = res[1]

    return best_point[1]

