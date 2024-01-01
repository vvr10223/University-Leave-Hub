from flask import Flask,render_template,request
import json
f=open('db.json','r')
data=json.load(f)
clist=data["colleges"]
app=Flask("authentication")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        college="jntu"
        phone=request.form['phone']
        aadhar=request.form['aadhar']
        email=request.form['email']
        department=request.form['department']
        designation=request.form['designation']
        employment_type=request.form['employment_type']
        employment_status=request.form['employment_status']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        # for index,college in clist:
        #     if college["name"]=="jntu":
        #         if designation=="Principal":
        #             details={}
        #             details["name"]=name
        #             details['phone']=phone
        #             details['aadhar']=aadhar
        #             details['email']=email
        #             details['password']=password

        #             clist[index]["Principal"]=details
    return render_template("register.html")
@app.route('/login')
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
    return render_template("login.html")
app.run(debug=True)