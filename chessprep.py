import berserk
from datetime import datetime

# Create API client
token = ''
with open('lichess_token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.Client(session)

start = berserk.utils.to_millis(datetime(2018, 12, 8))
end = berserk.utils.to_millis(datetime(2018, 12, 9))
games = list(client.games.export_by_player('LeelaChess', since=start, until=end, max=300))

game_id = games[0]['createdAt']

print(client.games.export(game_id))