import random

leagues = {
    'Premier League': ['Arsenal','Aston Villa','Brighton and Hove Albion','Burnley','Chelsea','Crystal Palace','Everton','Fulham','Leeds United','Liverpool','Leicester City','Manchester City','Manchester United','Newcastle United','Sheffield United','Southampton','Tottenham Hotspur','West Bromwich Albion','West Ham United','Wolverhampton Wanderers'],
    'Championship': ['Birmingham City', 'Blackburn Rovers', 'Blackpool', 'Bristol City', 'Burnley', 'Cardiff City', 'Coventry City', 'Huddersfield Town', 'Hull City', 'Luton Town', 'Middlesbrough', 'Millwall', 'Norwich City', 'Preston North End', 'Queens Park Rangers', 'Reading', 'Rotherham', 'Sheffield United', 'Stoke City', 'Sunderland', 'Swansea City', 'Watford', 'West Bromich Albion', 'Wigan'],
    'League 1': ['Plymouth Argyle', 'Ipswich Town', 'Sheffield Wednesday', 'Petersborough United', 'Portsmouth', 'Barnsley', 'Bolton Wanderers', 'Shrewsbury Town', 'Derby County', 'Charlton Athletic', 'Exeter City', 'Bristol Rovers', 'Wycombe Wanderers', 'Lincoln City', 'Fleetwood Town', 'Port Vale', 'Accrington Stanley', 'Cambridge United', 'Oxford United', 'Cheltenham Town', 'Forest Green Rovers', 'Milton Keynes Dons', 'Burton Albion', 'Morecambe'],
    'League 2': ['Stevenage', 'Leyton Orient', 'Northampton Town', 'Mansfield Town', 'Bradford City', 'Carlisle United', 'Salford City', 'Swindon Town', 'Tranmere Rovers', 'Grimsby Town', 'Barrow', 'Doncaster Rovers', 'Crewe Alexandria', 'Sutton United', 'Walsall', 'Stockport County', 'AFC Wimbledon', 'Gillingham', 'Newport County AFC', 'Harrowgate Town', 'Rochdale', 'Colchester United', 'Crawley Town', 'Hartlepool United']
}

league_choice = {1: 'Premier League', 2: 'Championship', 3: 'League 1', 4: 'League 2'}

league_averages = [80, 60, 40, 20]
variation = 10

def stat_generator(league):
    stat = int(random.normalvariate(league_averages[league], variation))
    
    if stat > 100:
        stat = 100
    elif stat < 10:
        stat = 10
        
    return stat
    
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

while run_sim:
    
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
        league_input_num = input('Please input your choice: ')
        print()
        
    print('================================================================')
    if player_team != 'Preston North End':
        print(f'A great choice, you chose: {player_team} :)\n')
    else:
        print('I cannot believe you chose them, you have poor taste in football teams for sure.\n')
        
    print("These are your team's stats, they are ranked out of 100 each, where the higher the number the better.")
    print('These individual stats are then added together to give an overall rating for your team.\n')
    
    team_stats = team(league_input_num-1)
    
    print(f"Manager: {team_stats.manager}\nSquad: {team_stats.squad}\nFacilities: {team_stats.facilities}\nTotal: {team_stats.total}\n")
    
    print('================================================================')
    print('For reference the average total rating for your league would be:', 3 * league_averages[league_input_num-1])
    
    
    
    
    run_sim = False
