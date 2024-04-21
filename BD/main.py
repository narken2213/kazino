from flask import Flask, render_template, redirect
import random
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import webbrowser

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'tasty_and_anus'
levl = 0

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)

@app.route("/")
def index():
    db_sess = db_session.create_session()
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            balance=100000,
            cardnumber=form.cardnumber.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route("/indep")
def indexdep():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user:
        user.balance += 1000000
        db_sess.commit()
    return render_template("index.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/scam')
@login_required
def scam():
    return render_template("scam.html")

@app.route('/deposit')
@login_required
def deposit():
    return render_template("deposit.html")

@app.route('/case')
def case():
    return render_template("case.html")

@app.route('/case1')
@login_required
def opencase1():
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 100:
        user.balance -= 100
        a = random.randint(50, 150)
        user.balance += a
        db_sess.commit()
    else:
        a = 'не хватило средств'

    return render_template("case.html", win=a)

@app.route('/case4')
@login_required
def opencase4():
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 50000:
        user.balance -= 50000
        a = random.randint(100, 100000)
        user.balance += a
        db_sess.commit()
    else:
        a = 'не хватило средств'

    return render_template("case.html", win=a)

@app.route('/case3')
@login_required
def opencase3():
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 10000:
        user.balance -= 10000
        a = random.randint(5000, 15000)
        user.balance += a
        db_sess.commit()
    else:
        a = 'не хватило средств'

    return render_template("case.html", win=a)

@app.route('/case2')
@login_required
def opencase2():
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 1000:
        user.balance -= 1000
        a = random.randint(500, 1500)
        user.balance += a
        db_sess.commit()
    else:
        a = 'не хватило средств'

    return render_template("case.html", win=a)

@app.route('/case5')
@login_required
def opencase5():
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 1000000:
        user.balance -= 1000000
        w = [0,0,0,0,0,0,0,0,0,0,0,0,0,1000000, 100]
        a = random.choice(w)
        user.balance += a
        db_sess.commit()
    else:
        a = 'не хватило средств'

    return render_template("case.html", win=a)


@app.route('/intuichia')
def intu():
    return render_template("intu.html")


@app.route('/intu1')
@login_required
def start1():
    global levl
    levl = 1
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 550:
        user.balance += -550
        a = 'ok'
        db_sess.commit()
    else:
        a = 'не хватило средств'
    return render_template("intu.html", win=a)



@app.route('/intu2')
@login_required
def start2():
    global levl
    levl = 2
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 950:
        user.balance += -950
        a = 'ok'
        db_sess.commit()
    else:
        a = 'не хватило средств'
    return render_template("intu.html", win=a)


@app.route('/intu3')
@login_required
def start3():
    global levl
    levl = 3
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user and user.balance >= 1500:
        user.balance += -1500
        a = 'ok'
        db_sess.commit()
    else:
        a = 'не хватило средств'
    return render_template("intu.html", win=a)


@app.route('/intuv1')
@login_required
def pop():
    global levl
    if levl == 1:
        w = [-550, 1000]
        a = random.choice(w)
    if levl == 2:
        w = [-950, 2000]
        a = random.choice(w)
    if levl == 3:
        w = [-1500, 3000]
        a = random.choice(w)
    db_sess = db_session.create_session()
    print(current_user.id)
    user = db_sess.query(User).filter(User.id == current_user.id).first()

    if user:
        user.balance += a
        db_sess.commit()
    return render_template("intu.html", win=a)


@app.route('/helper')
def help():
    webbrowser.open('https://web.telegram.org/a/#7020446645')

def main():
    db_session.global_init("db/users.db")
    app.run()

if __name__ == '__main__':
    main()
