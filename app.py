from flask import Flask, render_template, url_for, session, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

      
app = Flask(__name__)
app.secret_key = "9b90b2d63c112a08bd2ecabff1999b20"

@app.route("/")

def homePortal():
    return render_template ("homePortal.html", title="EduScore University eCampus Portal")



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class Applicant(db.Model):
    __tablename__ =  'applicantDetails'
    id = db.Column(db.Integer, primary_key =True)
    # username = db.Column(db.String(15), nullable= False,)
    firstname = db.Column(db.String(15), nullable= False)
    lastname = db.Column(db.String(15), nullable= False )
    email = db.Column(db.String(30), unique =True, nullable =False )
    password = db.Column(db.String(40),  nullable =False )
    def __repr__(self):
        return f"<Applicant {self.firstname}, {self.lastname}>"
    
class ApplicantSession(db.Model):
    __tablename__ = "applicantSession" 
    id = db.Column(db.Integer, primary_key =True)
    level = db.Column(db.String(40),  nullable =False )
    semester = db.Column(db.String(40),  nullable =False )
    department = db.Column(db.String(40),  nullable =False )
    
     
    def __repr__(self):
        return f"<Applicant {self.firstname}, {self.lastname}>"
    
   
       
class Staff_details(db.Model):
    __tablename__ =  'admin_details'
    id = db.Column(db.Integer, primary_key =True)
    adminusername = db.Column(db.String(40),  nullable =False )
    adminpassword  = db.Column(db.String(40),  nullable =False )
    
    def __repr__(self):
        return f"<Staff {self.firstname}, {self.lastname}>"
    
class Courses(db.Model):
    __tablename__ = "coursesDetails"
    id = db.Column(db.Integer, primary_key =True)  
    code =  db.Column(db.String(100), nullable= False)
    title = db.Column(db.String(100), nullable =False)
    credits_hours = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(20))
    semester = db.Column(db.String(20))
    
    def __repr__(self):
        return f"<Courses {self.firstname}, {self.lastname}>"
    
    
        

@app.route('/applicant/', methods= ["GET","POST"])
def applicant():
    if request.method == "POST":
        firstname = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        level = request.form['level']
        semester = request.form['semester']
        department = request.form['department']
        
        new_applicant = Applicant( firstname=firstname, lastname =lastname, email= email, password= password)
        applicantSession = ApplicantSession(level=level, semester= semester, department= department)
        # Add to database
        try:
            db.session.add(applicantSession)
            db.session.commit()
        except Exception as e :
            return f"ERROR: {e}"  
        try:
            db.session.add(new_applicant)
            db.session.commit()
        except Exception as e :
            return f"ERROR: {e}"    
        
        return render_template('SuccessfulReg.html')
    return render_template("applicant.html")





@app.route('/Login_User/',  methods = ["POST", "GET"])

def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        user = Applicant.query.filter_by(email=email).first()
       
        
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return"Invalid Credentails, please try again"
                
    
    return render_template("Login_User.html")

@app.route("/staff/" , methods= ["POST", "GET"])
def staff():
    if request.method == "POST":
        adminusername = request.form['adminusername']
        adminpassword = request.form['adminpassword']
         
        new_db = Staff_details(adminusername ="Admin1", adminpassword = "admin123")
         
        try:  
            db.session.add(new_db)
            db.session.commit()
        except Exception as e :
           return f"ERROR: {e}"
       
        admin = Staff_details.query.filter_by(adminusername = adminusername).first()
        if admin and admin.adminpassword == adminpassword: 
            return redirect(url_for('admin_dashboard'))
        else:
             return"Invalid Credentails, please try again"
            
    return render_template("staff.html")

@app.route("/admin_dashboard/" ,methods=["POST", "GET"])
def admin_dashboard():
    if request.method == "POST":
        code = request.form["code"]
        credit_hours = request.form['credit_hours']
        title = request.form['title']
        level = request.form['level']
        semester =request.form['semester']
        
        courses_db = Courses(code=code, credits_hours=credit_hours, title=title,level =level, semester = semester)
        try:
            db.session.add(courses_db)
            db.session.commit()
        except Exception as e :
           return f"ERROR: {e}"
        flash("Uploaded Successful", 'success')
        return redirect(url_for('upload_courses'))

        

   
    
    return render_template ("admin_dashboard.html")


@app.route("/upload_courses/")
def upload_courses():
    
    return render_template("upload_courses.html") 


@app.route("/course_list/")
def course_list():
    courses = Courses.query.all()
    
    return render_template("course_list.html", courses=courses)


@app.route("/dashboard/")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    
    student = Applicant.query.get(session['user_id'])
    studentsession = ApplicantSession.query.filter_by(id= student.id).first()
    student_level = studentsession.level
    student_semester = studentsession.semester
    
    courses = Courses.query.filter_by(level=student_level, semester= student_semester).all()
   
    
    return render_template('student_dashboard.html', student=studentsession, studentsession= student, courses=courses)
 
           
    
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True , port= 0000) 
