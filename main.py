import os
import openai as ai
import pyaudio
import speech_recognition as sr

# ai.organization = 'org-fiAKNGE2G2ivhR2h2M9tUQMF'
ai.organization = os.environ.get('OPENAI_ORGANIZATION')
# ai.api.key = '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' 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
ai.api_key = os.environ.get('OPENAI_API_KEY')

def query_ai(prompt):
    print('Prompt: ', prompt)
    completions = ai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 10,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    message = completions.choices[0].text
    print('Message: ', message)
    return message


def listen_for_wake_word():
    recog = sr.Recognizer()
    print('Accessing Microphone')
    # 0 = default, vs. Krisp, or other mics or pre-processors/effects
    with sr.Microphone(0) as source:
        print('Listening for wake word')
        audio = recog.listen(source, 10, 4)

        try:
            speech = recog.recognize_google(audio)
            print('What I heard: ', speech)
            if "hey jarvis" in speech.lower():
                print('\033[92mwake word detected\033[0m')
            else:
                print('\033[93mwake word not detected\033[0m')
        except sr.RequestError:
            print('Request Error')
        except sr.UnknownValueError:
            print('Unknown Value Error: Could Not Hear You')
        except sr.WaitTimeoutError:
            print ('Wait Timeout Error: You took too long!')
    return

if __name__ == '__main__':
    # query_ai('When is the next full moon?')
    listen_for_wake_word()
    print('It works!')

