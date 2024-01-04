import json
import praw 
import time
from extract_player_names import extract_player_names


def process_comment(comment, output_file):
    matches = extract_player_names(comment.body)
    for match in matches:
        output_file.write(match + "\n")

    for reply in comment.replies:
        process_comment(reply, output_file)


with open(".secrets/tokens.json") as f:
    secrets = json.load(f)


reddit = praw.Reddit(
    user_agent = secrets["USER_AGENT"],
    client_id = secrets["CLIENT_ID"],
    client_secret = secrets["CLIENT_SECRET"],
)

post_details = (("2023", "134fjip"), ("2023", "167f6p3"))

for year, post_id in post_details:
    submission = reddit.submission(id = post_id)
    submission.comments.replace_more(limit=None)

    op_file = f'player_names_{year}.txt'

    with open(op_file, 'w') as f:
        for top_level_comment in submission.comments:
          process_comment(top_level_comment, f)

    time.sleep(10)



    

    
