import win32com.client
speaker= win32com.client.Dispatch("SAPI.SpVoice")
while True:
    word_to_speak=input("enter your converation(press q to end converation:")
    if word_to_speak.lower()=='q':
        break
    else:
        speaker.Speak(word_to_speak)
