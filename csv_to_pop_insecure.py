
#import necessary packages
import csv
import sqlite3

# open the database for storing our data
conn = sqlite3.connect('data.db')
c = conn.cursor()

# opens the county_insecure csv file.
# this csv was created by copy pasting data from here:
# http://www.feedingamerica.org/research/map-the-meal-gap/2015/MMG_AllCounties_CDs_MMG_2015_2/TX_AllCounties_CDs_MMG_2015.pdf

with open('county_insecure', 'rb') as csvfile:

    spamreader = csv.reader(csvfile)

    # reads each line from the csv
    for row in spamreader:
        # inserts the database
        query = ("INSERT INTO food_insecure_county (county, insecure_population, calories_needed) VALUES('{}', {}, {})".format(row[0], row[3], int(row[3]) * 1857))
        # print out the query for checking for errors.
        print query
        c.execute(query)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()