import sqlite3

# open the database for storing our data
conn = sqlite3.connect('data_texas.db')
c = conn.cursor()

f = open("W values", "w")

sum_of_counties_nets = 0

with open("food_production_county.tsv") as file:
    for line in file:
        splitting = [i.replace(",", "") for i in line.split("\t")]
        county = splitting[0]
        # County cattle wheat milk_cows corn sorghum oats rice soybean	sunflower_oil	sugarcane	peanuts	sunflower_nonoil
        cattle = 0.095 * 974 * int(splitting[1])
        wheat = 0.14 * 179 * int(splitting[2])
        milk_cows = 0.052 * 13824 * int(splitting[3])
        corn = 0.14 * 268 * int(splitting[4])
        sorghum = 0.14 * 236 * int(splitting[5])
        oats = 0.14 * 155 * int(splitting[6])
        rice = 0.14 * 138 * int(splitting[7])
        soybean = 0.14 * 333 * int(splitting[8])
        sunflower_oil = 0.17 * 10.9 * int(splitting[9])
        sugarcan = .26 * 648 * int(splitting[10])
        peanut = 0.17 * 7.05 * int(splitting[11])
        sunflower_nonoil = 0.17 * 10.9 * int(splitting[12])

        # total calories we can gain from not wasting this stuff at production NOTE: WE CHANGED The pop/retail
        calories = cattle + wheat + milk_cows + corn + sorghum + oats + rice + soybean + sunflower_oil + sugarcan + peanut + sunflower_nonoil;
        groceries_in_this_county = int(c.execute("SELECT population from food_insecure_county where county= '{}'".format(county)).fetchone()[0])/5009
        calories_wasted_by_retail = 0.0378 * groceries_in_this_county * 2231
        calories += calories_wasted_by_retail


        net = int(calories) - int(c.execute("SELECT calories_needed from food_insecure_county where county= '{}'".format(county)).fetchone()[0])
        sum_of_counties_nets += net
        query = "INSERT INTO county_net_food (county, net, wasted_calories) VALUES('{}', {}, {})".format(county, net, calories)
        print query
        c.execute(query)

        f.write(county + "   " + str(calories))
        f.write("\n")
f.write("net sum " + str(sum_of_counties_nets))


# remove this line so it doesn't actually add more stuff to db.
conn.commit()
conn.close()