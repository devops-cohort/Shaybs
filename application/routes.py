from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts, Book_Posts
from application.forms import PostForm, Book_PostForm

@app.route('/')
@app.route('/home')
def home():
	postData = Posts.query.all()
	postData1 = Book_Posts.query.all()
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

@app.route('/login')
def login():
	return render_template('login.html', title='Login')

@app.route('/register')
def register():
	return render_template('register.html', title='Register')

@app.route('/post', methods=['GET', 'POST'])
def post():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
		first_name=form.first_name.data,
		last_name=form.last_name.data,
		title=form.title.data,
		content=form.content.data
	)

		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('post.html', title='Post', form=form)

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
