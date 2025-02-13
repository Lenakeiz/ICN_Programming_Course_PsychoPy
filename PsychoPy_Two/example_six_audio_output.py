import sounddevice as sd
import soundfile as sf
import numpy as np
from psychopy import core

def list_audio_devices():
    """Print all available audio devices"""
    print("\nAvailable audio devices:")
    print(sd.query_devices())

def play_tone(frequency=440, duration=0.5, amplitude=0.5, sample_rate=44100):
    """Play a simple sine wave tone
    
    Parameters:
    -----------
    frequency : float
        Frequency in Hz (default: 440Hz, note A4)
    duration : float
        Duration in seconds (default: 0.5s)
    amplitude : float
        Volume between 0 and 1 (default: 0.5)
    sample_rate : int
        Samples per second (default: 44100Hz)
    """
    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Generate sine wave
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    
    print(f"\nPlaying {frequency}Hz tone...")
    sd.play(tone, sample_rate)
    sd.wait()  # Wait until sound has finished
    print("Tone finished!")

def play_wav_file(file_path):
    """Play a WAV file
    
    Parameters:
    -----------
    file_path : str
        Path to the WAV file
    """
    try:
        # Load the WAV file
        data, sample_rate = sf.read(file_path)
        
        print(f"\nPlaying WAV file: {file_path}")
        sd.play(data, sample_rate)
        sd.wait()  # Wait until sound has finished
        print("WAV file finished!")
        
    except Exception as e:
        print(f"Error playing WAV file: {str(e)}")

def test_audio():
    """Test both tone and WAV file playback"""
    try:
        # List available devices
        list_audio_devices()
        
        # Play a test tone
        play_tone(frequency=440, duration=0.5)  # A4 note
        
        # Wait a moment
        core.wait(0.5)
        
        # Try to play a WAV file if it exists
        try:
            play_wav_file('./Assets/pos_feedback.wav')
        except Exception as e:
            print(f"Note: WAV file test skipped - {str(e)}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    test_audio()