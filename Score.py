from Utils import SCORES_FILE_NAME


def add_score(dif_game):
    try:
        with open(SCORES_FILE_NAME, "r+") as f:
            user_score = int(f.readline())
            POINTS_OF_WINNING = user_score + (dif_game * 3) + 5
            f.write(POINTS_OF_WINNING)
    except:
        with open(SCORES_FILE_NAME, "a+") as f:
            POINTS_OF_WINNING = (dif_game * 3) + 5
            f.write(POINTS_OF_WINNING)
