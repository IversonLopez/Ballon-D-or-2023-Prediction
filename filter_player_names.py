import re

ip_files = ("player_names_2023.txt",)
op_files = ("filtered_player_names_2023.txt",)

player_name_pattern = re.compile(r'\b(?:[A-Z][a-z]*\s?)+\b')

for ip_file, op_file in zip(ip_files, op_files):
    with open(ip_file) as ipf, open(op_file, 'w') as opf:
        for line in ipf:
            if re.fullmatch(r'\s+', line):
                continue
            matches = player_name_pattern.findall(line)
            for match in matches:
                opf.write(match + "\n")