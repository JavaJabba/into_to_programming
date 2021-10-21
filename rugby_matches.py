#Script Name:       rugby_matches.py
#Author:            Dylan Murray 121747725

sep= "\t"

def print_match_results():
    #Ask for the first teams name and store as variable
    team1 = input("\nEnter the name of team1:",)

    #Ask for the second teams name and store as variable
    team2 = input("Enter the name of team2:",)

    #Ask for tries scored by the first team and store as int variable.
    tries_for_team1 = int(input("Enter the number of tries scored by team 1:",))

    #Ask for tries scored by the second team and store as int variable.
    tries_for_team2 = int(input("Enter the number of tries scored by team 2:\t"))

    #Ask for number of coversions and penalties scored by the first team and store as int variable.
    points_team1 = int(input("Enter the number of points from conversions and penalties scored by team 1:\t"))

    #Ask for number of coversions and penalties scored by the second team and store as int variable.
    points_team2 = int(input("Enter the number of points from conversions and penalties scored by team 2:\t"))

    #print match results with required formatting.
    print("Results:\n\n\tTeam\tTries\tPoints\n\n\t-----------------------\n")
    print("\t" + team1 +"\t " , tries_for_team1 , "\t " , points_team1)
    print("\t" + team2 +"\t " , tries_for_team2 , "\t " , points_team2,"\n")

def get_players_age():

    #Ask for players name and save as variable.
    player_name = input("Enter the name of player:\t")
    #Ask for number of days old and save as variable.
    days_old = int(input("The number of days old:\t"))
    
    

#8395
get_players_age()

