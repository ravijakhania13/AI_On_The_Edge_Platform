import numpy as np
import sys
sys.path.insert (0, '../../')
sys.path.insert (0, '../../../')
from RabbitMQ.message_queue import *
import time
RMQ = RabbitMQ()

l = ["Iris-Setosa", "Iris-Virginica", "Iris-Versicolor"]
for i in range(20):
    itr = np.random.randint(0, 3)
    RMQ.send('', "helper_test", str(l[itr]))
    time.sleep(2)

