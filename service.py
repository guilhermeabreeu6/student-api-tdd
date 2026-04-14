from datetime import datetime
from models import Student, db

CAPITALS = ["Palmas", "São Paulo", "Rio de Janeiro", "Brasília", "Curitiba", "Belo Horizonte"]

def validate_student(data):
    errors = []
    
    # Age check
    birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
    age = (datetime.now() - birth_date).days // 365
    if age < 18:
        errors.append("Student must be of legal age.")
    
    # Hometown check
    if data['hometown'] not in CAPITALS:
        errors.append("Only students from capitals are accepted.")
        
    # National phone check (Simples: starts with 1-9)
    if not str(data['phone']).strip().startswith(('1','2','3','4','5','6','7','8','9')):
        errors.append("Only national phone numbers are accepted.")
        
    return errors

def create_student(data):
    errors = validate_student(data)
    if errors:
        return {"errors": errors}, 400
    
    try:
        new_student = Student(
            name=data['name'],
            birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d'),
            cpf=data['cpf'],
            email=data['email'],
            phone=data['phone'],
            hometown=data['hometown']
        )
        db.session.add(new_student)
        db.session.commit()
        return {"id": new_student.id, "message": "Student created successfully"}, 201
    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 500