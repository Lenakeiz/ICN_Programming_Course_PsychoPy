# Import necessary modules from PsychoPy
from psychopy import visual, event, core

def check_keyboard_input():
    """Demonstrate keyboard input handling.
    
    This example demonstrates:
    1. Waiting for any key press
    2. Getting the key that was pressed
    3. Displaying information about the pressed key on screen
    4. Waiting for a second key press to exit
    """
    try:
        # Create a window to capture keyboard focus
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255'
        )
        
        # Create and draw some instruction text
        instruction = visual.TextStim(
            win=win,
            text='Press any key...',
            height=45,
            color=[255, 255, 255],
            colorSpace='rgb255'
        )
        instruction.draw()
        win.flip()
        
        # Wait for a key press (equivalent to KbWait)
        keys = event.waitKeys()[0]  # Get the first key press
        
        # Create and draw the result text
        result = visual.TextStim(
            win=win,
            height=45,
            text=f'You pressed the key: {keys}\n\nPress any key to exit...',
            color=[255, 255, 255],
            colorSpace='rgb255'
        )
        result.draw()
        win.flip()
        
        # Wait for another key press before closing
        event.waitKeys()
        
        # Close the window
        win.close()
        
        # Also print to console
        print(f'You pressed the key: {keys}')
        
    except Exception as e:
        # If there's an error, make sure to close the window
        if 'win' in locals():
            win.close()
        # Display any error message
        print(f"Error: {str(e)}")

# Add a main entry point so this script can be executed directly
if __name__ == "__main__":
    check_keyboard_input()
