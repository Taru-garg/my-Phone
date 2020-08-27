from imports import *

app = Flask(__name__, static_url_path="/home", static_folder="/home")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/photos", methods=["POST", "GET"])
def photos():
    photos = list_files(photos_dir)
    return render_template(
        "photos.html", title="Photos", photos=photos, length=len(photos)
    )


@app.route("/documents")
def documents():
    return render_template(
        "document.html",
        title="Document",
        documents=list_files(document_dir),
        len=len(list_files(document_dir)),
        document_name=list_files_name(document_dir),
    )


@app.route("/music")
def music():
    music = list_files(music_dir)
    ids = []
    for i in range(1, len(music) + 1):
        ids.append(i)
    return render_template(
        "music.html",
        title="Music",
        music=list_files(music_dir),
        len=len(list_files(music_dir)),
        music_name=list_files_name_shortened(music_dir),
        ids=ids,
    )


@app.route("/video")
def video():
    return render_template(
        "video.html",
        title="Video",
        videos=list_files(video_dir),
        len=len(list_files(video_dir)),
        video_names=list_files_name(video_dir),
    )
