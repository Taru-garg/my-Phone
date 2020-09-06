from routes import *

# Run the server
if __name__ == "__main__":
    os.system('termux-wake-lock')
    app.run(host=get_my_ip(), port=12345, debug=True)
