# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event
from screeninfo import get_monitors


def draw_diagonal_line():
    """
    Open a PsychoPy window and draw a pink diagonal line across it.
    The line extends from the top-left to bottom-right corner.
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

        # Select the second screen if available
        screen_to_use = len(system_monitors)

        # Create a full-screen window with black background
        win = visual.Window(
            size=(target_monitor.width, target_monitor.height),
            color=[0, 0, 0],  # Black background
            colorSpace='rgb255',  # Use RGB color space
            units="pix",  # Use pixel units
            screen=screen_to_use
        )

        # Get the actual window dimensions
        window_width, window_height = win.size
        
        # Calculate line coordinates based on window size
        start_x = -window_width/2 + window_width*0.1  # Left edge + 10% width
        start_y = window_height/2 - window_height*0.1  # Top edge - 10% height
        end_x = window_width/2 - window_width*0.1     # Right edge - 10% width
        end_y = -window_height/2 + window_height*0.1  # Bottom edge + 10% height

        diagonal_line = visual.Line(
            win=win,
            start=(start_x, start_y),
            end=(end_x, end_y),
            lineWidth=30,  # Line thickness
            lineColor=[1, 0, 1],  # Pink color in RGB
            colorSpace='rgb',
            units='pix'
        )

        # Draw the line to the window
        diagonal_line.draw()
        
        # Update the display to show the line
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the window
        win.close()

    except Exception as e:
        # If an error occurs, handle it by closing the window (if open) and raising the exception
        if 'win' in locals():
            win.close()
        raise e

if __name__ == "__main__":
    draw_diagonal_line()
