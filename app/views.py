from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
#  return "hello simon"
  user={'nickname':'Lkk'} # fake user
  return render_template("index.html",
     title='Hpme',
     user= user)
   
  
