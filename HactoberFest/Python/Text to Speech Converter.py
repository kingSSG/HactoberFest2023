# Import the gTTS library
from gtts import gTTS
i = input("1>Direct input \n2>For txt file read\n::")
# Get user input text
if i == '1':
    user_input = input("Enter the text you want to convert to speech: ")
if i == '2':
    file_name = input("Enter the text file name  you want to convert to speech : ")
    try:
        with open(file_name, "r" ,encoding="utf-8") as file:
            user_input = file.read()
            #print(content)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Create a gTTS object with user input text
tts = gTTS(user_input)

# Save the audio to a file (optional)
output_file = "output.mp3"
tts.save(output_file)
print(f"Speech saved to {output_file}")

# Play the audio (requires a media player)
import os

# Adjust the command based on your OS
if os.name == 'posix':  # Linux or macOS
    os.system("mpg321 " + output_file)
elif os.name == 'nt':   # Windows
    os.system("start " + output_file)
else:
    print("Unsupported OS for audio playback.")
