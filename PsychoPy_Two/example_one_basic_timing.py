from psychopy import visual, core, event, monitors
import numpy as np
import time
from datetime import datetime

def create_window():
    """Create a PsychoPy window with black background"""
    return visual.Window(
        fullscr=True,
        monitor="testMonitor",
        units="pix",
        color=[0, 0, 0],
        colorSpace='rgb255'
    )

def basic_timing(win):
    """Example 1: Reading keyboard input with timings (part 1)"""
    try:

        # Create instruction text
        instruction = visual.TextStim(
            win=win,
            text="Press any key to respond\n\nYou have 4 seconds to respond",
            pos=(0, 0),
            color=[255, 255, 255],
            colorSpace='rgb255',
            height=30,
            units='pix'
        )
        
        # Draw instruction and flip window
        instruction.draw()
        win.flip()

        # Create a variable that indicates how long we are going to wait for a key press
        trial_duration = 4.0

        # Get start time using both system clock and psychopy
        start_t = core.getTime()
        t1 = datetime.now()
        
        # Display start time
        print(f"Showing keyboard timings using example 1. Timestamp {start_t:.3f}s {t1}")

        # Wait for key press with timeout
        keys = event.waitKeys(maxWait=trial_duration, timeStamped=True)
        
        if keys:  # If a key was pressed before timeout
            resp_t = keys[0][1]  # Get timestamp of the key press
            key_name = keys[0][0]  # Get name of the key pressed
            react_time = resp_t - start_t
            
            # Wait for remaining trial duration if needed
            if react_time < trial_duration:
                core.wait(trial_duration - react_time)
        else:
            react_time = trial_duration
            key_name = "no key"
            
        # Get end time
        t2 = datetime.now()
        
        # Display results
        print(f"Time elapsed for script execution: {(t2-t1).total_seconds():.3f}")
        print(f"You pressed key {key_name} after {react_time:.3f} seconds")

        # Refresh the screen
        win.flip()

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Create window to be used across all examples
        win = create_window()
        basic_timing(win)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        # Ensure window is closed properly
        if 'win' in locals():
            win.close()