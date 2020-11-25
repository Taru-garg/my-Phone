from imports import *
from flask import make_response, jsonify, flash, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(
    __name__, static_url_path="/storage/emulated/0", static_folder="/storage/emulated/0"
)

UPLOAD_FOLDER = "/storage/emulated/0"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "banana"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
@app.route("/home")
def home():
    return render_template(
        "home_1.html",
        title="Home",
    )


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/photos", methods=["POST", "GET"])
def photos():
    all_files = []
    for photo in photos_dir:
        files_ = list_files(photo)
        for a_file in files_:
            all_files.append(a_file)
    photos = []
    for photo in all_files:
        if photo.rpartition(".")[-1] in photolst:
            photos.append(photo)
    return render_template(
        "photos.html",
        title="Photos",
        photos=photos,
        length=len(photos),
        len_dec=int(len(photos) / 100),
    )


@app.route("/documents")
def documents():
    all_files = []
    all_files_names = []
    for doc in document_dir:
        files_ = list_files(doc)
        files_names = list_files_name(doc)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    documents = []
    documents_names = []
    for i in range(0, len(all_files)):
        if all_files[i].rpartition(".")[2] in doclst:
            documents.append(all_files[i])
            documents_names.append(all_files_names[i])
    return render_template(
        "document.html",
        title="Document",
        documents=documents,
        len=len(documents),
        document_name=documents_names,
    )


@app.route("/music")
def music():
    all_files = []
    all_files_names = []
    for music_ in music_dir:
        files_ = list_files(music_)
        files_names = list_files_name_shortened(music_)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    ids = []
    music = []
    music_names = []
    for i in range(0, len(all_files)):
        if all_files[i].rpartition(".")[2] in musiclst:
            music.append(all_files[i])
            music_names.append(all_files_names[i])
    for i in range(1, len(music) + 1):
        ids.append(i)
    return render_template(
        "music.html",
        title="Music",
        music=music,
        len=len(music),
        music_name=music_names,
        ids=ids,
    )


@app.route("/video")
def video():
    all_files = []
    all_files_names = []
    for video_ in video_dir:
        files_ = list_files(video_)
        files_names = list_files_name(video_)
        for a_file in files_:
            all_files.append(a_file)
        for a_file_name in files_names:
            all_files_names.append(a_file_name)
    videos = []
    video_names = []
    for i in range(0, len(all_files)):
        if all_files[i].rpartition(".")[2] in videolst:
            videos.append(all_files[i])
            video_names.append(all_files_names[i])

    return render_template(
        "video(1).html",
        title="Video",
        videos=videos,
        len=len(videos),
        video_names=video_names,
    )

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route("/findPhone", methods=["GET", "POST"])
def findPhone():
    if request.method == "POST":
        passed = request.form["data"]
        if passed == "Play":
            try:
                os.system("termux-media-player play /storage/emulated/0/SoftwareEngineeringProject/server/iphone_6-30.ogg")
                return {"Message": "Playing"}
            except:
                pass
        else:
            try:
                os.system("termux-media-player stop")
                return {"Message": "Stopped"}
            except:
                pass
    return redirect("/home")


@app.route("/notification",methods=["GET","POST"])
def notif():
    notifs = subprocess.check_output("termux-notification-list")
    notifs = str(notifs.decode("utf8"))
    if request.method == "POST":
    	return notifs
    return render_template("notif.html", title="Notifications", notifs=notifs)


@app.route("/getBattery", methods=["GET", "POST"])
def getBattery():
    if request.method == "POST":
        return jsonify({"Message": battery()})
    return redirect("/home")


@app.route("/contact")
def contact():
    contacts = subprocess.check_output("termux-contact-list")
    contact = str(contacts.decode("utf8"))
    return render_template(
        "contact.html",
        title="Contacts",
        contacts=contact,
    )


@app.route("/call", methods=["POST", "GET"])
def call():
    to_call = request.form["phone"]
    try:
        os.system("termux-telephony-call " + to_call)
    except:
        pass
    return redirect("/home")


@app.route("/clipboard", methods=["GET", "POST"])
def get_clipboard():
    if request.method == "GET":
        return jsonify(
            {
                "Message": str(
                    subprocess.check_output("termux-clipboard-get").decode("utf8")
                )
            }
        )
    return redirect("/home")
    
