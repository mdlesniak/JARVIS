import os
import openai as ai

# ai.organization = 'org-fiAKNGE2G2ivhR2h2M9tUQMF'
# ai.api.key = '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'
ai.organization = os.environ.get('OPENAI_API_KEY')
ai.api_key = os.environ.get('OPENAI_ORGANIZATION')

if __name__ == '__main__':
    print('It works!')
