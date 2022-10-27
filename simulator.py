import random

leagues = {
    'Premier League': ['Arsenal','Aston Villa','Brighton and Hove Albion','Burnley','Chelsea','Crystal Palace','Everton','Fulham','Leeds United','Liverpool','Leicester City','Manchester City','Manchester United','Newcastle United','Sheffield United','Southampton','Tottenham Hotspur','West Bromwich Albion','West Ham United','Wolverhampton Wanderers'],
    'Championship': ['Birmingham City', 'Blackburn Rovers', 'Blackpool', 'Bristol City', 'Burnley', 'Cardiff City', 'Coventry City', 'Huddersfield Town', 'Hull City', 'Luton Town', 'Middlesbrough', 'Millwall', 'Norwich City', 'Preston North End', 'Queens Park Rangers', 'Reading', 'Rotherham', 'Sheffield United', 'Stoke City', 'Sunderland', 'Swansea City', 'Watford', 'West Bromich Albion', 'Wigan'],
    'League 1': ['Plymouth Argyle', 'Ipswich Town', 'Sheffield Wednesday', 'Petersborough United', 'Portsmouth', 'Barnsley', 'Bolton Wanderers', 'Shrewsbury Town', 'Derby County', 'Charlton Athletic', 'Exeter City', 'Bristol Rovers', 'Wycombe Wanderers', 'Lincoln City', 'Fleetwood Town', 'Port Vale', 'Accrington Stanley', 'Cambridge United', 'Oxford United', 'Cheltenham Town', 'Forest Green Rovers', 'Milton Keynes Dons', 'Burton Albion', 'Morecambe'],
    'League 2': ['Stevenage', 'Leyton Orient', 'Northampton Town', 'Mansfield Town', 'Bradford City', 'Carlisle United', 'Salford City', 'Swindon Town', 'Tranmere Rovers', 'Grimsby Town', 'Barrow', 'Doncaster Rovers', 'Crewe Alexandria', 'Sutton United', 'Walsall', 'Stockport County', 'AFC Wimbledon', 'Gillingham', 'Newport County AFC', 'Harrowgate Town', 'Rochdale', 'Colchester United', 'Crawley Town', 'Hartlepool United']
}

league_choice = {1: 'Premier League', 2: 'Championship', 3: 'League 1', 4: 'League 2'}

league_averages = [80, 70, 60, 50]
team_variation = 3
match_variation = 10
score_weights = [10, 5, 2, 1] # 1 goal, 2, 3, 4

def stat_generator(league):
    stat = int(random.normalvariate(league_averages[league], team_variation))
    
    if stat > 100:
        stat = 100
    elif stat < 10:
        stat = 10
        
    return stat

def investment(money_left, ):
    print(f'You have {money_left} avaliable to spend, how much to you want to invest?')
    money_input_num = int(input('Please input your amount: '))
    print()
    
    while not 0 <= money_input_num <= money_left:
        print(f'Error! Please input a number from 0 to {money_left} (inclusive)')
        print()
        moeny_input_num = int(input('Please input your amount: '))
        print()

def matchday_sim(matchday_num, fix_list, league_table, league_stats, player_team):
    results = f''
    for fix in fix_list[matchday_num]:
        team1, team2 = fix[0], fix[1]
        
        diff = league_stats[team1].total - league_stats[team2].total
        
        winner = random.normalvariate(diff, match_variation)
        
        if winner < -5:
            #team1 wins the match
            team1_score = random.choices(population=[1,2,3,4], weights=score_weights, k=1)[0] #winner
            team2_score = random.randint(0, team1_score-1)
            
            league_table[team1] += 3
            league_table[team2] += 0
            
        elif -5 <= winner < 5:
            team1_score = random.choices(population=[1,2,3,4], weights=score_weights, k=1)[0]
            team2_score = team1_score
            
            league_table[team1] += 1
            league_table[team2] += 1
            
        else:
            #team2 wins the match
            team2_score = random.choices(population=[1,2,3,4],weights=score_weights, k=1)[0] #winner
            team1_score = random.randint(0, team2_score-1)
            
            league_table[team1] += 0
            league_table[team2] += 3
            
        if player_team in [team1, team2]:
            results += f"{team1} v {team2} : {team1_score} - {team2_score}  <------ YOUR TEAM\n"
        else:
            results += f"{team1} v {team2} : {team1_score} - {team2_score}\n"
    
    return results
    
class team:
    def __init__(self, league):
        self.manager = stat_generator(league)
        self.squad = stat_generator(league)
        self.facilities = stat_generator(league)
        self.total = self.manager + self.squad + self.facilities

run_sim = True

