from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_review = request.form['title_give']
    author_review = request.form['author_give']
    review_review = request.form['review_give']

    doc = {
        'title':title_review,
        'author':author_review,
        'review':review_review
    }
    db.bookreview.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookreview.find({},{'_id':False}))
    return jsonify({'result': 'success', 'reviews': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
