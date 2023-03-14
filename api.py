import os

from flask import Flask, jsonify, request

from generator import generate_password

app = Flask(__name__)
app.debug = bool(os.environ.get('DEBUG'))


@app.route('/api/alpha/generate')
def default():
    pwd = []
    length = request.args.get('length', type=int, default=8)
    count = request.args.get('count', type=int, default=1)
    use_digits = True if request.args.get(
        'use_digits', default='true').lower() == 'true' else False
    use_symbols = True if request.args.get(
        'use_symbols', default='true').lower() == 'true' else False
    use_uppercase = True if request.args.get(
        'use_uppercase', default='true').lower() == 'true' else False
    use_lowercase = True if request.args.get(
        'use_lowercase', default='true').lower() == 'true' else False

    for _ in range(count):
        pwd.append(generate_password(length, use_digits,
                   use_symbols, use_uppercase, use_lowercase))

    return {'success': True, 'content': pwd}
