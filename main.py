import speech_recognition as sr
import gtts
from playsound import playsound
import openai

r = sr.Recognizer()


def chat_with_gpt(prompt):
    openai.api_key = 'API-KEY'  # Replace with your OpenAI API key

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()


# Open the microphone and start recording
with sr.Microphone() as source:
    print("ask something...")
    audio = r.listen(source)

try:
    # Use the default Google Speech Recognition engine to perform the transcription
    text = r.recognize_google(audio)
    print("You said:", text)
    answer = chat_with_gpt(str(text))
    tts = gtts.gTTS(str(answer))

    print("COde executed after text 2")
    tts.save("hello.mp3")
    playsound("hello.mp3")
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Sorry, an error occurred while processing your request:", str(e))
