import numpy as np

def create_random_trial_structure():
    # Create experiment info dictionary (similar to MATLAB struct)
    exp_info = {}
    
    # Create a list with paths to image files
    exp_info['images'] = [
        './Assets/Goomba.png',
        './Assets/Lakitu.png',
        './Assets/Bill.png',
        './Assets/SuperHammer.png'
    ]
    
    # Set number of presentations for each image
    exp_info['n_presentations'] = 3
    
    # Create array of indices repeated n_presentations times
    # np.tile is equivalent to MATLAB's repmat
    trial_structure = np.tile(
        np.arange(len(exp_info['images'])),  # equivalent to 1:size(expInfo.images,2)
        exp_info['n_presentations']
    )
    
    # Shuffle the trial structure
    np.random.shuffle(trial_structure)
    
    # Display random presentation order
    for n_trial, trial_idx in enumerate(trial_structure, 1):  # start counting from 1
        print(f"Trial: {n_trial} Showing: {exp_info['images'][trial_idx]}")
        
    return trial_structure, exp_info

if __name__ == "__main__":
    trial_structure, exp_info = create_random_trial_structure()