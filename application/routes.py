#Import all the relevant libraries and functions
from flask import abort, render_template, redirect, url_for, request, flash
from application import app, db, bcrypt, login_manager
from application.models import Books, Users, Reviews
from application.forms import Book_PostForm, RegistrationForm, UpdateAccountForm, LoginForm, ReviewForm, UploadForm
from flask_login import login_user, current_user, logout_user, login_required
import boto3

#Render the home page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#Render the about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')

#Renders the books page
@app.route('/books', methods=['GET', 'POST'])
@login_required
def books():
    #List all books
    books = Books.query.all()
    return render_template('books.html', title='Books', books=books)

#Render the books page
@app.route('/books/add', methods=['GET', 'POST'])
@login_required
def add_book():

    #Add a vairable that changes the output of the book page
    #If it is true it is for adding a book
    #If it is false it for editing a book
    add_book = True

    #Add a form
    form = Book_PostForm()
    if form.validate_on_submit():
        book = Books(
        book=form.book.data,
        author=form.author.data,
        description=form.description.data,
        rating=form.rating.data
        )
        #Add the information if it is a new book
        #Returns to the book page if the addition is successful
        try:
            db.session.add(book)
            db.session.commit()
            flash('You have successfully added a new book')
        except:
            flash('Error: The book already exists')
        return redirect(url_for('books'))

    return render_template('book.html', action="Add", title='Add Book', form=form, add_book=add_book)

@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_books(id):

    add_book = False

    book = Books.query.get_or_404(id)
    form = Book_PostForm(obj=book)
    if form.validate_on_submit():
        book.book = form.book.data
        book.author = form.author.data
        book.description = form.description.data
        book.rating = form.rating.data
        db.session.commit()
        flash('You have successfully edited the book')
        #return to books list
        return redirect(url_for('books'))

    form.rating.data = book.rating
    form.description.data = book.description
    form.author.data = book.author
    form.book.data = book.book

    return render_template('book.html', action="Edit", add_book=add_book, book=book, form=form, title="Edit Book")

@app.route('/books/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_books(id):

    reviews = Reviews.query.filter_by(book_id=id)
    for review in reviews:
        db.session.delete(review)

    book = Books.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted a book')

    return redirect(url_for('books'))

    return render_template(title="Delete Book")


@app.route('/reviews')
@login_required
def reviews():

    reviews = Reviews.query.all()

    return render_template('reviews.html', title='Reviews', reviews=reviews)

@app.route('/reviews/add', methods=['GET', 'POST'])
@login_required
def add_review():

    add_review = True

    form = ReviewForm()
    if form.validate_on_submit():
        review = Reviews(
        review_author=form.review_author.data,
        review=form.review.data,
        rating=form.rating.data,
        book_ref=form.book.data
        )
        try:
            db.session.add(review)
            db.session.commit()
            flash('You have successfully added a new Review')
        except:
            flash('Error: The review already exists')
        return redirect(url_for('reviews'))

    return render_template('review.html', action="Add", title='Add Review', form=form, add_review=add_review)

@app.route('/reviews/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_review(id):

    add_review = False

    review = Reviews.query.get_or_404(id)
    form = ReviewForm(obj=review)
    if form.validate_on_submit():
        review.review_author = form.review_author.data
        review.review = form.review.data
        review.rating = form.rating.data
        book_ref = form.book.data
        db.session.commit()
        flash('You have successfully edited the review')
        #return to books list
        return redirect(url_for('reviews'))

    form.book.data = review.book_ref
    form.rating.data = review.rating
    form.review.data = review.review
    form.review_author.data = review.review_author

    return render_template('review.html', action="Edit", add_review=add_review, review=review, form=form, title="Edit Review")

@app.route('/reviews/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_review(id):
    review = Reviews.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    flash('You have successfully edited the review')
    return redirect(url_for('reviews'))

    return render_template(title="Delete Review")


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
                            flash('Invalid email or password')
                            return redirect(url_for('home'))
                    
    return render_template('login.html', title='Login', form=form)

@login_manager.user_loader
def load_user(id):
        return Users.query.get(int(id))

@app.route('/logout')
@login_required
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
                username=form.username.data,
                email=form.email.data,
                password=hashed_pw
        )
        
        db.session.add(user)
        db.session.commit()

        flash('You have successfully registered! You can now login')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    return render_template('upload.html', form=form)


@app.route('/upload_post', methods=['GET', 'POST'])
def upload_post():
    s3 = boto3.resource('s3')
    s3.Bucket('webhosting-1').put_object(Key=request.files["filename"], Body=request.files["image"])

    return 'Filed saved'


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()

	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)


