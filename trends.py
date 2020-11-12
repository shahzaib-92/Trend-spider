import pandas as pd
import data_saver
import webbrowser
from pathlib import Path


def show():
    data_saver.save_csv()

    file = pd.read_csv("data.csv")
    file.to_html("trends.html")
    webbrowser.open(Path("trends.html"))


# if you want to see trends list in browser than call this function.
show()
