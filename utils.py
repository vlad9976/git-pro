import os
import platform
from tqdm import tqdm
import time

def file():
    SCORES_FILE_NAME = "Scores.txt"
    return SCORES_FILE_NAME


def bad_code():
    BAD_RETURN_CODE = 404
    return BAD_RETURN_CODE


def cls_screen():
    # Check the operating system and clear the screen accordingly
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')



def load_game_assets():
    total_assets = 100  # Total number of assets to load

    # Create a tqdm instance with the total number of assets
    with tqdm(total=total_assets, desc="Loading Game", bar_format="{l_bar}{bar}{r_bar}") as pbar:
        for asset_id in range(total_assets):
            # Simulate loading an asset
            time.sleep(0.05)
            # Update the progress bar
            pbar.update(1)

