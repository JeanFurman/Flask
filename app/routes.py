from flask import Flask, render_template, request, flash

def load(app: Flask) -> Flask:
    @app.route("/testing")
    def testing():
        return render_template('testing.html')
    
    @app.route("/")
    def home():
        name = 'Home Page'
        return render_template('home.html', name=name)
    
    @app.route("/login", methods=['GET', "POST"])
    def login():

        contact = ''

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            contact = f'<Name {name}> {email}'
            flash('Logado com sucesso', 'success')
        return render_template('login.html', contact=contact)

    return app