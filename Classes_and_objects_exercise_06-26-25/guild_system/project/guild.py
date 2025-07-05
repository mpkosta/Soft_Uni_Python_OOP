from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = next((p for p in self.players if p.name == player_name), None)
        if player is None:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        player.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."


    def guild_info(self):
        return (f"Guild: {self.name}\n" +
                ''.join(p.player_info() for p in self.players))
