# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event

def draw_overlapping_rectangles():
    """Draw two semi-transparent rectangles that overlap.
    
    This example demonstrates:
    1. Creating a full screen window
    2. Drawing multiple rectangles with transparency
    3. Showing how colors blend in overlapping regions
    4. Waiting for a keypress before closing
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
        
        # Create yellow rectangle (semi-transparent)
        yellow_rect = visual.Rect(
            win=win,
            width=400,    # 400 pixels wide (-300 to +100 in original)
            height=400,   # 400 pixels tall (-300 to +100 in original)
            pos=(-100, -100),  # Shifted left and up from center
            fillColor=[1, 1, 0],  # Yellow color
            opacity=0.5,  # 50% transparent
            lineColor=None,  # No border
            units='pix'
        )

        # Create blue rectangle (semi-transparent)
        blue_rect = visual.Rect(
            win=win,
            width=400,    # 400 pixels wide (-100 to +300 in original)
            height=400,   # 400 pixels tall (-100 to +300 in original)
            pos=(100, 100),  # Shifted right and down from center
            fillColor=[0, 0, 1],  # Blue color
            opacity=0.5,  # 50% transparent
            lineColor=None,  # No border
            units='pix'
        )

        # Draw the rectangles (order matters for transparency)
        yellow_rect.draw()
        blue_rect.draw()

        # Update the display to show both rectangles
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the window (this will also restore the mouse cursor)
        win.close()

    except Exception as e:
        # If there's an error, make sure to close the window
        if 'win' in locals():
            win.close()
        # Re-raise the error
        raise e

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    draw_overlapping_rectangles()
