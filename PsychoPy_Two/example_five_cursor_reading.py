from psychopy import visual, core, event
from psychopy.hardware import mouse
import numpy as np

def mouse_query():
    """Example 5: Querying the mouse position and drawing dots"""
    try:
        # Create window
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255',
            screen=1
        )
        
        # Create mouse object
        mouse_obj = mouse.Mouse(visible=False, win=win)
        
        # Create text stimulus for showing coordinates
        coord_text = visual.TextStim(
            win=win,
            text='',
            height=40,
            color=[255, 255, 255],
            colorSpace='rgb255',
            units='pix',
            wrapWidth=800,
            alignText='center'
        )
        
        # Create dot stimulus
        dot = visual.Circle(
            win=win,
            radius=10,
            units='pix',
            fillColor=[1, 1, 1],
            colorSpace='rgb'
        )
        
        # Main loop
        while not mouse_obj.leftButtonPressed:  # Using the leftButtonPressed property
            # Get mouse position
            mouse_pos = mouse_obj.getPos()
            mouse_x, mouse_y = mouse_pos
            
            # Constrain mouse position to window boundaries
            mouse_x = min(max(mouse_x, -win.size[0]/2), win.size[0]/2)
            mouse_y = min(max(mouse_y, -win.size[1]/2), win.size[1]/2)
            
            # Update text
            coord_text.text = f'Mouse X pixel coordinate {round(mouse_x)} and Y pixel coordinate {round(mouse_y)}'
            
            # Update dot position and color
            dot.pos = (mouse_x, mouse_y)
            dot.fillColor = [np.random.random() for _ in range(3)]
            
            # Draw stimuli
            coord_text.draw()
            dot.draw()
            
            # Flip screen
            win.flip()
            
            # Check for escape key
            if event.getKeys(['escape']):
                break

    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        # Ensure cursor is visible and window is closed
        if 'mouse_obj' in locals():
            mouse_obj.setVisible(True)
        if 'win' in locals():
            win.close()

if __name__ == "__main__":
    mouse_query()