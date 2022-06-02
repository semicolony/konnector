import webbrowser
import pyperclip    # pip install pyperclip
import logging
import time


logger = logging.getLogger('fullauto')
logger.setLevel(logging.INFO)

def validate(token):
    if not isinstance(token, str):
        token = b'{token}'
    token = token.strip()
    if len(token) == 32 and token.isalnum():
        pyperclip.copy(token)
        logger.info('token valid')
        return True
    else:
        logger.info('token invalid')
        return False


def fullauto(url,name,region,email,auth_token):
    i = 0
    while not validate(auth_token):
        i += 1
        time.sleep(2)
        print('token valid') if validate(auth_token) else print('token not valid')
        exit(1) if i > 5 else None
    if not email:
        email = f'{name}@{region}.rng'
    print(f'Open url -> {url}')
    assert pyperclip.paste(), 'Clipboard is empty'
    print(f'You have this in your clipboard -> {pyperclip.paste()}')
    print(f'With selenium, control the initial login to the konnect interface')
    print(f'Use {email} as the email. It is not required to be validated anyways')
    print(f'Log in authentication happens via the token from clipboard')
#    webbrowser.open(url)
