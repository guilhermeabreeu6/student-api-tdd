from flask import Flask, request, jsonify
from models import db
import service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    result, status = service.create_student(data)
    return jsonify(result), status

if __name__ == '__main__':
    app.run(debug=True)