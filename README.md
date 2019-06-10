# Spell Check
A simple spell checking flask service based on the open-source aspell
library.

## Installing
This runs on a Linux environment.

1. Install `python >= 3.6`
2. Install the [Aspell library](http://aspell.net/)
3. Install the python requirements: `pip install -r requirements.txt`

## Usage
1. Start the flask service:
    ```bash
    python app.py --port 5555
    ```
2. Issue POST commands:
    ```bash
    curl -H "Content-Type: application/json" -X POST http://localhost:5555/spellCheck -d '{"string": "helloworld"}'
    ```
