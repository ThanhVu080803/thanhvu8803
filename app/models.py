from app import db, app
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import  relationship


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100),
                   default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.commit()

        p1 = Product(name='iPhone 13', price=22000000, category_id=1)
        p2 = Product(name='SamSung S1', price=17000000, category_id=2)
        p3 = Product(name='OPPO F1', price=27000000, category_id=2)
        p4 = Product(name='iPhone 14 Pro', price=52000000, category_id=2)
        p5 = Product(name='OPPO F5', price=11000000, category_id=1)
        p6 = Product(name='SamSung galaxy', price=23000000, category_id=1)
        db.session.add_all([p1, p2, p3, p4, p5, p6])
        db.session.commit()