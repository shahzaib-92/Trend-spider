import spider
import csv

# get the list of trends and save it in a csv file


def save_csv():
    trend_list = spider.trendList()
    with open("data.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Trends List"])
        for trend in trend_list:
            writer.writerow([trend])


# if you just want to store trends in a csv file than call the below fuction only.
# save_csv()
