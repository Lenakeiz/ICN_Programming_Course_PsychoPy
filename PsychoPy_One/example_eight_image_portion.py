# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event

def display_image_portion():
    """Display a portion of an image (the eyes) scaled to a specific size.
    
    This example demonstrates:
    1. Loading an image from the Assets folder
    2. Displaying only a specific portion of that image using an aperture
    3. Scaling that portion to a desired size
    4. Waiting for a keypress before closing
    """
    try:
        # Create a window with a black background
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255',
            allowStencil=True
        )
        
        # Hide the mouse cursor
        win.mouseVisible = False
        
        # Define image properties
        IMAGE_SIZE = [1148, 1525]  # Original image size [width, height]
        
        # Define aperture properties as ratios of image size
        APERTURE_CENTER = [0.15, 0.2]  # Relative position from center [-0.5 to 0.5]
        APERTURE_SIZE = [0.5, 0.25]     # Size as ratio of image size
        
        # Create an ImageStim
        image_stim = visual.ImageStim(
            win=win,
            image='./Assets/Goomba.png',
            units='pix',
            size=IMAGE_SIZE,
            pos=(0, 0)  # Center of screen
        )
        
        # Calculate aperture properties in pixels
        aperture_width = IMAGE_SIZE[0] * APERTURE_SIZE[0]
        aperture_height = IMAGE_SIZE[1] * APERTURE_SIZE[1]
        aperture_x = IMAGE_SIZE[0] * APERTURE_CENTER[0]
        aperture_y = IMAGE_SIZE[1] * APERTURE_CENTER[1]
        
        # Create an aperture
        aperture = visual.Aperture(
            win=win,
            size=(aperture_width, aperture_height),
            pos=(aperture_x, aperture_y),
            units='pix',
            shape='circle'
        )

        # Draw the image
        image_stim.draw()

        # Update the display to show the image
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the aperture before closing the window
        aperture.disable()
        
        # Close the window
        win.close()

    except Exception as e:
        # If there's an error, make sure to close the window
        if 'win' in locals():
            win.close()
        raise e

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    display_image_portion() 