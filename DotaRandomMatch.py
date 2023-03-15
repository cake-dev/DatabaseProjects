import pandas as pd
import numpy as np
import random
from SinglePerformance import SinglePerformance

# FIXME: need to get the correct data from the database (i've changed it post insert)

dota_players = pd.read_csv("data/dota_players.csv")
dota_teams = pd.read_csv("data/dota_teams.csv")
dota_heroes = pd.read_csv("data/dota_heroes.csv")
hero_stats = pd.read_csv("data/hero_stats.csv")

# TODO fix hero_stats index (the script goes out of bounds when selecting a random hero SOMETIMES (index 119))

# a function to create random match data. it accepts 2 arrays of player ids. it returns a list of 10 SinglePerformance objects. The hero ids are randomly selected from the list of heroes, and if a hero has already been chosen, choose a new one. The stats are generated based on the hero values in hero_stats.
def create_random_match(players1, players2, match_id):
    # drop players if there are more than 5
    if len(players1) > 5:
        players1 = players1[:5]
    if len(players2) > 5:
        players2 = players2[:5]

    # match_id = random.randint(100000, 999999)
    performances = []
    for player in players1:
        # select a random hero
        hero_id = random.choice(dota_heroes["HERO_ID"].values)
        while hero_id in [x.hero_id for x in performances]:
            hero_id = random.choice(dota_heroes["HERO_ID"].values)
        kills = random.randint(
            hero_stats.loc[hero_id]["Kills_Min"], hero_stats.loc[hero_id]["Kills_Max"]
        )
        deaths = random.randint(
            hero_stats.loc[hero_id]["Deaths_Min"], hero_stats.loc[hero_id]["Deaths_Max"]
        )
        assists = random.randint(
            hero_stats.loc[hero_id]["Assists_Min"],
            hero_stats.loc[hero_id]["Assists_Max"],
        )
        last_hits = random.randint(
            hero_stats.loc[hero_id]["LH_Min"], hero_stats.loc[hero_id]["LH_Max"]
        )
        denies = random.randint(
            hero_stats.loc[hero_id]["Denies_Min"], hero_stats.loc[hero_id]["Denies_Max"]
        )
        gpm = random.randint(
            hero_stats.loc[hero_id]["GPM_Min"], hero_stats.loc[hero_id]["GPM_Max"]
        )
        xpm = random.randint(
            hero_stats.loc[hero_id]["XPM_Min"], hero_stats.loc[hero_id]["XPM_Max"]
        )
        hero_damage = random.randint(
            hero_stats.loc[hero_id]["HD_Min"], hero_stats.loc[hero_id]["HD_Max"]
        )
        tower_damage = random.randint(
            hero_stats.loc[hero_id]["TD_Min"], hero_stats.loc[hero_id]["TD_Max"]
        )
        hero_healing = random.randint(
            hero_stats.loc[hero_id]["HH_Min"], hero_stats.loc[hero_id]["HH_Max"]
        )
        level = random.randint(
            hero_stats.loc[hero_id]["LVL_Min"], hero_stats.loc[hero_id]["LVL_Max"]
        )
        win = -1

        performances.append(
            SinglePerformance(
                match_id,
                player,
                hero_id,
                kills,
                deaths,
                assists,
                last_hits,
                denies,
                gpm,
                xpm,
                hero_damage,
                tower_damage,
                hero_healing,
                level,
                win,
            )
        )

    for player in players2:
        # select a random hero
        hero_id = random.choice(dota_heroes["HERO_ID"].values)
        while hero_id in [x.hero_id for x in performances]:
            hero_id = random.choice(dota_heroes["HERO_ID"].values)
        kills = random.randint(
            hero_stats.loc[hero_id]["Kills_Min"], hero_stats.loc[hero_id]["Kills_Max"]
        )
        deaths = random.randint(
            hero_stats.loc[hero_id]["Deaths_Min"], hero_stats.loc[hero_id]["Deaths_Max"]
        )
        assists = random.randint(
            hero_stats.loc[hero_id]["Assists_Min"],
            hero_stats.loc[hero_id]["Assists_Max"],
        )
        last_hits = random.randint(
            hero_stats.loc[hero_id]["LH_Min"], hero_stats.loc[hero_id]["LH_Max"]
        )
        denies = random.randint(
            hero_stats.loc[hero_id]["Denies_Min"], hero_stats.loc[hero_id]["Denies_Max"]
        )
        gpm = random.randint(
            hero_stats.loc[hero_id]["GPM_Min"], hero_stats.loc[hero_id]["GPM_Max"]
        )
        xpm = random.randint(
            hero_stats.loc[hero_id]["XPM_Min"], hero_stats.loc[hero_id]["XPM_Max"]
        )
        hero_damage = random.randint(
            hero_stats.loc[hero_id]["HD_Min"], hero_stats.loc[hero_id]["HD_Max"]
        )
        tower_damage = random.randint(
            hero_stats.loc[hero_id]["TD_Min"], hero_stats.loc[hero_id]["TD_Max"]
        )
        hero_healing = random.randint(
            hero_stats.loc[hero_id]["HH_Min"], hero_stats.loc[hero_id]["HH_Max"]
        )
        level = random.randint(
            hero_stats.loc[hero_id]["LVL_Min"], hero_stats.loc[hero_id]["LVL_Max"]
        )
        win = -1

        performances.append(
            SinglePerformance(
                match_id,
                player,
                hero_id,
                kills,
                deaths,
                assists,
                last_hits,
                denies,
                gpm,
                xpm,
                hero_damage,
                tower_damage,
                hero_healing,
                level,
                win,
            )
        )

    # set the team with the least deaths as the winning team
    if sum([x.deaths for x in performances[:5]]) > sum(
        [x.deaths for x in performances[5:]]
    ):
        for performance in performances[5:]:
            performance.win = 1
        for performance in performances[:5]:
            performance.win = 0
    else:
        for performance in performances[:5]:
            performance.win = 1
        for performance in performances[5:]:
            performance.win = 0

    for performance in performances:
        performances[performances.index(performance)] = performance.get_info()
    return pd.DataFrame(performances)


def assemble_team_data():
    # create a dataframe of dataframes for each team_name in dota_players
    team_dataframes = {}
    for team_name in dota_players["team_name"].unique():
        team_dataframes[team_name] = dota_players[
            dota_players["team_name"] == team_name
        ]
    # get a subframe of all teams with at least 5 players
    team_dataframes_5 = {k: v for k, v in team_dataframes.items() if len(v) >= 5}
    return team_dataframes_5


# a function to select 2 random teams from team_names, then create a random match between their players
def create_random_match_data(t_n, t_d_5, match_id):
    # select 2 random teams
    team1 = random.choice(t_n)
    team2 = random.choice(t_n)
    while team1 == team2:
        team2 = random.choice(t_n)

    # create a random match between the 2 teams
    randommatch = create_random_match(
        t_d_5[team1]["p_id"].values, t_d_5[team2]["p_id"].values, match_id
    )

    return randommatch


# main method
def main():
    # get a dataframe of all teams with at least 5 players
    team_dataframes_5 = assemble_team_data()

    # get a list of all team names
    team_names = list(team_dataframes_5.keys())

    # create a dataframe of random matches
    random_matches = pd.DataFrame()
    match_ids = np.arange(1, 11)
    for i in range(len(match_ids)):
        random_matches = random_matches.append(
            create_random_match_data(team_names, team_dataframes_5, match_ids[i])
        )

    # write the random matches to a csv file
    random_matches.to_csv("random_matches.csv", index=False)


if __name__ == "__main__":
    main()
