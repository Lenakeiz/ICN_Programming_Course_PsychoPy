from psychopy import gui, core

def get_participant_info():
    """Create a dialog box to get participant information."""
    # Create the dialog box
    dlg = gui.Dlg(title="Participant Info")
    dlg.addField("Enter participant ID:", "1")
    dlg.addField("Enter participant name:", "")
    dlg.addField("Enter participant age:", "18")
    
    # Show dialog and wait for input
    ok_data = dlg.show()
    
    if dlg.OK:  # If user clicked OK
        return ok_data
    else:  # If user clicked Cancel
        core.quit()  # Exit the experiment

def main():
    """Main function to run the experiment."""
    try:
        # Get participant information
        participant_info = get_participant_info()
        
        # Extract individual fields
        participant_id = participant_info[0]
        participant_name = participant_info[1]
        participant_age = participant_info[2]
        
        # Print the collected information
        print(f"Participant ID: {participant_id}")
        print(f"Participant Name: {participant_name}")
        print(f"Participant Age: {participant_age}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()