# the purpose of this is to calculate the total cost of all trucks
# first goal is the calculate the total miles trucks would drive
# this is calculated by finding number of trucks * distance


import sqlite3
import itertools

# amount in whatever units of the crop
# its not dependent on type because that makes the optimization problem many times more difficult.
def calculate_cost(amount, distance):
    # .37 dollar/ton/mile (truck) according to our source
    # 341 is the average cost per calorie for our food types
    return 0.37 * distance * amount * 341/1609


distance_dp = {}
def getDistance(county_a, county_b):

    if county_b[0] < county_a[0]:
        tmp = county_b
        county_b = county_a
        county_a = tmp

    if distance_dp.has_key(county_a + county_b):
        return distance_dp[county_a + county_b]
    else:
        dist = c.execute(
                        "SELECT distance FROM county_county_distance WHERE county_a = '{}' AND county_b = '{}'".format(
                            county_a, county_b)).fetchone()
        if dist is None:
            dist = c.execute(
                "SELECT distance FROM county_county_distance WHERE county_a = '{}' AND county_b = '{}'".format(
                    county_b, county_a)).fetchone()
        print county_a, county_b
        # Winkler Zavala
        distance_dp[county_a + county_b] = int(dist[0])
        return int(dist[0])


# open the database for storing our data
conn = sqlite3.connect('data.db')
c = conn.cursor()

deficit_counties_copy = c.execute("SELECT county, net FROM county_net_food WHERE net < 0").fetchall()
excess_counties_copy = c.execute("SELECT county, net FROM county_net_food WHERE net > 0").fetchall()

curr_best_cost = 0
curr_best_matching_data = ""

for permutation_of_deficit in itertools.permutations(deficit_counties_copy):

    # this is our temporary ones we can manipulate for this permutation's calculations
    food_in_deficit_counties = dict(deficit_counties_copy)
    food_in_excess_counties = dict(excess_counties_copy)
    cost = 0
    matching_data = " "

    for deficit_county in permutation_of_deficit:
        # now find the best excess for first, then second then third...
        county_d = deficit_county[0]
        while food_in_deficit_counties[county_d] < 0:
            county_e = None

            for county in food_in_excess_counties.keys():
                # retrieve distance between county and county_d
                if county_e is None:
                    county_e = county

                #$print county_d, county
                distancec = getDistance(county_d, county)
                # distance between county_e and county_d
                distancee = getDistance(county_d, county_e)

                if distancec < distancee:
                    county_e = county


            # now we know the best county
            food_shipped = 0

            if - food_in_deficit_counties[county_d] > food_in_excess_counties[county_e]:
                food_shipped = food_in_excess_counties[county_e]
            else:
                food_shipped = -food_in_deficit_counties[county_d]

            food_in_excess_counties[county_e] -= food_shipped
            food_in_deficit_counties[county_d] += food_shipped

            distancee = getDistance(county_d, county_e)

            cost += calculate_cost(food_shipped, distancee)
            matching_data += county_e + " -> "+ county_d + "\n"

            if food_in_excess_counties[county_e] == 0:
                # we took all the food, we must remove the county from the list
                # so it doesn't go back to this one ever again.
                food_in_excess_counties.pop(county_e)

            #print food_in_deficit_counties[county_d]
    print cost
    if cost > curr_best_cost:
        curr_best_matching_data = matching_data;


#
# COUNTY_INDEX = 0
# NET_FOOD_INDEX = 1
#
# # these come out as arrays of tuples
# deficit_counties_not_as_dict = c.execute("SELECT county, net_food FROM county_net_food WHERE county_net_food < 0")
# deficit_counties = dict(deficit_counties_not_as_dict)
# excess_counties = dict(c.execute("SELECT county, net_food FROM county_net_food WHERE county_net_food > 0"))
#
# cost = 0
#
# for permutation_of_deficit in itertools.permutations(deficit_counties_not_as_dict):
#
#     deficit_list = list(permutation_of_deficit)
#
#     while len(deficit_list) > 0:
#
#         # format of tuple (county, net_food)
#         county_a = deficit_list[len(deficit_list)-1][0]
#         distances_to_excesses = c.execute("SELECT county_a, county_b, distance FROM county_county_distance WHERE county_a='{}'".format(county_a))
#
#         # in the format (county_a, county_b, distance)
#         minimum = None
#         for excess in distances_to_excesses:
#             distance = excess[2]
#             curr_min_distance = minimum[2]
#
#             if minimum is None:
#                 minimum = excess
#             elif distance < curr_min_distance:
#                 minimum = excess
#
#
#         county_b = minimum[1]
#         distnace = minimum[2]
#         # now we have the closest excess
#         food_needed = -1 * deficit_counties[county_a][1]
#         food_can_be_shipped = excess_counties[county_b][1]
#
#         food_shipped = 0
#
#         if food_needed >= food_can_be_shipped:
#             food_shipped = food_can_be_shipped
#         elif food_needed < food_can_be_shipped:
#             food_shipped = food_needed
#
#         # take away the excess's stuff
#         excess_counties[county_b][NET_FOOD_INDEX] -= food_shipped
#         deficit_counties[county_a][NET_FOOD_INDEX] += food_shipped
#
#         if deficit_counties[county_a][NET_FOOD_INDEX] >= 0:
#             deficit_counties.pop(county_a) # cuts out last elem
#
#         if excess_counties[county_b][NET_FOOD_INDEX] == 0:
#             # can't contribute anymore food
#             excess_counties.pop(county_b)
