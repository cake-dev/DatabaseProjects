# a class to store single performance data
class SinglePerformance:
    def __init__(
        self,
        match_id,
        player_id,
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
    ):
        self.match_id = match_id
        self.player_id = player_id
        self.hero_id = hero_id
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.last_hits = last_hits
        self.denies = denies
        self.gpm = gpm
        self.xpm = xpm
        self.hero_damage = hero_damage
        self.tower_damage = tower_damage
        self.hero_healing = hero_healing
        self.level = level
        self.win = win

    def get_info(self):
        return {
            "Match": self.match_id,
            "Player": self.player_id,
            "Hero": self.hero_id,
            "Kills": self.kills,
            "Deaths": self.deaths,
            "Assists": self.assists,
            "Last_Hits": self.last_hits,
            "Denies": self.denies,
            "GPM": self.gpm,
            "XPM": self.xpm,
            "Hero_Damage": self.hero_damage,
            "Tower_Damage": self.tower_damage,
            "Hero_Healing": self.hero_healing,
            "Level": self.level,
            "Win": self.win,
        }
