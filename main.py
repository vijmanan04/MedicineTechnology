from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import datetime
from database import add, remove, select, extract_time, extract_total_time


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'



@app.route("/")
def layout():
    return render_template('layout.html')
    
    
    



user = ""
@app.route("/register", methods=['GET', 'POST'])
def register():
    global user
    form = RegistrationForm()
    if form.validate_on_submit():
        dt = datetime.datetime.today()
        user = form.id.data
        day = str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year)
        s = (dt.second)
        if s < 10:
            s = "0" + str(s)
        m = dt.minute
        if m < 10:
            m = "0"+ str(m)
        t = dt.hour
        if t < 10:
            t = "0" + str(t)
        entry = str(t) + ":" + str(m) + ":" + str(s)
        exit = "NaN"
        add(user, day, entry, exit, '1', 0)
        flash(f'Sign-in recorded for {form.id.data}!', 'success')
        return redirect(url_for('register'))
    
    print(user)
    return render_template('register.html', title='Sign-in', form=form)
    


@app.route("/leave", methods=['GET', 'POST'])
def leave():
    global user
    form = RegistrationForm()
    if form.validate_on_submit():
        dt = datetime.datetime.today()
        user = form.id.data
        day = str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year)
        s = (dt.second)
        if s < 10:
            s = "0" + str(s)
        m = dt.minute
        if m < 10:
            m = "0"+ str(m)
        t = dt.hour
        if t < 10:
            t = "0" + str(t)
        exit = str(t) + ":" + str(m) + ":" + str(s)
        start = extract_time(user) #FINISH THIS LATER
        FMT = '%H:%M:%S'
        tdelta = datetime.datetime.strptime(exit, FMT) - datetime.datetime.strptime(start, FMT)
        #print((tdelta.seconds))
        tdelta = round((tdelta.seconds) / 60, 2)
        
        
        remove(user, day, exit, '1', str(tdelta))
        flash(f'Sign-out recorded for {form.id.data}!', 'success')
        return redirect(url_for('leave'))
    
    return render_template('leave.html', title='Sign-out', form=form)
    



@app.route("/viewing", methods=['GET', 'POST'])
def view():
    global user
    form = RegistrationForm()
    if form.validate_on_submit():
        id = form.id.data
        data = select(id)
        total = extract_total_time(id)
        #print(total)
        return render_template('viewer.html', title='View Service', data=data, total=total)
    
    return render_template('viewing.html', title='View Service', form=form)


if __name__ == '__main__':
    app.run(debug=True)