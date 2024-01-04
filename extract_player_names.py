import re
def extract_player_names(comment_text):
    player_name_pattern = re.compile(r'\b(?:[A-Z][a-z]*\s?)+\b')
    matches = player_name_pattern.findall(comment_text)
    return matches 





