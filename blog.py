from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,SelectField
from passlib.hash import sha256_crypt
from functools import wraps
#from werkzeug import secure_filename




#kullanıcı giriş decoreter
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "loggedadmin_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Bu sayfayı görüntülemek için lütfen giriş yapın","danger")
            return redirect(url_for("login"))
    return decorated_function

#Kayıt Formu
class RegisterForm(Form):
    name=StringField("İsim Soyisim",validators=[validators.Length(min=4,max=25)])
    username=StringField("Kullanıcı Adı",validators=[validators.Length(min=5,max=35)])
    email=StringField("Email Adresi",validators=[validators.Email(message="Lütfen geçerli bir email adresi giriniz.")])
    password=PasswordField("Parola:",validators=[
        validators.DataRequired(message="Lürfen bir parola belirleyin"),
        validators.EqualTo(fieldname="confirm",message="Parolanız Uyuşmuyor")
    ])

    confirm=PasswordField("Parola Doğrula")

#Giriş Formu
class LoginForm(Form):
    username=StringField("Kullanıcı Adı")
    password=PasswordField("Parola") 




app=Flask(__name__)
app.secret_key="yektugmat"


app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="yektugmat"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app)


@app.route("/")
def index():
    cursor=mysql.connection.cursor()
    sorgu="Select * From articles"
    result=cursor.execute(sorgu)

    if result>0:
        articles=cursor.fetchall()
        return render_template("index.html",articles=articles)
    else:
        return render_template("index.html")

    #return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dgs")
def dgs():
    cursor=mysql.connection.cursor()
    sorgu="Select *From dersler where bolum_ismi='dgs'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("dgs.html",konuadlari=konuadlari)
    else:
        return render_template("dgs.html")

@app.route("/tyt")
def tyt():
    cursor=mysql.connection.cursor()
    sorgu="Select *From dersler where bolum_ismi='tyt'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("tyt.html",konuadlari=konuadlari)
    else:
        return render_template("tyt.html")

@app.route("/kpss")
def kpss():
    cursor=mysql.connection.cursor()
    sorgu="Select *From dersler where bolum_ismi='kpss'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("kpss.html",konuadlari=konuadlari)
    else:
        return render_template("kpss.html")
@app.route("/ayt")
def ayt():
    cursor=mysql.connection.cursor()
    sorgu="Select *From dersler where bolum_ismi='ayt'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("ayt.html",konuadlari=konuadlari)
    else:
        return render_template("ayt.html")

@app.route("/ales")
def ales():
    cursor=mysql.connection.cursor()
    sorgu="Select *From dersler where bolum_ismi='ales'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("ales.html",konuadlari=konuadlari)
    else:
        return render_template("ales.html")

