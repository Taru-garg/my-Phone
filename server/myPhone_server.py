from routes import *

# Run the server
if __name__ == "__main__":
    try:
        os.system("termux-wake-lock")
    except:
        os.system("termux-wake-unlock")
        os.system("termux-wake-lock")
    app.run(host=get_my_ip(), port=12345, debug=True)
