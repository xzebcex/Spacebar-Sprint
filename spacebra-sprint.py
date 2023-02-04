# Spacebar Sprint.


import sys
import time


print('Use "Spacebar and Tab keys to play" and "ctl+c" to quit')
start = input('Press Enter to play: ')
indent = 0  # How many spaces to indent.
indent_increasing = True  # Whether the indentation is incresing or not.

try:
    while True:  # Main loop.
        print('' * indent, end='')
        print('*******')
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if indent_increasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 20:
                # Change direction:
                indent_increasing = False

        else:
            # Decrease the number of spaces:
            indent -= 1

            if indent == 0:
                # Change direction:
                indent_increasing = True

except:
    sys.exit()
