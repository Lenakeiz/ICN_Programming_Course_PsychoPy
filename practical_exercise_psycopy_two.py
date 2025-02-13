from psychopy import visual, event, core, gui
import os
import numpy as np

def get_participant_id():
    """Create a dialog box to get participant ID."""
    # Create the dialog box
    dlg = gui.Dlg(title="Participant Info")
    dlg.addField("Enter participant ID:", "")  # Empty default value
    
    # Show dialog and wait for input
    ok_data = dlg.show()
    
    if dlg.OK:  # If user clicked OK
        return ok_data[0]  # Return the entered ID
    else:  # If user clicked Cancel
        core.quit()  # Exit the experiment

def demonstrate_mario_game():
    """Main function to run the Mario game demonstration."""
    try:
        # Initialize experiment info structure
        exp_info = {}
        
        # Set up experimental parameters
        exp_info['n_images_repeat'] = 2
        exp_info['images_name'] = ['Goomba', 'Lakitu', 'Bill', 'Super Hammer']
        exp_info['images'] = [
            './Assets/Goomba.png', './Assets/Lakitu.png', 
            './Assets/Bill.png', './Assets/SuperHammer.png'
        ]
        exp_info['images_key_presses'] = ['up', 'right', 'down', 'left']
        exp_info['images_scale'] = [0.3, 0.9, 0.2, 0.5]
        exp_info['images_flip'] = [1, 1, 0, 1]
        
        # Color palette (using RGB 0-255 values)
        exp_info['palette_grey'] = [194, 194, 235]
        exp_info['palette_red'] = [255, 68, 59]
        exp_info['palette_dark_grey'] = [109, 93, 95]
        exp_info['palette_black'] = [0, 0, 0]
        exp_info['palette_white'] = [255, 255, 255]
        
        # Add new experimental parameters
        exp_info['trial_duration'] = 2  # seconds
        exp_info['fix_cross_dim_pix'] = 50
        exp_info['fix_line_width_pix'] = 10
        exp_info['fix_cross_duration'] = 1  # seconds
        
        # Get participant ID
        exp_info['pID'] = get_participant_id()
        
        # Create window
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=exp_info['palette_black'],
            colorSpace='rgb255'
        )
        
        # Store window dimensions
        exp_info['screen_x_pixels'], exp_info['screen_y_pixels'] = win.size
        exp_info['x_center'], exp_info['y_center'] = win.size[0]/2, win.size[1]/2
        
        # Create a results folder if it doesn't exist
        if not os.path.exists('./Results'):
            os.makedirs('./Results')
            
        # Run training
        do_training(win, exp_info)
        
        # Run test phase after training
        results = do_test(win, exp_info)
        
        # Cleanup
        win.close()
        
    except Exception as e:
        if 'win' in locals():
            win.close()
        print(f"Error: {str(e)}")
        raise

def do_training(win, exp_info):
    """Handle the training phase of the game."""
    try:
        # Create background
        background = visual.Rect(
            win=win,
            width=exp_info['screen_x_pixels'],
            height=exp_info['screen_y_pixels'],
            fillColor=exp_info['palette_dark_grey'],
            colorSpace='rgb255'
        )
        
        # Create title text
        title = visual.TextStim(
            win=win,
            text="Super Mario PsychoPy",
            pos=(0, exp_info['screen_y_pixels'] * 0.3),
            color=exp_info['palette_red'],
            colorSpace='rgb255',
            wrapWidth=1200,
            height=80,
            bold=True,
            italic=True,
            units='pix'
        )

        # Get the bounding box of the title text
        title_bounds = title.boundingBox  # [width, height]
        padding = 15  # Same padding as MATLAB version
        
        # Create frame around title
        title_frame = visual.Rect(
            win=win,
            width=title_bounds[0] + (padding * 2),
            height=title_bounds[1] + (padding * 2),
            pos=title.pos,  # Center at same position as text
            lineColor=exp_info['palette_red'],
            colorSpace='rgb255',
            lineWidth=4,
            fillColor=None
        )
        
        # Create instruction text
        instructions = visual.TextStim(
            win=win,
            text=("Help Mario to survive against different enemies!\n"
                  "Each enemy can be avoided by using a particular arrow key.\n\n"
                  "In the next part you will learn what arrow key to use for each different enemy."),
            pos=(0, 0),
            color=exp_info['palette_grey'],
            colorSpace='rgb255',
            height=50,
            wrapWidth=1500,
            units='pix'
        )
        
        # Create continue text
        continue_text = visual.TextStim(
            win=win,
            text="Press any key to continue",
            pos=(0, -exp_info['screen_y_pixels'] * 0.3),
            color=exp_info['palette_grey'],
            colorSpace='rgb255',
            units='pix',
            wrapWidth=1500,
            height=50
        )
        
        # Draw welcome screen
        background.draw()
        title_frame.draw()
        title.draw()
        instructions.draw()
        continue_text.draw()
        win.flip()
        
        # Wait for key press
        event.waitKeys()
        
        # Present each enemy and associated key
        for i in range(len(exp_info['images_name'])):
            # Create instruction for this enemy
            enemy_text = visual.TextStim(
                win=win,
                text=f"When {exp_info['images_name'][i]} appears you press {exp_info['images_key_presses'][i]}",
                pos=(0, exp_info['screen_y_pixels'] * 0.3),
                color=exp_info['palette_grey'],
                colorSpace='rgb255',
                height=50
            )
            
            # Load and display enemy image
            enemy_image = visual.ImageStim(
                win=win,
                image=exp_info['images'][i],
                units='pix',
                flipHoriz=bool(exp_info['images_flip'][i])
            )
            
            # Scale the image using the scale factor
            original_size = enemy_image.size
            enemy_image.size = [
                original_size[0] * exp_info['images_scale'][i],
                original_size[1] * exp_info['images_scale'][i]
            ]
            
            # Draw stimuli
            background.draw()
            enemy_text.draw()
            enemy_image.draw()
            win.flip()
            
            # Wait for correct key press
            while True:
                keys = event.waitKeys()
                if exp_info['images_key_presses'][i] in keys:
                    break
        
        # Show completion message
        completion_text = visual.TextStim(
            win=win,
            text=f"Good job! Now you will go through {exp_info['n_images_repeat'] * len(exp_info['images_name'])} trials to help Mario.\n\nGood luck!\n\nPress any key to continue",
            pos=(0, 0),
            color=exp_info['palette_grey'],
            colorSpace='rgb255',
            height=50,
            wrapWidth=800
        )
        
        background.draw()
        completion_text.draw()
        win.flip()
        
        # Wait for final key press
        event.waitKeys()
        
        # Show blank screen briefly
        win.color = exp_info['palette_black']
        win.flip()
        core.wait(0.5)
        
    except Exception as e:
        print(f"Error in training: {str(e)}")
        raise

