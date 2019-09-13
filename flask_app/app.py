from flask import Flask, render_template, flash, redirect, url_for, session
from flask_session import Session
from forms import MatchForm, Match2Form, TimeForm
app = Flask(__name__)

SESSION_TYPE = 'redis'
sess = Session()
app.config['SECRET_KEY'] = 'jhbfhjzsbckjdhsddhjbjfhfvhjbspq'
app.secret_key = 'sldknoiwoiojwefwoiefjeo'

names = ['steve', 'carl', 'jenna', 'stutler', 'me', 'myself', 'I'] 

@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html', names=names)


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/match', methods=['GET', 'POST'])
def match():
	form = MatchForm()
	if form.validate_on_submit():
		session['match_number'] = form.match_number.data
		session['name_number'] = form.name_number.data
		session['match_row'] = form.match_row.data
		session['robot_number'] = form.robot_number.data
		return redirect(url_for('match2'))
	return render_template('match.html', form=form, num=0)

@app.route('/match2', methods=['GET', 'POST'])
def match2():
	form = Match2Form()
	if form.validate_on_submit():
		session['name_list'] = form.name_list.data.split(",")
		return redirect(url_for('match3'))
	return render_template('match2.html', form=form)

@app.route('/match3')
def match3():
	return render_template('match3.html', robot=session.get('robot_number', None), names=session.get('name_list', None),
							rows=session.get('match_row', None), ranges=int(session.get('match_number', None)/session.get('match_row', None)),
							name_num=session.get('name_number', None), matches=session.get('match_number', None))

@app.route('/time', methods=['GET', 'POST'])
def time():
	form = TimeForm()
	if form.validate_on_submit():
		session['time_number1'] = form.match_number.data
		session['time_number2'] = form.match_number.data
		session['name_number'] = form.name_number.data
		session['time_row'] = form.match_row.data
		session['robot_number'] = form.robot_number.data
		return redirect(url_for('match2'))
	return render_template('time.html', form=form, num=0)

if __name__ == '__main__':
	app.run(debug=True)
	sess.init_app(app)
