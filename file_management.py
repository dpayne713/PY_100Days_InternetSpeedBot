import os
import time
import csv


class FileManagement:
    def __init__(self):
        self.download_dir_path = "/Users/davidpayne/Downloads"
        self.csv_dir_path = './CSV_Files'

        self.date = time.strftime("%Y_%m_%d")
        self.today_file = f"Speedtest Results Export-{self.date}.csv"

    def move_file(self):
        files = os.listdir(self.download_dir_path)
        if self.today_file in files:
            os.replace(f"{self.download_dir_path}/{self.today_file}", f"{self.csv_dir_path}/{self.today_file}")
            return

    def add_reading(self):
        with open('./CSV_Files/composite/composite.csv', 'a') as composite_file:
            composite_file = csv.writer(composite_file)

            with open(f'./CSV_Files/{self.today_file}', 'r') as today_file:
                today_file = list(csv.reader(today_file))[1:]
                composite_file.writerows(today_file)

            os.remove(f"{self.csv_dir_path}/{self.today_file}")


