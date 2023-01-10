import os
import sys
import subprocess
from tempfile import gettempdir
import openai as ai
import pyaudio
import speech_recognition as sr
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from pydub import AudioSegment
from pydub.playback import play

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
                audio_cmd = recog.listen(source, 5, 15)
                cmd = recog.recognize_google(audio_cmd)
                print ('Command: ', cmd)
                response = query_ai(cmd)
                print('Response to command: ', response)
                speak(response)
            else:
                print('\033[93mwake word not detected\033[0m')
        except sr.RequestError:
            print('Request Error')
        except sr.UnknownValueError:
            print('Unknown Value Error: Could not hear you')
        except sr.WaitTimeoutError:
            print ('Wait Timeout Error: You took too long!')
    return

def speak(content):
    session = Session(
        aws_access_key_id='AKIA55PKKMM24MQ6BCZV',
        aws_secret_access_key='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',
        region_name='us-east-2'
    )
    polly = session.client('polly')
    speech = polly.synthesize_speech(
        Text=content,
        OutputFormat='mp3',
        VoiceId='Brian'
    )
    audio = speech['AudioStream'].read()
    print('creating mp3 file')
    filename = 'jarvis.mp3'
    with open(filename, 'wb') as file:
        file.write(audio)
        file.close()
    clip = AudioSegment.from_mp3(filename)
    play(clip)

if __name__ == '__main__':
    # query_ai('When is the next full moon?')

    # while True:
    #     listen_for_wake_word()

    speak(query_ai('When is the next full moon?'))

    print('It works!')

