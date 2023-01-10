import os
import openai as ai

# ai.organization = 'org-fiAKNGE2G2ivhR2h2M9tUQMF'
# ai.api.key = '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'
ai.organization = os.environ.get('OPENAI_ORGANIZATION')
ai.api_key = os.environ.get('OPENAI_API_KEY')

def query_ai(prompt):
    print('Prompt: ', prompt)
    completions = ai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 2,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    message = completions.choices[0].text
    print('Message: ', message)
    return message

if __name__ == '__main__':
    query_ai('hello')
    print('It works!')

