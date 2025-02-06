# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event

def draw_fixation_cross():
    """
    Draw a fixation cross in the center of the screen using two lines.
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

        # Create two Line stimuli for the fixation cross
        # Horizontal line
        line_horiz = visual.Line(
            win=win,
            start=(-100, 0),  # (x,y) start point
            end=(100, 0),     # (x,y) end point
            lineWidth=10,
            lineColor=[1, 1, 1],  # White color
            units='pix'
        )

        # Vertical line 
        line_vert = visual.Line(
            win=win,
            start=(0, -100),  # (x,y) start point
            end=(0, 100),     # (x,y) end point
            lineWidth=10,
            lineColor=[1, 1, 1],  # White color
            units='pix'
        )

        # Draw both lines
        line_horiz.draw()
        line_vert.draw()

        # Update the display to show the lines
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
    draw_fixation_cross()