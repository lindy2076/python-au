import flask
from flask import Flask, request

import vk_proceed

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


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

@app.route('/convert', methods = ['GET', 'POST'])
def convr():
    if request.method == 'GET':
        token_ = request.args.get('token_input')
        '''
        peer_id_ = request.args.get('id_input')
        link_ = request.args.get('png_link')
        randint_ = request.args.get('randint_input')'''
        peer_id_ = None
        link_ = None
        randint_ = 0
    elif request.method == 'POST':
        token_ = request.form.get('token_input')
        peer_id_ = request.form.get('id_input')
        link_ = request.form.get('png_link')
        randint_ = request.form.get('randint_input')

    if token_ is None:
        token_ = ''
    else:
        print(token_)
    if peer_id_ is None:
        peer_id_ = ''
    else:
        print(peer_id_)
    if link_ is None:
        link_ = ''
    if randint_ is None:
        randint_ = 1
    
    response = -1

    if token_ and peer_id_ and link_:
        res = vk_proceed.main(token_, link_, peer_id_, int(randint_))
        response = res


    return flask.render_template(
        'convert.html',
        token=token_,
        peer_id=peer_id_,
        link=link_,
        response=response,
        randint=randint_,
        method=request.method
    )

if __name__ == "__main__":
    app.run(debug=True)
    