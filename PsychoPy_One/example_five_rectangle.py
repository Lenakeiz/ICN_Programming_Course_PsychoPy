# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event

def draw_green_rectangle():
    """Draw a green rectangle in the upper right part of the screen.
    
    This example demonstrates:
    1. Creating a full screen window
    2. Drawing a colored rectangle in a specific screen location
    3. Waiting for a keypress before closing
    """
    try:
        # Create a window with a black background
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],  # Black background
            colorSpace='rgb255'
        )
        
        # Get the window size to help position the rectangle
        win_size = win.size
        
        # Create a rectangle stimulus
        # Position is relative to center, so we need to adjust coordinates accordingly
        rectangle = visual.Rect(
            win=win,
            width=win_size[0]/2 - 80,    # Width from center to edge minus margin
            height=win_size[1]/2 - 80,    # Height from center to edge minus margin
            pos=(win_size[0]/4, win_size[1]/4),  # Position in upper right quadrant
            fillColor=[0, 1, 0],  # Green color
            lineColor=[1, 0, 0],  # No border
            units='pix'
        )

        # Draw the rectangle
        rectangle.draw()

        # Update the display to show the rectangle
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the window
        win.close()

    except Exception as e:
        # If there's an error, make sure to close the window
        if 'win' in locals():
            win.close()
        # Re-raise the error
        raise e

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    draw_green_rectangle()
