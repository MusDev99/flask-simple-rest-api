from flask import Flask
from blueprints.items_blueprints import items_bp
from blueprints.category_blueprints import category_bp

app = Flask(__name__)

app.register_blueprint(items_bp, url_prefix='/api')
app.register_blueprint(category_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
