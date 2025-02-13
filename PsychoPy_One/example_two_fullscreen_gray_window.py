# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging
from screeninfo import get_monitors


def open_fullscreen_gray_window():
    """
    Open a full-screen PsychoPy window with a gray background color
    on the highest-numbered screen (external monitor if available).
    """
    # Suppress warnings and set the logging level
    logging.console.setLevel(logging.WARNING)

    try:
        
        # Get system monitors information
        system_monitors = get_monitors()
        print(f"System detected monitors: {system_monitors}")
        
        # Get the external monitor (it may be indexed differently on your system)
        target_monitor = system_monitors[0]
        print(f"Using monitor: {target_monitor}")
        print(f"Resolution: {target_monitor.width}x{target_monitor.height}")

        # Open a full-screen PsychoPy window with a gray background color.
        # The 'visual.Window()' function creates the window. We specify the screen
        # number using the 'screen' parameter and set the background color using 'color'.
        win = visual.Window(
            size=(target_monitor.width, target_monitor.height),
            color=[0, 0, 0],  # Gray color in PsychoPy's normalized RGB scale (-1 to 1)
            colorSpace='rgb',  # Use the normalized RGB color space
            units="pix",  # Use pixel units for any drawing commands
            screen=0,  # Specify the detected screen number
            fullscr=True  # Enable full-screen mode
        )

        # Display the window for a fixed amount of seconds before closing it.
        seconds_to_display = 3  # Time in seconds to display the window
        core.wait(seconds_to_display)  # Pause execution for the specified time

        # Close the PsychoPy window safely.
        win.close()

    except Exception as e:
        # If an error occurs, handle it by closing the window (if open) and raising the exception.
        if 'win' in locals():
            win.close()
        raise e

if __name__ == "__main__":
    open_fullscreen_gray_window()
