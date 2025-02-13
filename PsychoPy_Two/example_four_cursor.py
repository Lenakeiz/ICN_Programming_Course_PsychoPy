from psychopy import visual, core, event, monitors
from psychopy.hardware import mouse

def cursor_control():
    """Example 4: Hiding and Showing mouse cursor"""
    try:
        # Create window
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255'
        )
        
        # Create mouse object
        mouse_obj = mouse.Mouse(visible=True, win=win)
        
        # Create rectangle stimulus
        rect = visual.Rect(
            win=win,
            width=300,  # 150 * 2 as in MATLAB example
            height=300,
            pos=(0, 0),  # Center position
            fillColor=[25, 255, 25],  # Light green
            colorSpace='rgb255'
        )
        
        # Draw green rectangle and flip
        rect.draw()
        win.flip()
        
        # Wait 2 seconds
        core.wait(2.0)
        
        # Hide the cursor
        mouse_obj.setVisible(False)
        
        # Change rectangle color to red and flip
        rect.fillColor = [255, 0, 25]  # Red
        rect.draw()
        win.flip()
        
        # Wait 2 seconds with hidden cursor
        core.wait(2.0)
        
        # Change rectangle color to yellow
        rect.fillColor = [255, 204, 25]  # Yellow
        rect.draw()
        win.flip()
        
        # Set mouse position to bottom-left corner of rectangle
        # Calculate position relative to center
        mouse_x = - 150
        mouse_y = - 150
        mouse_obj.setPos((mouse_x, mouse_y))
        
        # Show cursor
        mouse_obj.setVisible(True)
        
        # Wait final 2 seconds
        core.wait(2.0)

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
    cursor_control()