from ..import db, photos
from flask import render_template, redirect, url_for, abort
from . import main
from .forms import UpdateProfile, ReviewForm, PitchForm, CategoryForm, CommentForm
from flask_login import login_required, current_user
from ..models import Review, User, Pitch, Category, Comments


@main.route('/')
def index():
    '''
    View function to route to index page
    '''

    #Getting popular movi
    title = 'Home - PRO-PITCH'
    allPitches = Pitch.query.all()
    reviewz = Review.query.all()

    return render_template('index.html', title=title, pitches=allPitches, reviewz=reviewz)


@main.route('/user/<uname>')
def profile(uname):
    '''
    view function of the user profile page
    '''
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user, Pitch=Pitch)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form, user=user)




@main.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
    '''
    Function to route user to the form page to create new pitch
    '''

    form = PitchForm()
    pitch = Pitch()

    if form.validate_on_submit():

        title = form.pitch.data
        id = form.category_id.data
        new_pitch = Pitch(title=title, id=id)

        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('new_pitch.html', PitchForm=form)

@main.route('/user/<uname>/update/pic', methods=['GET', 'POST'])
@login_required
def update_pic(uname):

    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_photo_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/category/<int:id>')
def pitches(category):
    '''
    category route function returns a list of pitches in the category chosen
    '''
    title = Pitch.query.filter_by(
        pitch_id=pitch.id).order_by(Pitch.posted.desc())
    pitches = Pitch.query.filter_by(
        category=category).order_by(Pitch.posted.desc())
    comments = Review.query.filter_by(
        pitch_id=pitch.id).order_by(Review.posted.desc())

    return render_template("pitches.html", pitches=pitches, category=category,comments=comments,title=title)


@main.route('/reviews/<pitch_id>')
@login_required
def reviews(pitch_id):
    pitch = Pitch.query.filter_by(id=pitch_id).first()
    reviews = Review.query.filter_by(
        pitch_id=pitch.id).order_by(Review.posted.desc())

    return render_template('reviews.html', pitch=pitch, reviews=reviews)

@main.route('/add/category', methods=['GET', 'POST'])
@login_required
def new_category():
    '''
    View new group route function that returns a page with a form to create a category
    '''
    form = CategoryForm()
    pitch = Pitch.query.all()

    if form.validate_on_submit():
        name = form.pitch.data
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('main.index'))

    title = 'New category'
    return render_template('new_category.html', category_form=form, title=title, pitches=pitch)

@main.route('/pitch/review/new/<pitch_id>', methods=['GET', 'POST'])
@login_required
def new_review(pitch_id):
    form = ReviewForm()
    pitch = Pitch.query.filter_by(id=pitch_id).first()
    review = Review()

    if form.validate_on_submit():
        review.pitch_review_title = form.title.data
        review.pitch_review = form.review.data
        review.pitch_id = pitch_id
        review.user_id = current_user.id

        db.session.add(review)
        db.session.commit()

        return redirect(url_for('main.reviews', pitch_id=pitch.id))

    return render_template('new_review.html', review_form=form)


@main.route('/write_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def post_comment(id):
    ''' function to post comments '''
    form = CommentForm()
    title = 'post comment'
    pitches = Pitch.query.filter_by(id=id).first()
    comments = Comments.query.filter_by().all()

    if pitches is None:
         abort(404)

    if form.validate_on_submit():
        feedback = form.feedback.data
        new_comment = Comments(
            feedback=feedback, user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        
        return redirect(url_for('main.index', id=pitches.id))

    return render_template('post_comment.html', comment_form=form, title=title,comments=comments)


