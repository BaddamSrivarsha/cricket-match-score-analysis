class Player:
    def __init__(self, name):  # Corrected constructor name
        self.name = name
        self.runs = 0
        self.wickets = 0
        self.balls_faced = 0
        self.balls_bowled = 0
    
    def add_runs(self, runs):
        self.runs += runs
    
    def add_wickets(self, wickets):
        self.wickets += wickets
    
    def add_balls_faced(self, balls):
        self.balls_faced += balls
    
    def add_balls_bowled(self, balls):
        self.balls_bowled += balls
    
    def batting_average(self):
        if self.balls_faced == 0:  # Prevent division by zero
            return 0
        return round(self.runs / self.balls_faced * 100, 2)  # Runs per 100 balls faced
    
    def bowling_average(self):
        if self.wickets == 0:  # Prevent division by zero
            return 0
        return round(self.balls_bowled / self.wickets, 2)  # Balls per wicket

    def player_summary(self):
        return f"{self.name}: Runs: {self.runs}, Wickets: {self.wickets}, Balls Faced: {self.balls_faced}, Balls Bowled: {self.balls_bowled}, Batting Average: {self.batting_average()}, Bowling Average: {self.bowling_average()}"


class CricketMatch:
    def __init__(self, team_name):  # Corrected constructor name
        self.team_name = team_name
        self.runs = 0
        self.wickets = 0
        self.overs = 0.0
        self.extras = {"wides": 0, "no_balls": 0, "leg_byes": 0}
        self.players = {}  # Dictionary to store players

    def add_player(self, player_name):
        self.players[player_name] = Player(player_name)
    
    def update_score(self, runs, wickets, overs, player_name=None, extras=None):
        if extras is None:
            extras = {}  # Ensure extras is always a dictionary if not provided

        self.runs += runs
        self.wickets += wickets
        self.overs += overs
        self.extras["wides"] += extras.get("wides", 0)
        self.extras["no_balls"] += extras.get("no_balls", 0)
        self.extras["leg_byes"] += extras.get("leg_byes", 0)
        
        # Update player statistics if player_name is provided
        if player_name:
            if player_name not in self.players:
                self.add_player(player_name)  # Add player if not already present
            self.players[player_name].add_runs(runs)
            self.players[player_name].add_wickets(wickets)
    
    def calculate_run_rate(self):
        if self.overs == 0:
            return 0
        return round(self.runs / self.overs, 2)
    
    def get_match_summary(self):
        summary = f"{self.team_name} - Runs: {self.runs}, Wickets: {self.wickets}, Overs: {self.overs}, Run Rate: {self.calculate_run_rate()}, Extras: {self.extras}"
        player_summaries = "\n".join([player.player_summary() for player in self.players.values()])
        return f"{summary}\n{player_summaries}"


class MatchAnalysis:
    def __init__(self, team1_name, team2_name):  # Corrected constructor name
        self.team1 = CricketMatch(team1_name)
        self.team2 = CricketMatch(team2_name)
    
    def update_team_score(self, team_name, runs, wickets, overs, player_name=None, extras=None):
        if extras is None:
            extras = {}  # Ensure extras is always a dictionary if not provided
            
        if team_name == self.team1.team_name:
            self.team1.update_score(runs, wickets, overs, player_name, extras)
        elif team_name == self.team2.team_name:
            self.team2.update_score(runs, wickets, overs, player_name, extras)
        else:
            print("Invalid team name.")
    
    def display_summary(self):
        print(self.team1.get_match_summary())
        print(self.team2.get_match_summary())
    
    def match_winner(self):
        if self.team1.runs > self.team2.runs:
            return f"{self.team1.team_name} wins!"
        elif self.team2.runs > self.team1.runs:
            return f"{self.team2.team_name} wins!"
        else:
            return "It's a draw!"
    
    def match_progression(self):
        print(f"Match Progress:\n{self.team1.team_name} vs {self.team2.team_name}")
        print(f"Team 1: Runs: {self.team1.runs}, Wickets: {self.team1.wickets}, Overs: {self.team1.overs}")
        print(f"Team 2: Runs: {self.team2.runs}, Wickets: {self.team2.wickets}, Overs: {self.team2.overs}")


# Example usage:
match = MatchAnalysis("Team A", "Team B")

# Team A updates (player performance, extras)
match.update_team_score("Team A", 150, 3, 20.0, "Player 1", {"wides": 5, "no_balls": 2, "leg_byes": 3})
match.update_team_score("Team A", 25, 0, 3.5, "Player 2")
match.update_team_score("Team A", 40, 2, 4.0, "Player 3", {"wides": 2})

# Team B updates (player performance, extras)
match.update_team_score("Team B", 145, 5, 20.0, "Player 4", {"wides": 3, "no_balls": 1, "leg_byes": 0})
match.update_team_score("Team B", 30, 1, 3.0, "Player 5")

# Display match summary
match.display_summary()

# Show match progression
match.match_progression()

# Determine winner
print(match.match_winner())
