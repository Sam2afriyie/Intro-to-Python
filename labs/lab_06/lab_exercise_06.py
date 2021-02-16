# START LAB EXERCISE 06
print('Lab Exercise 06 \n')

#SETUP
mario_kart_game = [
('Peach', 49), ('Mario', 35), ('Yoshi', 23),
('Wario', 20), ('Daisy', 18), ('Luigi', 10)
]

# END SETUP

# PROBLEM 1 (5 points)
def scores(game):
    #calculate the total score of team 1
    team_1 = mario_kart_game[0][1] + mario_kart_game[1][1] + mario_kart_game[2][1]
    #calculate the total score of team 2
    team_2 = mario_kart_game[3][1] + mario_kart_game[4][1] + mario_kart_game[-1][1]
    return (team_1, team_2)
# PROBLEM 2 (5 points)
def blue_shell(game):
    #1) Remove the player in first place
    player = game.pop(0)
    #2) Insert that player into the list in third place
    game.insert(2, player)
    #3) Return the modified list
    return game
# PROBLEM 3 (5 points)
# SETUP
new_mario_kart_game =  [
('Donkey Kong', 45), ('Mario', 30), ('Yoshi', 22),
('Wario', 20), ('Toad', 18), ('Peach', 15)
]

# END SETUP

# PROBLEM 4 (5 points)
def top_three(game):
    new_list = []
    #calculate the total score of team 1
    # team1_scores = game[0][1] + game[1][1] + game[2][1]
    # print(team1_scores)
    # get the strings of the first three items in the tupl
    new_list.append(game[0][0])
    new_list.append(game[1][0])
    new_list.append(game[2][0])
    #Optiton 2
    #new_list = []
    #for player in game[0:3]:
        #new_list.append(player[0])
            #return new_list
    # print()
    # print()
    #Return a list with those strings
    return new_list

# main()
def main():
    pass
    #call <scores() > and assign to <team_scores >
    team_scores = scores(mario_kart_game)
    print(f'First game team scores: {team_scores}') ## Uncomment when ready!

    # Call < blue_shell() > and assign to < blue_shell_players >
    blue_shell_players = blue_shell(mario_kart_game)
    print(f'Player positions after blue shell: {blue_shell_players}') ## Uncomment when ready!

    # Insert the new character tuple as the first element of < new_mario_kart_game >
    bowser = ('Bowser', 60)
    new_mario_kart_game.insert(0, bowser)
    print(f'Updated new game: {new_mario_kart_game}') ## Uncomment when ready!

    # Call < top_three() > and assign to top_three_players
    top_three_players = top_three(new_mario_kart_game)
    print(f'Top three players: {top_three_players}') ## Uncomment when ready!

    # END LAB EXERCISE

if __name__ == '__main__':
    main()