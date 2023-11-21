import requests

response = requests.get('https://api.pawan.krd/v1/chat/completions')

headers = {
    'Authorization': 'Bearer pk-VupZWhrwHDKyODJUwTyuJRInwWCPQvQHQPQdtnjRemlzKEFV' ,
    'Content-Type': 'application/json',
}

json_data = {
    'model': 'pai-001-light-beta',
    'max_tokens': 100,
    'messages': [
        {
            'role': 'system',
            'content': 'You are an helpful assistant.',
        },
        {
            'role': 'user',
            'content': 'Who are you?',
        },
    ],
}

response = requests.post('https://api.pawan.krd/v1/chat/completions', headers=headers, json=json_data)
