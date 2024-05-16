import g4f



_models = {
    '3t': 'gpt-3.5-turbo',
    '3l': 'gpt-3.5-long',
    'r': 'command-r+',
    '100': 'mistral_7b',
    '101': 'mixtral_8x7b',
    '4': 'gpt-4'}

_model = ''
_provider = None
def settings(model, provider=None):
    global _model, _provider
    _model = model if model not in _models else _models[model]
    _provider = provider

def display_settings():
    from g4f_xn.test_providers import (bl, d)
    print(f'{bl}model: {d}{_model}')
    print(f'{bl}provider: {d}{_provider}')

def _chat_completetion(prompt):
    return g4f.ChatCompletion.create(
        model=_model,
        messages=[{"role": "user", "content": prompt}],
        provider=_provider,
        auth=''
    )

def gpt(prompt, chat: None | list[str] = None):

    try:
        if type(chat) is list:
            history = ''.join(chat)
            user_prompt = f'user:\n{prompt}\n'

            response = _chat_completetion(history + user_prompt)
            assistant_prompt = f'assistant:\n\n{response}\n\n'

            chat.append(user_prompt)
            chat.append(assistant_prompt)
        else:
            response = _chat_completetion(prompt)
    except Exception as e:
        return f'[Error: {e}]'

    return response