print('================================================================')
print('Welcome to my English Football Simulator! Soon to replace FM2022\n')
print('The first thing you need to do is select a league to run a club in:')
print('Input 1 for the Premier League, 2 for the Championship, 3 for League 1 and 4 for League 2.')


league_input_num = int(input('Please input your choice: '))
print()

while league_input_num not in [1,2,3,4]:
    print('Error! Please input a number from 1 to 4 (inclusive)')
    print()
    league_input_num = int(input('Please input your choice: '))
    print()
    
chosen_league_name = league_choice[league_input_num]
chosen_league_teams = leagues[chosen_league_name]
    
print('================================================================')
print(f'Good choice!, you chose: {chosen_league_name}\n')

print('Now you need to choose a team in that league to manage.\n')
print(f'Your choices are: {leagues[chosen_league_name]}\n')
print('Make sure to write your choice exactly as it is written in the list above!')

player_team = input('Please input your choice: ')
print()

while player_team not in chosen_league_teams:
    print('Error! Please input a team in the list of teams in your chosen league!')
    print()
    player_team = input('Please input your choice: ')
    print()
    


playing = True
while playing:
    
    print('================================================================')
        
    if player_team != 'Preston North End':
        print(f'A great choice, you chose: {player_team} :)\n')
    else:
        print('I cannot believe you chose them, you have poor taste in football teams for sure.\n')
        
    print("These are your team's stats, they are ranked out of 100 each, where the higher the number the better.")
    print('These individual stats are then added together to give an overall rating for your team.\n')

    # Generate the rest of the teams stats in the league.
    league_stats = {team_name: team(league_input_num-1) for team_name in chosen_league_teams}
    # Select the stats for our team
    team_stats = league_stats[player_team]

    print(f"Manager: {team_stats.manager}\nSquad: {team_stats.squad}\nFacilities: {team_stats.facilities}\nTotal: {team_stats.total}\n")

    print('For reference the average total rating for your league is:', 3 * league_averages[league_input_num-1], '\n')

    print('================================================================')

    # This piece of code generates the fixture list.
    teams = random.sample(chosen_league_teams, len(chosen_league_teams))

    matches = []
    return_matches = []
    fixtures = []

    for fixture in range(1, len(chosen_league_teams)):

        for i in range(int(len(chosen_league_teams)/2)):
            matches.append((teams[i], teams[len(chosen_league_teams) - 1 - i]))
            return_matches.append((teams[len(chosen_league_teams) - 1 - i], teams[i]))
            
        teams.insert(1, teams.pop())
        fixtures.insert(int(len(fixtures)/2), matches)
        fixtures.append(return_matches)
        matches = []
        return_matches = []

            
    # Initialise league table:
    table = {team_name: 0 for team_name in chosen_league_teams}

    print('Ready for the league to start??')
    print()
    input('Press any button to simulate the first matchday of the season!\n')
 
    for matchday in range(1, len(chosen_league_teams)*2 - 1):
        print('================================================================')
        print(f'Matchday {matchday}\n')
        print('The results for this matchday are: ')
        
        res = matchday_sim(matchday - 1, fixtures, table, league_stats, player_team)
        
        print(res)
        
        user_choice = input('Hit enter to go to the next matchday, or input L to see the league table or X to exit:\n')
        
        if user_choice.upper() not in ['L', 'X']:
            continue
        elif user_choice.upper() == 'L':
            print()
            print('The league table is as follows: \n')
            counter = 1
            
            for name, points in sorted(table.items(), key=lambda item: item[1], reverse=True):
                print(f'{counter}. {name} - {points} points.')
                counter += 1
            
            input('\nHit enter to go to the next matchday.\n')
        else:
            exit()
    
    print('================================================================')
    print('================================================================')
    print('================================================================')
    
    counter = 1
    postion = 1
    for name, points in sorted(table.items(), key=lambda item: item[1], reverse=True):
        if name == player_team:
            position = counter
            break
        counter += 1
        
    if position not in [1, 2, 3, 21, 22, 23]:
        position_string = f'{position}th'
    elif position == 1:
            position_string = f'1st'
    elif position == 2:
            position_string = f'2nd'
    elif position == 3:
            position_string = f'3rd'
    elif position == 21:
            position_string = f'21st'
    elif position == 22:
            position_string = f'22nd'
    elif position == 23:
            position_string = f'23rd'
    
    print(f'The season is now over, your team {player_team} finished in {position_string} position.\n')
    print("The final league standings are as follows: \n")
    
    print('The league table is as follows: \n')
    counter = 1
    
    for name, points in sorted(table.items(), key=lambda item: item[1], reverse=True):
        print(f'{counter}. {name} - {points} points.')
        counter += 1
        
    print("\nThanks for playing, do you want to play again? If so hit enter, if not type 'X'")
    
    if input().upper() == 'X':
        playing = False

