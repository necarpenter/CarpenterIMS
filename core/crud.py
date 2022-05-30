from models.user import User
from models.product import Product, Product_Item
from sqlalchemy.orm import Session


def get_user(db: Session, user_email: str) -> User:
    return db.query(User).filter(User.Email == user_email).first()


def get_products(db: Session) -> list:
    productList: list = []
    for p in db.query(Product).all():
        print(p)
        productList.append(p.__dict__)
    return productList


def get_product(db: Session, productId) -> Product:
    return db.query(Product).filter(Product.Id == productId).first()


def get_productItems(db: Session) -> list:
    productItemList: list = []
    for p in db.query(Product).join(Product_Item, Product.items).all():
        for i in p.items:
            row = {'Name': p.Name, 'Qty': i.Qty}
            print(i)
            productItemList.append(row)
    return productItemList


def get_productItems(db: Session, productId) -> list:
    productItemList: list = []
    for p in db.query(Product).join(Product_Item, Product.items).filter(Product.Id == productId).all():
        for i in p.items:
            row = {'Name': p.Name, 'Qty': i.Qty}
            print(i)
            productItemList.append(row)
    return productItemList


def commitWork(db: Session):
    db.commit()
