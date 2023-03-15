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
            "game_id": self.match_id,
            "player_id": self.player_id,
            "hero_id": self.hero_id,
            "g_kills;": self.kills,
            "g_deaths": self.deaths,
            "g_assists": self.assists,
            "g_last_hits": self.last_hits,
            "Denies": self.denies,
            "g_gpm": self.gpm,
            "g_xpm": self.xpm,
            "g_hero_damage": self.hero_damage,
            "g_tower_damage": self.tower_damage,
            "g_hero_healing": self.hero_healing,
            "g_level": self.level,
            "g_win": self.win,
        }
