
import numpy as np
import abo_omar
def om_omar_func():
    abo_omar.omar_list = np.random.randint(100, 200, 15)
    om_omar_list = abo_omar.omar_list
    print(om_omar_list)
    return om_omar_list
om_omar_list = om_omar_func()
