from psychopy import visual, event, core

def demonstrate_clear_events():
    """Demonstrate the effect of clearEvents in waitKeys."""
    try:
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255'
        )
        
        # First demonstration: WITHOUT clearing events
        instruction = visual.TextStim(
            win=win,
            text='Spam some keys NOW...\n(waiting 3 seconds)',
            height=45,
            color=[255, 255, 255],
            colorSpace='rgb255'
        )
        instruction.draw()
        win.flip()
        
        # Give user time to press keys
        core.wait(3)
        
        # Now check with clearEvents=False
        instruction.text = 'Now stopped collecting.\nWatch what happens with clearEvents=False...'
        instruction.draw()
        win.flip()
        core.wait(2)
        
        keys = event.waitKeys(clearEvents=False)
        print("Keys detected (without clearing):", keys)
        
        # Second demonstration: WITH clearing events
        instruction.text = 'Spam some keys NOW...\n(waiting 3 seconds)'
        instruction.draw()
        win.flip()
        
        # Give user time to press keys
        core.wait(3)
        
        # Now check with clearEvents=True (default)
        instruction.text = 'Now stopped collecting.\nWatch what happens with clearEvents=True...'
        instruction.draw()
        win.flip()
        core.wait(2)
        
        keys = event.waitKeys(clearEvents=True)  # This is actually the default
        print("Keys detected (with clearing):", keys)
        
        # Cleanup
        win.close()
        
    except Exception as e:
        if 'win' in locals():
            win.close()
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    demonstrate_clear_events()