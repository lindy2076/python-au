#2022 https://github.com/lindy2076/python-au/tree/main/web_dz_vk_fun

import flask
from flask import Flask, jsonify, request, redirect, session, url_for, send_file
from flask_sqlalchemy import SQLAlchemy

import tasks

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")
app.secret_key = "amogus"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imgs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Img(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    hash_owner = db.Column(db.Text)
    doc_id = db.Column(db.Text)
    doc_owner = db.Column(db.Text)

    def __init__(self, hash_owner, doc_id, doc_owner):
        self.hash_owner = hash_owner
        self.doc_id = doc_id
        self.doc_owner = doc_owner


@app.context_processor
def get_vk_pic():
    def get_pic(doc_id, doc_owner):
        if 'token' in session:
            link = tasks.vk_get_doc_link(session['token'], doc_id, doc_owner)
            if link:
                return link
        return url_for('invalid_pic')
    return dict(get_pic=get_pic)


@app.context_processor
def get_last_pic_uploaded():
    def get_uploaded():
        if 'id' in session:
            return url_for('last_pic')
        return url_for('invalid_pic')
    return dict(get_uploaded=get_uploaded)


@app.route('/invalid_pic')
def invalid_pic():
    return flask.send_file('404_.gif')


@app.route('/last_pic')
def last_pic():
    link = 'temp/' + session['id'] + '_temp.png'
    return flask.send_file(link)
    

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/instruction')
def instr():
    return flask.render_template(
        'instruction.html'
    )


@app.route('/auth', methods=['POST', 'GET'])
def auth():
    if request.method == 'GET':
        if 'token' in session:
            return flask.redirect(url_for('root'))
        return flask.render_template(
            'auth.html',
            token_not_ok = 0
        )
    elif request.method == 'POST':
        token = request.form.get('token_confirm')
        if tasks.check_token(token):
            session['token'] = token
            session['id'] = tasks.hash_token(token)
            return flask.redirect(url_for('graffities'))
        else:
            return flask.render_template(
                'auth.html',
                token_not_ok=1
            )

    
@app.route('/my_graffities', methods=['GET', 'POST'])
def graffities():
    if request.method == 'GET': 
        if 'token' in session:          
            print(Img.query.filter_by(hash_owner=session['id'])) 
            return flask.render_template(
                'graffities.html',
                graffities=list(Img.query.filter_by(hash_owner=session['id']))
            ) 
        else:
            return flask.redirect(url_for('auth'))
    elif request.method == 'POST':
        return 'post request'


@app.route('/convert', methods=['POST', 'GET'])
def conv():
    if request.method == 'GET':
        if 'token' in session:
            return flask.render_template(
                'convertation.html',
                photo_uploaded = 0,
                response = 0
            )
        else:
            return flask.redirect(url_for('auth'))
    elif request.method == 'POST':
        pic_link = request.form.get('png_link')
        pic_file = request.files['usr_file']
        if pic_file:
            print(pic_file)

        if not (pic_link or pic_file):
            return flask.render_template(
                'convertation.html',
                photo_uploaded = 0,
                response = 'нет ни ссылки, ни файла'
            )
        else:
            if pic_link:
                res = tasks.request_img(pic_link, session['id'])
            else:
                res = tasks.save_img(pic_file, session['id'])
            return flask.render_template(
                'convertation.html',
                photo_uploaded = res[1],
                response = res[0]
            )


@app.route('/msg', methods=['GET'])
def send_msg():
    peer_id = request.args.get('peer_id')
    doc_id = request.args.get('doc_id') # 632879818  FOR TEST
    doc_owner = request.args.get('doc_owner') # 474500957 
    print(peer_id, doc_id, doc_owner)
    res = tasks.vk_send_message(session['token'], peer_id, doc_id, doc_owner, tasks.random_int())
    res = {
        'response_': str(res)
    }
    return jsonify(res)


@app.route('/upload', methods=['POST'])
def pic_upload():
    if request.method == 'POST':
        try:
            doc_id, doc_owner = tasks.vk_graffiti_upload(session['token'])
            print(doc_id, doc_owner)
            info = Img(session['id'], doc_id, doc_owner)
        except Exception as wtf:
            print('graffiti upload failure ' + str(wtf.__class__))
            res = jsonify({"response_": -1})
        else:
            db.session.add(info)
            db.session.commit()
            res = jsonify({"response_": 1}) 
        return res
    else:
        return flask.redirect(url_for('page_not_found'))


@app.route('/logout')
def logout():
    session.pop('token', None)
    session.pop('id', None)
    return flask.redirect(url_for('auth'))

    
@app.route('/test')
def test():
    # url = 'https://psv4.userapi.com/c537417/u95120065/docs/a758cafe3d54/benedict-cumberbatch-sherlock-john-fan-art.gif?extra=4XEsDe9_IaMEHlQTWWQ2v_mU01ZU8cdxr2TTHP2Ou0p6wqJRArodt4C6k7l3scoLPdJda0Vx-T9QTT59TF5AGNBlSHLFAp8o55_WXWPDc8_2iBCXUfpH4egWup2sXBm7W4f6OHAQHy09yQ6V1wh20yRC'
    #s = tasks.request_img(url, "asdjfdo")
    # res = tasks.vk_get_doc_link(session['token'], "632879818", "474500957")
    # return flask.redirect(res)
    # s = Img("afdsdf", "632879818", "474500957")
    # db.session.add(s)
    # db.session.commit()
    # return 'ok'
    return flask.redirect(url_for('auth'))


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    