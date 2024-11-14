import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while(True):
        word = input("Enter your command(press q if you wanna exit ): ")
        if word.lower() == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()
                