@app.route("/tytbaski1")
def tytbaski1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='TYT1'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("tytbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("tytbaski1.html")
@app.route("/tytbaski2")
def tytbaski2():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='tytproblem2'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("tytbaski2.html",konuadlari=konuadlari)
    else:
        return render_template("tytbaski2.html")

@app.route("/dgsbaski1")
def dgsbaski1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='DGS1'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("dgsbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("dgsbaski1.html")
@app.route("/dgsbaski2")
def dgsbaski2():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='dgsproblem2'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("dgsbaski2.html",konuadlari=konuadlari)
    else:
        return render_template("dgsbaski2.html")
@app.route("/alesbaski1")
def alesbaski1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='ALES'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("alesbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("alesbaski1.html")
@app.route("/kpssbaski1")
def kpssbaski1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='KPSS'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("kpssbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("kpssbaski1.html")
@app.route("/tytcebir")
def tytcebir():
    cursor=mysql.connection.cursor()
    sorgu="Select *From cebir where bolum_ismi='tyt'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("tytcebir.html",konuadlari=konuadlari)
    else:
        return render_template("tytcebir.html")

@app.route("/alescebir")
def alescebir():
    cursor=mysql.connection.cursor()
    sorgu="Select *From cebir where bolum_ismi='ales'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("alescebir.html",konuadlari=konuadlari)
    else:
        return render_template("alescebir.html")       
@app.route("/kpsscebir")
def kpsscebir():
    cursor=mysql.connection.cursor()
    sorgu="Select *From cebir where bolum_ismi='kpss'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("kpsscebir.html",konuadlari=konuadlari)
    else:
        return render_template("kpsscebir.html") 
@app.route("/ALES")
def ALES():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='ALES'"
    result=cursor.execute(sorgu)
    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("alesbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("alesbaski1.html")
@app.route("/DGS1")
def DGS1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='DGS1'"
    result=cursor.execute(sorgu)
    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("dgsbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("dgsbaski1.html")
@app.route("/KPSS")
def KPSS():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='KPSS'"
    result=cursor.execute(sorgu)
    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("kpssbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("kpssbaski1.html")
@app.route("/TYT1")
def TYT1():
    cursor=mysql.connection.cursor()
    sorgu="Select *From problem where bolum_ismi='TYT1'"
    result=cursor.execute(sorgu)
    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("tytbaski1.html",konuadlari=konuadlari)
    else:
        return render_template("tytbaski1.html")
@app.route("/ders")
def ders():
    cursor=mysql.connection.cursor()
    sorgu='Select *From sinavisimleri_ders'
    result=cursor.execute(sorgu)
    if result>0:
        dersadlari=cursor.fetchall()
        return render_template("ders.html",dersadlari=dersadlari)
    else:
        return render_template("ders.html")



@app.route("/problem")
def problem():
    cursor=mysql.connection.cursor()
    sorgu='Select bolum_ismi From problem GROUP BY bolum_ismi'
    result=cursor.execute(sorgu)
    if result>0:
        problemadlari=cursor.fetchall()
        return render_template('problem.html',problemadlari=problemadlari)
    else:
        return render_template("problem.html")
@app.route("/cebir")
def cebir():
    cursor=mysql.connection.cursor()
    sorgu='Select bolum_ismi From cebir GROUP BY bolum_ismi'
    result=cursor.execute(sorgu)
    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("cebir.html",konuadlari=konuadlari)
    else:
        return render_template("cebir.html")



@app.route("/dgscebir")
def dgscebir():
    cursor=mysql.connection.cursor()
    sorgu="Select *From cebir where bolum_ismi='dgs'"
    result=cursor.execute(sorgu)

    if result>0:
        konuadlari=cursor.fetchall()
        return render_template("dgscebir.html",konuadlari=konuadlari)
    else:
        return render_template("dgscebir.html") 
#Makale SAyfası
@app.route("/articles")
def articles():
    cursor=mysql.connection.cursor()
    sorgu="Select * From articles"
    result=cursor.execute(sorgu)

    if result>0:
        articles=cursor.fetchall()
        return render_template("articles.html",articles=articles)
    else:
        return render_template("articles.html")

@app.route("/addcebir",methods=["GET","POST"])
@login_required
def addcebir():
    form=cebirForm(request.form)
    if request.method=="POST" and form.validate():
        video_title=form.video_title.data
        video_url=form.video_url.data
        referans_kodu=form.referans_kodu.data
        
        cursor=mysql.connection.cursor()
        sorgu="Insert into cebir_videolari(video_title,videoUrl,referans_kodu) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(video_title,video_url,referans_kodu))
        mysql.connection.commit()
        cursor.close()

        flash("Video Başarıyla Eklendi...","success")
        return redirect(url_for("dashboard"))
        
        


    return render_template("addcebir.html",form=form)
    

#addproblem
@app.route("/addproblem",methods=["GET","POST"])
@login_required
def addproblem():
    form=cebirForm(request.form)
    if request.method=="POST" and form.validate():
        video_title=form.video_title.data
        video_url=form.video_url.data
        referans_kodu=form.referans_kodu.data
        
        cursor=mysql.connection.cursor()
        sorgu="Insert into problem_videolari(video_title,video_url,referans_kodu) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(video_title,video_url,referans_kodu))
        mysql.connection.commit()
        cursor.close()

        flash("Video Başarıyla Eklendi...","success")
        return redirect(url_for("dashboard"))
        
        


    return render_template("addproblem.html",form=form)

#addDers
@app.route("/addDers",methods=["GET","POST"])
@login_required
def addDers():
    form=cebirForm(request.form)
    if request.method=="POST" and form.validate():
        video_title=form.video_title.data
        video_url=form.video_url.data
        referans_kodu=form.referans_kodu.data
        
        cursor=mysql.connection.cursor()
        sorgu="Insert into ders_videolari(video_title,videoUrl,referans_kodu) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(video_title,video_url,referans_kodu))
        mysql.connection.commit()
        cursor.close()

        flash("Video Başarıyla Eklendi...","success")
        return redirect(url_for("dashboard"))

    return render_template("addDers.html",form=form)      



@app.route("/dashboard")
@login_required
def dashboard():
    cursor=mysql.connection.cursor()
    sorgu="Select *From articles where author=%s"
    result=cursor.execute(sorgu,(session["username"],))

    if result>0:
        articles=cursor.fetchall()
        return render_template("dashboard.html",articles=articles)
    else:
        return render_template("dashboard.html")

    

    

       
@app.route("/register",methods=["GET","POST"])    
@login_required 
def register():

    form=RegisterForm(request.form)

    if request.method=="POST" and form.validate():
        name=form.name.data
        username=form.username.data
        email=form.email.data
        password=sha256_crypt.encrypt(form.password.data)
        cursor= mysql.connection.cursor()
        sorgu="Insert into admins(name,email,username,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()
        cursor.close()
        flash("Başarıyla Kayıt Oldunuz...","success")
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form=form)

    

#Login islemi

@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm(request.form)
    if request.method=="POST":
        username=form.username.data
        password_entered=form.password.data

        cursor=mysql.connection.cursor()
        
        sorgu="Select *From users where username= %s"
        result=cursor.execute(sorgu,(username,))

        if result>0:
            data=cursor.fetchone()
            real_password=data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla giriş yaptınız...","success")

                session["logged_in"]=True
                session["username"]=username

                return redirect(url_for("index"))
            else:
                flash("Parolanızı yanlış girdiniz...","danger")
                return redirect(url_for("login"))    


        else:
            flash("Böyle bir kullanıcı bulunmuyor...","danger")
            return redirect(url_for("login"))




    return render_template("login.html",form=form)

#adminLogin
@app.route("/adminlogin",methods=["GET","POST"])
def adminlogin():
    form=LoginForm(request.form)
    if request.method=="POST":
        username=form.username.data
        password_entered=form.password.data

        cursor=mysql.connection.cursor()
        
        sorgu="Select *From admins where username= %s"
        result=cursor.execute(sorgu,(username,))

        if result>0:
            data=cursor.fetchone()
            real_password=data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("Başarıyla giriş yaptınız...","success")

                session["loggedadmin_in"]=True
                session["username"]=username

                return redirect(url_for("index"))
            else:
                flash("Parolanızı yanlış girdiniz...","danger")
                return redirect(url_for("adminlogin"))    


        else:
            flash("Böyle bir kullanıcı bulunmuyor...","danger")
            return redirect(url_for("adminlogin"))




    return render_template("adminlogin.html",form=form)
#DETAY Sayfası
@app.route("/article/<string:id>")
def article(id):
    cursor=mysql.connection.cursor()
    sorgu="Select * from articles where id=%s"

    result=cursor.execute(sorgu,(id,))

    if result>0:
        article=cursor.fetchone()
        return render_template("article.html",article=article)
    else:
        return render_template("article.html")

#video işleri

#CEBİR#
@app.route("/cebirVideos/<string:id>")
def cebirVideos(id):
    cursor=mysql.connection.cursor()
    sorgu="Select *from cebir_videolari where referans_kodu=%s"

    result=cursor.execute(sorgu,(id,))
    if result>0:
        videos=cursor.fetchall()
        return render_template("cebirVideos.html",videos=videos)
    else:
        return render_template("cebirVideos.html")
#Problem
@app.route("/problemVideos/<string:id>")
def problemVideos(id):
    cursor=mysql.connection.cursor()
    sorgu="Select *from problem_videolari where referans_kodu=%s"

    result=cursor.execute(sorgu,(id,))
    if result>0:
        videos=cursor.fetchall()
        return render_template("problemVideos.html",videos=videos)
    else:
        return render_template("problemVideos.html")
#Ders
@app.route("/dersVideos/<string:id>")
def dersVideos(id):
    cursor=mysql.connection.cursor()
    sorgu="Select *from ders_videolari where referans_kodu=%s"

    result=cursor.execute(sorgu,(id,))
    if result>0:
        videos=cursor.fetchall()
        return render_template("dersVideos.html",videos=videos)
    else:
        return render_template("dersVideos.html")
#Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


#makale-video ekleme
@app.route("/addarticle",methods=["GET","POST"])
@login_required
def addarticle():
    form=ArticleForm(request.form)
    if request.method=="POST" and form.validate():
        title=form.title.data
        content=form.content.data

        cursor=mysql.connection.cursor()
        sorgu="Insert into articles(title,author,content) VALUES(%s,%s,%s) "
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()

        flash("Video Başarıyla Eklendi...","success")

        return redirect(url_for("dashboard"))
    

    return render_template("addarticle.html",form=form)
#Konu Yükle
@app.route("/addkonu",methods=["GET","POST"])
@login_required
def konuyukle():
    form=konuEklemeForm(request.form)
    if request.method=="POST" and form.validate():
        
        konununAdı=form.konununAdı.data
        alan=form.alan.data
        if alan=="AYT":
            cursor=mysql.connection.cursor()
            sorgu="Insert into ayt_konuları(konu_ismi) VALUES(%s)"
            cursor.execute(sorgu,(konununAdı,))
            mysql.connection.commit()
            cursor.close()

            flash("Video Başarıyla Eklendi...","success")

            return redirect(url_for("dashboard"))

        elif alan=="TYT":
            cursor=mysql.connection.cursor()
            sorgu="Insert into tyt_konuları(konu_ismi) VALUES(%s)"
            cursor.execute(sorgu,(konununAdı,))
            mysql.connection.commit()
            cursor.close()

            flash("Video Başarıyla Eklendi...","success")

            return redirect(url_for("dashboard"))
        elif alan=="KPSS":
            cursor=mysql.connection.cursor()
            sorgu="Insert into kpss_konuları(konu_ismi) VALUES(%s)"
            cursor.execute(sorgu,(konununAdı,))
            mysql.connection.commit()
            cursor.close()

            flash("Video Başarıyla Eklendi...","success")

            return redirect(url_for("dashboard"))
        elif alan=="DGS":
            cursor=mysql.connection.cursor()
            sorgu="Insert into dgs_konuları(konu_ismi) VALUES(%s)"
            cursor.execute(sorgu,(konununAdı,))
            mysql.connection.commit()
            cursor.close()

            flash("Video Başarıyla Eklendi...","success")

            return redirect(url_for("dashboard"))
        elif alan=="ALES":
            cursor=mysql.connection.cursor()
            sorgu="Insert into ales_konuları(konu_ismi) VALUES(%s)"
            cursor.execute(sorgu,(konununAdı,))
            mysql.connection.commit()
            cursor.close()

            flash("Video Başarıyla Eklendi...","success")

            return redirect(url_for("dashboard"))
    return render_template("addkonu.html",form=form)




#Dosya Ekleme

@app.route("/addFile",methods=["GET","POST"])
@login_required
def addFile():
    form=ArticleForm(request.form)
    if request.method=="POST" and form.validate():
        title=form.title.data
        content=form.content.data

        cursor=mysql.connection.cursor()
        sorgu="Insert into articles(title,author,content) VALUES(%s,%s,%s) "
        cursor.execute(sorgu,(title,session["username"],content))
        mysql.connection.commit()
        cursor.close()

        flash("Video Başarıyla Eklendi...","success")

        return redirect(url_for("dashboard"))
    

    return render_template("addFile.html",form=form)
#makale Silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cursor=mysql.connection.cursor()
    sorgu="Select * from articles where author=%s and id= %s"
    result=cursor.execute(sorgu,(session["username"],id))

    if result>0:
        sorgu2="Delete from articles where id= %s"
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()

        return redirect(url_for("dashboard"))

    else:
        flash("Böyle bir makale yok  veya bu işleme yetkiniz yok...","danger")
        return redirect(url_for("index"))


#makale Guncelleme
@app.route("/edit/<string:id>",methods=["GET","POST"])
@login_required
def update(id):

    if request.method=="GET":
        cursor=mysql.connection.cursor()

        sorgu="Select *from articles where id=%s and author=%s"
        result=cursor.execute(sorgu,(id,session["username"]))

        if result==0:
            flash("Böyle bir makale yok veya bu işleme yetkiniz yok...","danger")
            return redirect(url_for("index"))
        else:
            article=cursor.fetchone()
            form=ArticleForm()

            form.title.data=article["title"]
            form.content.data=article["content"]
            return render_template("update.html",form=form)
    else:
        #POST REQUEST
        form=ArticleForm(request.form)

        newTitle=form.title.data
        newContent=form.content.data
        
        sorgu2="Update articles Set title =%s,content=%s where id=%s"
        cursor=mysql.connection.cursor()
        cursor.execute(sorgu2,(newTitle,newContent,id))
        mysql.connection.commit()
        flash("Video Başarıyla Güncellendi...","success")
        return redirect(url_for("dashboard"))

#Arama URL
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method=="GET":
        return redirect(url_for("index"))
    else:
        keyword=(request.form.get("keyword"))
        cursor=mysql.connection.cursor()
        sorgu="Select * from articles where title like '%" + str(keyword) + "%'"
        result=cursor.execute(sorgu)
        if result==0:
            flash("Aranan kelimeye uygun video bulunamadı...","warning")
            return redirect(url_for("articles"))
        else:
            articles=cursor.fetchall()
            return render_template("articles.html",articles=articles)


#makale form
class ArticleForm(Form):
    title=StringField("Video Başlığı",validators=[validators.Length(min=5,max=100)])
    content=TextAreaField("Video Urlsi",validators=[validators.Length(min=10)])
    alan=SelectField("alan",choices=["DGS","KPSS"])


#Konu Form
class konuEklemeForm(Form):
    sınavAdı=StringField("Sınavın İsmi",validators=[validators.Length(min=0,max=100)])
    konununAdı=TextAreaField("Konunun Başlığı",validators=[validators.Length(min=3)])
    alan=SelectField("alan",choices=["DGS","KPSS","ALES","TYT","AYT"])
    

#cebirForm
class cebirForm(Form):
    video_title=StringField("video_title",validators=[validators.Length(min=5,max=100)])
    video_url=TextAreaField("video_url",validators=[validators.Length(min=5,max=100)])
    referans_kodu=StringField("Referans_kodu",validators=[validators.Length(min=1,max=6)])


if __name__=="__main__":
    app.run(host='192.168.1.38',port=int('80'),debug=True)