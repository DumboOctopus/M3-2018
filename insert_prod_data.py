# the purpose of this file is to insert all
# of the food production data for each county
# unfortunately, the data is not a table so we
# have to manually enter it into the database


import sqlite3

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# open the database
conn = sqlite3.connect('data.db')
c = conn.cursor()




# county = raw_input("County name: ")
# data_values = input("amt: ")
# insertions = [data_values]
#
# for i in xrange(data_values):
#     tmp = raw_input().split(" ")
#     insertions[i] = (tmp[0], int(tmp[1]))
#
# query = "INSERT INTO food_production_county ("
# for insertion in insertions:
#     query += insertion[0] + ","
# # cut off last char and put a closing parenthesis
# query = query[:-1] + ")"
# query += "VALUES("
# for insertion in insertions:
#     if is_int(insertion[1]):
#         query += insertion[1] + ","
#     else:
#         query += "'"+insertion[1] + "'" + ","
#

