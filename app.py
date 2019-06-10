import argparse
import logging

from flask import request
from typing import Tuple, List
import json
from flask import Flask
import aspell
import waitress

# Flask app
app = Flask(__name__)
logger = logging.getLogger(__name__)

speller = aspell.Speller('lang', 'en')


def get_corrected_words(string: str) -> List[str]:
    words = string.replace('-', ' ').split()
    corrected_words = []
    for word in words:
        corrected_words.extend(speller.suggest(word)[0].split())

    return corrected_words


@app.route('/spellCheck', methods=['POST'])
def spell_check() -> Tuple:
    logger.info('Process request received')

    # Perform validation on request parameters
    params = json.loads(request.form["json"])
    string = params['string']
    logger.info(string)

    corrected_words = get_corrected_words(string)
    logger.info(corrected_words)

    return json.dumps({
        'corrected_words': corrected_words
    }), 200


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='Port for the service.', required=False, type=int, default=5555)

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # waitress.serve(app, host='localhost', port=args.port)
    app.run('localhost', args.port)


if __name__ == '__main__':
    main()
