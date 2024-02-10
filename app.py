"""This project was created simply for the purpose of learning how to use Github Actions
    We will eventually, at two endpoints:
    1. GET endpoint for returning the default data.
    2. POST endpoint that accepts two list, generates a DataFrame and return it as a dict.
"""

import pandas as pd

DEFAULT_LIST_1 = ["Geeks", "For", "Geeks", "is", "portal", "for", "Geeks"]
DEFAULT_LIST_2 = [11, 22, 33, 44, 55, 66, 77]
DEFAULT_COLUMNS = ["Name", "val"]


def convert_two_lists_to_df(
    list_1=None,
    list_2=None,
    columns=None,
) -> pd.DataFrame:
    """Create a pandas DataFrame that combines two lists"""
    list_1 = list_1 or DEFAULT_LIST_1
    list_2 = list_2 or DEFAULT_LIST_2
    columns = columns or DEFAULT_COLUMNS
    return pd.DataFrame(list(zip(list_1, list_2)), columns=columns)


if __name__ == "__main__":
    print(convert_two_lists_to_df())
