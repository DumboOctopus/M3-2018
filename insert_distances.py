
#import necessary packages
import sqlite3

# open the database for storing our data
conn = sqlite3.connect('data.db')
c = conn.cursor()

# opens the county_insecure csv file.
# this csv was created by copy pasting data from here:
# http://www.feedingamerica.org/research/map-the-meal-gap/2015/MMG_AllCounties_CDs_MMG_2015_2/TX_AllCounties_CDs_MMG_2015.pdf

with open('Texas_County_Distances.txt') as file:
    # reads each line from the csv
    for line in file:

        # format of lines county_a --> county_b : distance
        tmp = line.split(" --> ")
        county_a = tmp[0].replace(" County", "")
        tmp = tmp[1].split(" : ")
        county_b = tmp[0].replace(" County", "")
        # the distance is given as floats but we want integers because its not that percise
        distance = int(float(tmp[1]))

        query = ("INSERT INTO county_county_distance (county_a, county_b, distance) VALUES('{}', '{}', {})".format(county_a, county_b, distance))
        # print out the query for checking for errors.
        print query
        c.execute(query)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()