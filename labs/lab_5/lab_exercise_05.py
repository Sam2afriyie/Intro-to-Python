# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

# SETUP

record = [
    ['school', 'year', 'won', 'lost', 'win_percent', 'bowl_appear', 'bowl_win'],
    ['Michigan', 2019, 9, 4, None, True, False],
    ['Michigan', 2018, 10, 3, None, True, False],
    ['Michigan', 2017, 8, 5, None, True, False],
    ['Michigan', 2016, 10, 3, None, True, False],
    ['Michigan', 2015, 10, 3, None, True, True],
    ['Michigan', 2014, 5, 7, None, False, False],
    ['Michigan', 2013, 7, 6, None, True, False],
    ['Michigan', 2012, 8, 5, None, True, False],
    ['Michigan', 2011, 11, 2, None, True, True],
    ['Michigan', 2010, 7, 6, None, True, False],
    ['Michigan', 2009, 5, 7, None, False, False],
    ['Michigan', 2008, 3, 9, None, False, False],
    ['Michigan', 2007, 9, 4, None, True, True],
    ['Michigan', 2006, 11, 2, None, True, False],
    ['Michigan', 2005, 7, 5, None, True, False],
    ['Michigan', 2004, 9, 3, None, True, False],
    ['Michigan', 2003, 10, 3, None, True, False],
    ['Michigan', 2002, 10, 3, None, True, True],
    ['Michigan', 2001, 8, 4, None, True, False],
    ['Michigan', 2000, 9, 3, None, True, True]
]

# END SETUP

# PROBLEM 1.0 (5 Points)
def calculate_win_percentage(wins, losses):
    wp = wins / (wins + losses)
    return round(wp, 3)

wp = calculate_win_percentage(5,5)
print(wp)
wp = calculate_win_percentage(9993, 7)
print(wp)
wp = calculate_win_percentage(9997,3)
print(wp)

# PROBLEM 2.0 (5 Points)
for r in record[1:]:
    win = r[2]
    loss = r[3]
    wp = calculate_win_percentage(win, loss)
    r[4] = wp

print(record)


# PROBLEM 3.0 (5 Points)
record_wins = 0
record_losses = 0

for r in record[1:]:
    record_wins += r[2]
    record_losses += r[3]

record_win_percent = calculate_win_percentage(record_wins, record_losses)


# PROBLEM 4.0 (5 Points)
def calculate_best_year(record):
    year = None
    best_wp = 0
    worst_year = 0

    for r in record[1:]:
        calculate_win_percentage(r[2], r[3])
        # wp = r[4]
        if wp > best_wp:
            best_wp = wp
            year = r[1]
        elif wp == best_wp and r[-2] == True and r[-1] == True:
            year = r[1]
    return year
best_year = calculate_best_year(record)

# def calculate_worst_year(record)


# END LAB EXCERCISE