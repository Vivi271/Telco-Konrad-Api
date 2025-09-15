from sqlalchemy import Column, Integer, String, Date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(Date)

    def __repr__(self):
        return f'<User {self.username}>'

class Document(db.Model):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    document_type = Column(String(50), nullable=False)
    created_at = Column(Date)

    def __repr__(self):
        return f'<Document {self.document_type} for User {self.user_id}>'

class Contract(db.Model):
    __tablename__ = 'contracts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    contract_details = Column(String(255), nullable=False)
    created_at = Column(Date)

    def __repr__(self):
        return f'<Contract for User {self.user_id}>'