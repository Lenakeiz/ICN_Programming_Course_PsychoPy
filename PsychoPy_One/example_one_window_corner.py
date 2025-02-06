# Import necessary modules from PsychoPy
from psychopy import  visual, core, monitors, logging

# Define a function to open a PsychoPy window
def open_window():
    """
    Function to open a PsychoPy window for a fixed time.
    """
    # Suppress warnings and set the logging level.
    logging.console.setLevel(logging.WARNING)

    try:
        # Define a monitor configuration
        # The monitor's width and resolution should match your physical screen dimensions
        my_monitor = monitors.Monitor("myMonitor")  # Create a named monitor
        my_monitor.setSizePix([1920, 1080])  # Resolution of the monitor

        # Open a PsychoPy window.
        #   - `size` specifies the dimensions of the window (e.g., 900x600 pixels).
        #   - `pos` sets the position of the window on the screen (e.g., top-left corner with (0, 0)).
        #   - `color` defines the background color in RGB values (e.g., black as (0, 0, 0)).
        #   - `units` determines the coordinate system (e.g., "pix" for pixel units).
        win = visual.Window(
            size=(900, 600),  # Size of the window in pixels
            pos=(0, 0),  # Position of the window (top-left corner)
            color=(0, 0, 0),  # Black color in 0-255 scale
            colorSpace='rgb255',  # Specify color space as rgb255 for familiarity
            units="pix",  # Use pixel units
            monitor=my_monitor,  # Apply the monitor configuration
            checkTiming = False,
            screen=0  # Use the primary screen
        )

        # Display the window for a fixed amount of time.
        seconds_to_display = 5
        core.wait(seconds_to_display)

        # After completing the task, close the window safely.
        # This is equivalent to sca in PTB (e.g., Screen('CloseAll')).
        win.close()

    except Exception as e:
        # If an error arises, handle it by closing the window if it's open.
        if 'win' in locals():
            win.close()
        # Rethrow the error to display the details.
        raise e

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    open_window()

    