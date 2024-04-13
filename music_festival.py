#Task 1

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for artist in artist_names:
    if artist in unique_artists:
        print(artist, "is already in the festival!")
    else:
        unique_artists.add(artist)
print(unique_artists)