from rapidfuzz import fuzz

def identify_top_players(ip_file, op_file):
    print(f"Input File: {ip_file}")
    print(f"Output File: {op_file}")
    try:
        player_names = {}

        with open(ip_file) as ipf:
            for line in ipf:
                name = line.rstrip('\n')

                # Skips/filters out unwanted words 
                if name.lower() in {'cup', 'i', "wc", "world cup", "he", "it", "ballon d", "ucl", "argentina"}:
                    continue

                player_names[name] = player_names.get(name, 0) + 1

        fuzzed_names = {}
        for k1 in sorted(player_names, key=lambda k: -player_names[k]):
            s1 = k1.lower().replace('.', '')
            for k2 in fuzzed_names:
                s2 = k2.lower().replace('.', '')
                if round(fuzz.ratio(s1, s2)) >= 90:
                    fuzzed_names[k2] += player_names[k1]
                    break
            else:
                fuzzed_names[k1] = player_names[k1]

        with open(op_file, 'w') as opf:
            opf.write(f'Player,Votes\n')
            count = 0  # counter to track the top players
            for name in sorted(fuzzed_names, key=lambda k: -fuzzed_names[k]):
                votes = fuzzed_names[name]
                opf.write(f'{name},{votes}\n')
                count += 1
                if count == 3:  # only top three players
                    break
    except Exception as e:
        print(f"An error occurred: {e}") #to show any actual error


identify_top_players('filtered_player_names_2023.txt', 'top_players_2023.csv')