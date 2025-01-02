from flask import Flask, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

# Initialize the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://r:itnokitnok083103.@localhost/hasmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'itnokitnok083103.'

# Initialize database
CORS(app)
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    student_number = data['student_number']
    email = data['email']
    password = data['password']

    # Check if user already exists
    if User.query.filter_by(student_number=student_number).first():
        return jsonify({"error": "Student number already exists"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Hash the password and create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(student_number=student_number, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    student_number = data['student_number']
    password = data['password']

    user = User.query.filter_by(student_number=student_number).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user_id'] = user.id
    return jsonify({"message": "Login successful"})

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
