import argparse
from datetime import datetime, date
import os
import pickle


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_folder",
        type=str,
        help=(
            "Full path to the directory having all the cars images. Already "
            "splitted in train/test sets. E.g. "
            "`/home/app/src/data/car_ims_v1/`."
        ),
    )
    args = parser.parse_args()
    return args


def walkdir(folder):
    """
    Walk through all the files in a directory and its subfolders.

    Parameters
    ----------
    folder : str
        Path to the folder you want to walk.

    Returns
    -------
        For each file found, yields a tuple having the path to the file
        and the file name.
    """
    for dirpath, _, files in os.walk(folder):
        for filename in files:
            yield (dirpath, filename)


def timer(start_time=None):
    """
    This function calculate the time between two points: Start Time and Timer.

    Parameters
    ----------
        Start time: given datetime or None (now as default).

    Returns
    -------
        Time taken by function in hours (integer), mins(integer) and secs (integer).
    """
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        hour, temp_sec = divmod(
            (datetime.now() - start_time).total_seconds(), 3600
        )
        min, sec = divmod(temp_sec, 60)
        print(
            f"Time taken by function: {int(hour)} hours , {int(min)} mins and {int(sec)} secs"
        )


def save_data_checkpoint(filename, path):
    """
    Save picklable object to destination path.

    Parameters
    ----------
    filename : pickable obj
        name of the picklable objetc to save.

    path : str
        full path of destination directory.

    Returns
    -------
        Confirmation message.
    """
    if not os.path.exists(path):
        with open(path, "wb") as f:
            pickle.dump(filename, f, protocol=pickle.HIGHEST_PROTOCOL)
    return print(f"Object saved successfully in {path}.")


def load_data_checkpoint(path):
    """
    Load picklable object from destination path.

    Parameters
    ----------
    filename : str
        name of the picklable objetc to save.

    path : str
        full path of destination directory.

    Returns
    -------
        Confirmation message.
    """
    if os.path.exists(path):
        with open(path, "rb") as f:
            filename = pickle.load(f)
            print(f"Object loaded successfully from {path}.")
            return filename
    else:
        return print(f"Object or {path} does not exist.")
