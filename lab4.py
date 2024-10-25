import data
import math
# Write your functions for each part in the space below.

# Part 1
#
def first_element(list: list[list[int]])-> list:
    Innerlist = []
    for i in range(len(list)):
        if len(list[i]) > 0:
            Innerlist.append(list[i][0])
    return Innerlist




# Part 2
def x_coordinates(list: list[data.Point])->list:
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i].x)
    return(new_list)


# Part 3

def are_in_positive_quadrant(list: list[data.Point]):
    pos_list = []

    for i in range(len(list)):
        if(list[i].x>0 and list[i].y>0):
            coorlist = []
            coorlist.append(list[i].x)
            coorlist.append(list[i].y)
            pos_list.append(coorlist)
    return(pos_list)



# Part 4
def distance(point1 = data.Point,point2 = data.Point)-> float:
    x_distance = (point1.x-point2.x)**2
    y_distance = (point1.y-point2.y)**2
    return math.sqrt(x_distance+y_distance)




# Part 5
def manhattan_distance(p1 = data.Point,p2 = data.Point):
    x_distance = abs(p1.x - p2.x)
    y_distance = abs(p1.y - p2.y)
    return(x_distance+y_distance)




# Part 6

def distance_all(list: list[data.Point]):
    distance = []
    for i in range(len(list)):
        x_distance = (list[i].x - 0)**2
        y_distance = (list[i].y - 0)**2
        Dis_final = math.sqrt(x_distance+y_distance)
        distance.append(Dis_final)
    return distance



