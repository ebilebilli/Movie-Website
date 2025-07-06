import openai
from django.conf import settings

openai.api_key = settings.OPENAI_TOKEN


def generate_ai_response_task(question, message):
    prompt = f'Question of user: {question}\nAnswer find in database: {message}\nGive simple and clear answer.'

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'system', 'content': 'You are movie website.'},
                {'role': 'user', 'content': prompt},
            ],
            max_tokens=200,  
            temperature=0.7
        )
        answer = response['choices'][0]['message']['content']
        return {'answer': answer}
    
    except Exception as e:
         return f'AI error: {str(e)}'