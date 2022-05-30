import webbrowser
import pyperclip    # pip install pyperclip


def clipboard_content():
    return pyperclip.paste()


def fullauto(url,name,region):
    print(f'open url -> {url}')
    assert clipboard_content(), 'Clipboard is empty'
    print(f'have this in your clipboard -> {clipboard_content()}')
    print(f'with selenium, control the initial login to the konnect interface')
    print(f'use {name}.{region}@cloud.rng as the email. It is not required to be validated anyways')
    print(f'log in authentication happens via the token from clipboard')
    webbrowser.open(url)
