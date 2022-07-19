from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


todos = ['Buy coffe','Send purchase request','Product']

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('user_ip',user_ip)
    return response
    
@app.route('/hello')
def hello():
    user_ip=request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos,}
    #En context ponemos ** porque epandimos el directorio en cambio si 
    # ponemos solo contexts cada vez que ocupemos una variable necesitamos poner context.TUVARIABLE
    return render_template('hello.html',**context) 