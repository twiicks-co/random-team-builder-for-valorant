import random

#Characters
controllers=['Astra','Brimstone','Harbor','Omen','Viper']
duelists=['Jett','Neon','Phoenix','Raze','Reyna','Yoru']
initiators=['Breach','Fade','Gekko','KAY/O','Skye','Sova']
sentinels=['Chamber','Cypher','Deadlock','Killjoy','Sage']

#WWeapons
tier_a=['Classic','Judge','Guardian','Odin','Spectre']
tier_b=['Ares','Bulldog','Marshal','Ghost','Stinger']
tier_c=['Bucky','Knife','Shorty','Frenzy']
tier_s=['Operator','Phantom','Vandal','Sherif']

#Variables
agents=[]
agents_list=''
player_names=[]
remove_agent=True
add_agent=True

#Set team
players=int(input('How many agents are in your team? => '))
print('...')
for player in range(players):
    player_names.append(input("What's player "+(str(player+1))+' name? => '))
print('...')

#Select agents
print('Select your team roles')
print('c = controllers')
print('d = duelists')
print('i = initiators')
print('s = sentinels')
agent_type=input('Write your choise (cd, is, cdis) => ')
agent_type=agent_type.lower()
print('...')

if 'c' in agent_type:
    for agent in controllers:
        agents.append(agent)
if 'd' in agent_type:
    for agent in duelists:
        agents.append(agent)
if 'i' in agent_type:
    for agent in initiators:
        agents.append(agent)
if 's' in agent_type:
    for agent in sentinels:
        agents.append(agent)

#Show Agents
for agent in agents:
    agents_list=agents_list+'['+agent+'] '
print('Your valorant agents are: ',agents_list)
print('...')

#Remove agents
while remove_agent==True:
    if(input('Do you want to remove an agent? (Yes/No) => ')=='Yes'):
        print('...')
        agents.remove(input('What agent do you want to remove? => '))
        agents_list=''
        for agent in agents:
            agents_list=agents_list+'['+agent+'] '
        print('...')
        print('Now your valorant agents are: ',agents_list)
        print('...')
    else:
        remove_agent=False
        print('...')

#Add agents
while add_agent==True:
    if(input('Do you want to add an agent? (Yes/No) => ')=='Yes'):
        print('...')
        agents.append(input('What agent do you want to add? => '))
        agents_list=''
        for agent in agents:
            agents_list=agents_list+'['+agent+'] '
        print('...')
        print('Now your valorant agents are: ',agents_list)
        print('...')
    else:
        add_agent=False
        print('...')

for player in range(players):
    player_weapons=''
    player_agent=random.choice(agents)
    agents.remove(player_agent)
    print(player_names[player]+' chooses => '+player_agent)
    '''for weapon in range(4):
        player_weapons=player_weapons+'['+random.choice(weapons)+'] '
    print('and uses '+player_weapons)
    print('-'*20)'''