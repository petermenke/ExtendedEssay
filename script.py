import Microphone.script_mic as mic
import Webcam.script_cam as cam
import Speed.script_speed as speed
import PRNG.script_PRNG as PRNG
import Heat.script_heat as heat

import time

arr = [heat]

for t in arr:
    # Begin
    start_time = int(round(time.time() * 1000))
    print 'Beginning ' + t.name()

    # Collect Data #
    t_arr = t.collect(1000)

    # Finishing
    end_time = int(round(time.time() * 1000))
    elapsed = end_time - start_time
    print 'Elapsed Time (ms): ' + str(elapsed)

    # Write to file
    f = open(t.name() + '_output.txt', 'w')
    for i in t_arr:
        f.write(str(i) + '\n')
    f.close()
