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
    return distance_dp[county_a + county_b]


# open the database for storing our data
conn = sqlite3.connect('data.db')
c = conn.cursor()

deficit_counties_copy = c.execute("SELECT county, net FROM county_net_food WHERE net < 0").fetchall()
excess_counties_copy = c.execute("SELECT county, net FROM county_net_food WHERE net > 0").fetchall()

for records in c.execute("SELECT county_a, county_b, distance FROM county_county_distance").fetchall():
    distance_dp[records[0] + records[1]] = int(records[2])
    distance_dp[records[1] + records[0]] = int(records[2])

# this is our temporary ones we can manipulate for this permutation's calculations
food_in_deficit_counties = dict(deficit_counties_copy)
food_in_excess_counties = dict(excess_counties_copy)
cost = 0
matching_data = " "

for deficit_county in deficit_counties_copy:
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
        print food_in_deficit_counties[county_d]

print cost
print matching_data