from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt, login_manager
from application.models import Posts, Book_Posts, Users
from application.forms import PostForm, Book_PostForm, RegistrationForm, UpdateAccountForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	return render_template('home.html', title='Home', posts=postData)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

#@app.route('/books')
#def books():
#	return render_template('books.html', title='Books')

@app.route('/books', methods=['GET', 'POST'])
def books():
        form = Book_PostForm()
        if form.validate_on_submit():
                postData = Book_Posts(
                book=form.book.data,
                author=form.author.data,
                description=form.description.data,
                rating=form.rating.data
        )

                db.session.add(postData)
                db.session.commit()
                return redirect(url_for('books'))

        else:
                print(form.errors)
        return render_template('books.html', title='Books', form=form)

@app.route('/reviews')
def reviews():
	return render_template('reviews.html', title='Reviews')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
            user=Users.query.filter_by(email=form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                    login_user(user, remember=form.remember.data)
                    next_page = request.args.get('next')

                    if next_page:
                            return redirect(next_page)
                    else:
                            return redirect(url_for('home'))
                    
    return render_template('login.html', title='Login', form=form)

@login_manager.user_loader
def load_user(id):
        return Users.query.get(int(id))

@app.route('/logout')
def logout():
        logout_user()
        return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        
        form = RegistrationForm()
        if form.validate_on_submit():
                hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

                user = Users(
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        email=form.email.data,
                        password=hashed_pw
                )
                
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('books'))
        return render_template('register.html', title='Register', form=form)

@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():

		postData = Posts(
		title=form.title.data,
		content=form.content.data,
                author=current_user
                )

		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('post.html', title='Post', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
        form = UpdateAccountForm()
<<<<<<< HEAD
        if form.validate_on_submit():
                current_user.first_name = form.first_name.data
                current_user.last_name = form.last_name.data
                current_user.email = form.email.data
                db.session.commit()
                return redirect(url_for('account'))
        elif request.method == 'GET'
                form.first_name.data = current_user.first_name
                form.last_name.data = current_user.last_name
                form.email.data = current_user.email                                

dummyData = [
	{
		"name": {"first":"Chester", "last":"Gardner"},
		"title":"First Post",
		"content":"This is some dummy data for Flask lectures"
	},
	{
		"name": {"first":"Chris", "last":"Perrins"},
		"title":"Second Post",
		"content":"This is even more dummy data for Flask lectures"
	}
]