def do_test(win, exp_info):
    """Handle the testing phase of the game."""
    try:
        # Create trial structure - repeat each image index n times
        trial_structure = np.tile(range(len(exp_info['images_name'])), exp_info['n_images_repeat'])
        
        # Shuffle trial order
        np.random.shuffle(trial_structure)
        
        # Pre-allocate results list
        results = []
        
        # Loop through trials
        for n_trial in range(len(trial_structure)):
            # Store initial trial info
            trial_data = {
                'trial': n_trial + 1,
                'stimulus': exp_info['images_name'][trial_structure[n_trial]],
                'key': exp_info['images_key_presses'][trial_structure[n_trial]],
                'key_press': '',
                'rt': 0,
                'correct': 0
            }
            
            # Load and prepare image
            image = visual.ImageStim(
                win=win,
                image=exp_info['images'][trial_structure[n_trial]],
                units='pix',
                flipHoriz=bool(exp_info['images_flip'][trial_structure[n_trial]])
            )
            
            # Scale image
            original_size = image.size
            image.size = [
                original_size[0] * exp_info['images_scale'][trial_structure[n_trial]],
                original_size[1] * exp_info['images_scale'][trial_structure[n_trial]]
            ]
            
            # Clear any pending key events
            event.clearEvents()
            
            # Show fixation cross
            do_fixation_cross(win, exp_info)
            
            # Present stimulus and collect response
            image.draw()
            start_time = win.flip()
            
            # Initialize response tracking
            response_made = False
            
            # Check for responses while trial is ongoing
            while (core.getTime() - start_time) < exp_info['trial_duration']:
                keys = event.getKeys(timeStamped=True)
                
                if keys and not response_made:
                    key_name = keys[0][0]
                    press_time = keys[0][1]
                    
                    trial_data['key_press'] = key_name
                    trial_data['rt'] = press_time - start_time
                    trial_data['correct'] = int(key_name == trial_data['key'])
                    response_made = True
            
            # Clear screen
            win.color = exp_info['palette_black']
            win.flip()
            
            # Play feedback sound
            sound_file = './Assets/pos_feedback.wav' if trial_data['correct'] else './Assets/neg_feedback.wav'
            play_feedback(sound_file)
            
            # Store trial results
            results.append(trial_data)
            
        # Save results to file
        save_results(results, exp_info['pID'])
        
        return results
        
    except Exception as e:
        print(f"Error in test phase: {str(e)}")
        raise

def do_fixation_cross(win, exp_info):
    """Draw a fixation cross."""
    try:
        # Create horizontal line
        horizontal = visual.Line(
            win=win,
            start=(-exp_info['fix_cross_dim_pix'], 0),
            end=(exp_info['fix_cross_dim_pix'], 0),
            lineWidth=exp_info['fix_line_width_pix'],
            lineColor=exp_info['palette_white'],
            colorSpace='rgb255',
            units='pix'
        )
        
        # Create vertical line
        vertical = visual.Line(
            win=win,
            start=(0, -exp_info['fix_cross_dim_pix']),
            end=(0, exp_info['fix_cross_dim_pix']),
            lineWidth=exp_info['fix_line_width_pix'],
            lineColor=exp_info['palette_white'],
            colorSpace='rgb255',
            units='pix'
        )
        
        # Draw lines
        horizontal.draw()
        vertical.draw()
        win.flip()
        
        # Wait specified duration
        core.wait(exp_info['fix_cross_duration'])
        
    except Exception as e:
        print(f"Error drawing fixation cross: {str(e)}")
        raise

def play_feedback(sound_file):
    """Play audio feedback using sounddevice."""
    try:
        import sounddevice as sd
        import soundfile as sf
        from psychopy import core
        
        # Load the sound file
        data, samplerate = sf.read(sound_file)
        
        # Calculate duration (number of samples / sample rate)
        duration = len(data) / samplerate
        
        # Play the sound
        sd.play(data, samplerate)
        
        # Wait for the duration of the sound file
        core.wait(duration)
        
        # Stop the sound (cleanup)
        sd.stop()
        
    except Exception as e:
        print(f"Error playing feedback: {str(e)}")
        raise

def save_results(results, participant_id):
    """Save results to a file."""
    import pandas as pd
    import os
    
    # Convert results to DataFrame
    df = pd.DataFrame(results)
    
    # Create results directory if it doesn't exist
    if not os.path.exists('./Results'):
        os.makedirs('./Results')
    
    # Save to CSV
    df.to_csv(f'./Results/participant_{participant_id}.csv', index=False)

if __name__ == "__main__":
    demonstrate_mario_game() 