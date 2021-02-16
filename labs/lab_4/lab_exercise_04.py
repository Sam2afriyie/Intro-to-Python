# START LAB EXERCISE 04
print('Lab Exercise 04 \n')

# SETUP
city_state = ["Detroit|MI", "Philadelphia|PA", "Hollywood|CA",
            "Oakland|CA", "Boston|MA", "Atlanta|GA",
            "Phoenix|AZ", "Birmingham|AL", "Houston|TX", "Tampa|FL"]
# END SETUP

# PROBLEM 1.0 (5 Points)
cali = city_state[2:4]
print(cali)

# PROBLEM 2.0 (5 Points)
us_cities = []
for cs in city_state:
    # city = city.split('|')
    # us_cities.append([0])
# print(us_cities)


#Version 2
    cs_list = cs.split('|')
    print(cs_list)
    city = cs_list[0]
    print(city)
    us_cities.append(city)


# PROBLEM 3.0 (10 Points)
southern_cities = []
#loop over us_cities
for city in us_cities:
#get index
    index = us_cities.index(city)
#if conditional statement
    if index > 4:
#append the city if it's true
        southern_cities.append(city)

print(southern_cities)

# END LAB EXERCISE