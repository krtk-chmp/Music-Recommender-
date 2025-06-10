# Basic Python practice
song_features = {"artist": "ABBA", "song": "She's My Kind of Girl", "plays": 100}
print(f"Song: {song_features['song']} by {song_features['artist']}")

for i in range(3):
    print(f"Play count: {song_features['plays'] * (i + 1)}")

def add_play(count):
    try:
        return count + 50
    except TypeError:
        return "Error: Invalid count"

print(f"New play count: {add_play(song_features['plays'])}")