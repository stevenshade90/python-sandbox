# The humidity detector is plugged in, and the program executes
# A loop begins, and the detector takes a reading, and that reading is converted to maybe a .2f
# The current rating is displayed and added to a list
# The reader is set to sample every 15 seconds -- at the end of each 15 sec interval, the rating is displayed and the value
#   is added to the list
# When the program terminates or maybe ends after a set period of time, the results are plotted -- Eventually this will
#   need to be modified depending on the length of the sampling time
#   matplotlib for this probably
# Use Random for now to simulate data

import matplotlib.pyplot as plt
import math
import random

from time import *


humidity_samples = []
average_humidity_samples = []


while len(humidity_samples) < 100:
    try:
        current_humidity = random.uniform(50, 60)  # but eventually <unit_gathering_humidity> return its data
        humidity_samples.append(current_humidity)

        average_humidity = math.ceil(sum(humidity_samples)/len(humidity_samples))
        average_humidity_samples.append(average_humidity)

        print(f'Current Humidity: {humidity_samples[-1]:.2f}% | Average Humidity: {average_humidity}%')
        sleep(1)

    except KeyboardInterrupt:
        print('Data gathering interrupted, displaying data...')


fig, ax = plt.subplots()
plt.title('Current Humidity and Averages', fontsize=24)
ax.set_xlabel('Time', fontsize=20)
ax.set_ylabel('Humidity %', fontsize=20)

ax.plot(humidity_samples, c='red')
ax.plot(average_humidity_samples, c='blue')

plt.show()