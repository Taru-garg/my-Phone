from imports import *
from flask import make_response, jsonify

app = Flask(
    __name__, static_url_path="/storage/emulated/0", static_folder="/storage/emulated/0"
)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home_1.html", title="Home", battery=battery())


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", battery=battery())


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
        battery=battery(),
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
        battery=battery(),
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
        battery=battery(),
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
        battery=battery(),
    )


@app.route("/findPhone", methods=["GET", "POST"])
def findPhone():
    if request.method == "POST":
        passed = request.form["data"]
        if passed == "Play":
            try:
                os.system("termux-media-player play iphone_6-30.ogg")
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


# @app.route("/notification")
# def notif():
#    notifs = subprocess.check_output("termux-notification-list")
#    for notif in notifs:
#        print(json.dumps(json.loads(notif)))
#    return render_template("notif.html", title="Notifications", notifs=notifs)


@app.route("/contact")
def contact():
    contacts = subprocess.check_output("termux-contact-list")
    contact = contacts.decode("utf8").replace("'", '"')
    data = json.loads(contact)
    s = json.dumps(data)
    return render_template(
        "contact.html", title="Contacts", contacts=s, battery=battery()
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
