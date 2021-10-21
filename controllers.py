from flask import render_template, request
from app import app
from model import Cards, Feature



@app.route('/footer')
def footer():
    return render_template('footer.html')
@app.route('/bankrekvizitler')
def bankRekvizitler():
    return render_template('bakin_rekvizitleri.html')


@app.route('/hesabatlar')
def hesabatlar():
    return render_template('hesabatlar.html')

@app.route('/rehberlik')
def rehberlik():
    return render_template('rehberlik.html')

@app.route('/umumi_melumat')
def umumi_melumat():
    return render_template('umumi_melumat.html')




@app.route('/kartlar')
def kartlar():
    kart = Cards.query.all()
    feature = Feature.query.all()
    # for i in feature:
        # print(i.cards.id)
        # print(i.card_id)  
    return render_template('cards.html', kart=kart, feature=feature)
    

@app.route('/kartlar/compare')
def compare():
    kart = Cards.query.all()
    return render_template('compare.html', kart=kart)
    
@app.route('/')
def navbar():
    kart = Cards.query.all()
    return render_template('search.html', kart=kart)



@app.route('/search', methods=["GET","POST"])
def search_func():
    if request.method == 'POST':
        keyword = request.form.get('search_name')
        kart = Cards.query.filter((Cards.title.contains(keyword)) | (Cards.description.contains(keyword))).all()

        return render_template('search.html', kart=kart)
    return render_template('search.html')



