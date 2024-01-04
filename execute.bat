@echo off

REM Save Top Comments
python save_top_comments.py

REM Extract Player Names
python extract_player_names.py

REM Filter Player Names
python filter_player_names.py

REM Get Top Three Players
python top_three_players.py

REM Generate Graph
python players_graph.py

