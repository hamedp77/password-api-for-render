from flask import Flask, request, redirect
from flask_swagger_ui import get_swaggerui_blueprint

from generator import generate_password

app = Flask(__name__)
app.json.mimetype = 'application/json; charset=UTF-8'

SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
)

app.register_blueprint(swaggerui_blueprint)


@app.route('/')
def index():
    """ This route simply redirects / to SWAGGER_URL"""

    return redirect(SWAGGER_URL)


@app.route('/api/alpha/generate')
def default():
    pw = []
    length = request.args.get('length', type=int, default=8)
    count = request.args.get('count', type=int, default=1)
    use_digits = False if request.args.get(
        'use_digits', default='true').lower() == 'false' else True
    use_symbols = False if request.args.get(
        'use_symbols', default='true').lower() == 'false' else True
    use_uppercase = False if request.args.get(
        'use_uppercase', default='true').lower() == 'false' else True
    use_lowercase = False if request.args.get(
        'use_lowercase', default='true').lower() == 'false' else True

    for _ in range(count):
        pw.append(generate_password(length, use_digits,
                                    use_symbols, use_uppercase,
                                    use_lowercase))

    response = {'pws': pw, 'success': True}

    return response


if __name__ == '__main__':
    app.run()
