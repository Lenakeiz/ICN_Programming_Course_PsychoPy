# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event

def display_centered_image():
    """Display an image in the center of the screen.
    
    This example demonstrates:
    1. Loading an image from the Assets folder
    2. Resizing the image
    3. Displaying it centered on screen
    4. Waiting for a keypress before closing
    
    Note: Requires the Assets folder with Goomba.png in the project root
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
        
        # Hide the mouse cursor
        win.mouseVisible = False
        
        # Create an ImageStim - PsychoPy will handle the loading and sizing
        image_stim = visual.ImageStim(
            win=win,
            image='./Assets/Goomba.png',
            units='pix',
            pos=(0, 0),  # Center of screen
            size=None,    # None = original size
        )
        
        # Scale the image to 50% of its original size
        original_size = image_stim.size
        image_stim.size = [s * 0.5 for s in original_size]

        # Draw the image
        image_stim.draw()

        # Update the display to show the image
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the window (this will also restore the mouse cursor)
        win.close()

    except Exception as e:
        # If there's an error, make sure to close the window
        if 'win' in locals():
            win.close()
        # Re-raise the error with additional context about the image path
        raise type(e)(
            f"{str(e)}\nMake sure 'Goomba.png' exists in the './Assets' folder"
        ).with_traceback(e.__traceback__)

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    display_centered_image()