# Magic number
# X58653
# 'https://jutge.org/problems/X58653_en'

num_games = int(input())
team_leader_name,leader_wins,leader_looses = input().split()
second_team_name,second_number_wins,second_number_looses = input().split()

second_number_looses = int(second_number_looses)
second_number_wins = int(second_number_wins)
leader_looses = int(leader_looses)
leader_wins = int(leader_wins)

magic_number = int(num_games - leader_wins - second_number_looses + 1)   

print(f"{team_leader_name} must win {magic_number} matches")


