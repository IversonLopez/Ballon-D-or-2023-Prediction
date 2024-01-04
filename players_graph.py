import csv
import matplotlib.pyplot as plt

with open('top_players_2023.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)


players = [entry['Player'] for entry in data]
votes = [int(entry['Votes']) for entry in data]


plt.bar(players, votes)
plt.xlabel('Players')
plt.ylabel('Votes')
plt.title("Top Ballon D'or Picks")
plt.tight_layout()
plt.show()