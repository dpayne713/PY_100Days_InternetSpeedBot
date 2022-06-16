
import time

# TODO
# 1. Import Selenium
# 2. Run Speed test wait for 1 minute for test to run
# 3. Download CSV file on "results" page
# 4. Add to local CSV File

# Additional Todo
# 1. Compare CSV files for inconsistency
# 2. Setup tweet bot ??


from speed_test import SpeedTest
from file_management import FileManagement
speed = SpeedTest()
data = speed.run_test()

time.sleep(1)
file_management = FileManagement()
file_management.move_file()

file_management.add_reading()


