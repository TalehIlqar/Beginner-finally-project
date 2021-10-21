from extensions import db
from app import app

class Visamaster(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    visamaster = db.relationship('Cards', backref='visamaster', lazy=True)

    def __repr__(self):
        return f'{self.title}'
        

    def __init__(self, title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()




class Category(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    category = db.relationship('Cards', backref='category', lazy=True)

    def __repr__(self):
        return f'{self.title}'
        

    def __init__(self, title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

class Cardtype(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    cardtype = db.relationship('Cards', backref='cardtype', lazy=True)

    def __repr__(self):
        return f'{self.title}'
        

    def __init__(self, title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()

# class Valuta(db.Model):
#     id = db.Column(db.Integer(), primary_key = True)
#     title = db.Column(db.String(255), nullable=False)
#     # cards_id = db.Column(db.Integer(), db.ForeignKey('cards.id'), nullable = False)
#     valuta = db.relationship('Cards', backref='valuta', lazy=True)

#     def __repr__(self):
#         return f'{self.title}'
        

#     def __init__(self, title):
#         self.title = title

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


class Valuta(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    valuta_id = db.Column(db.Integer(), db.ForeignKey('cards.id'), nullable = True)
    

    def __repr__(self):
        return f'{self.title}'
        
    def __init__(self, title):
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()


class Feature(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    feature = db.Column(db.String(255), nullable=True)
    card_id = db.Column(db.Integer(), db.ForeignKey('cards.id'), nullable = True)

    

    def __repr__(self):
        return f'{self.title}, {self.feature}'
        
    def __init__(self, title, feature):
        self.title = title
        self.feature = feature

    def save(self):
        db.session.add(self)
        db.session.commit()




    


class Cards(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable = False)
    image = db.Column(db.String(255), nullable = False)
    is_button1 = db.Column(db.Boolean())
    is_button2 = db.Column(db.Boolean())
    visamaster_id = db.Column(db.Integer(), db.ForeignKey('visamaster.id'), nullable = True)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable = True)
    card_type = db.Column(db.Integer(), db.ForeignKey('cardtype.id'), nullable = True)
    # valuta_id = db.Column(db.Integer(), db.ForeignKey('valuta.id'), nullable = True)
    valuta_id = db.relationship('Valuta', backref='cards', lazy=True)
    feature_id = db.relationship('Feature', backref='cards', lazy=True)



    

    def __repr__(self):
        return f'{self.id},{self.title}, {self.description}, {self.image}, {self.is_button1}, {self.is_button2}, {self.visamaster_id}, {self.category_id}, {self.card_type}, {self.valuta_id}, {self.feature_id}'
    


    def __init__(self, title, description,image,is_button, visamaster_id,category_id, card_type, valuta_id, feature_id):
        self.title = title
        self.description = description
        self.image = image
        self.is_button = is_button
        self.visamaster_id = visamaster_id
        self.category_id = category_id 
        self.card_type = card_type 
        self.valuta_id = valuta_id
        self.feature_id = feature_id

        

    def save(self):
        db.session.add(self)
        db.session.commit()



