class team():
    def __init__(self, team_name):
        self.team_name = team_name


class players(team):
    def __init__(self, first_name, last_name, age):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.players_team_name = self.team_name


class kit(team):
    def __init__(self, team_name, home_or_away):
        super(kit, self).__init__(team_name)
        self.home_or_away = home_or_away
        self.kit_color = ""

    def choose_kit(self):
        if self.home_or_away == "home":
            if self.team_name == "pakistan":
                self.kit_color = "green"
        elif self.home_or_away == "away":
            if self.team_name == "pakistan":
                self.kit_color = "yellow"
        else:
            self.kit_color = "unknown"

        return self.kit_color


kit = kit("pakistan", "home")
print(kit)

