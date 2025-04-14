from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



app =Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    # username = db.Column(db.String(15), nullable= False,)
    firstname = db.Column(db.String(15), nullable= False)
    lastname = db.Column(db.String(15), nullable= False )
    email = db.Column(db.String(30), unique =True, nullable =False )
    password =db.Column(db.String(40),  nullable =False )
    
    def __repr__(self):
        return f"<Applicant {self.firstname}, {self.lastname}>"
    
    

@app.route('/', methods= ["GET","POST"])
def applicant():
    if request.method == "POST":
        firstname = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        
        
        new_applicant = Applicant( firstname=firstname, lastname=lastname, email= email, password= password)
        # Add to database
        try:
            db.session.add(new_applicant)
            db.session.commit()
        except Exception as e :
            return f"ERROR: {e}"    
        
        return render_template('SuccessfulReg.html')
    return render_template("applicant.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True , port= 0000) 