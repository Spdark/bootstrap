from flask import Flask,request,url_for,render_template
from flask_socketio import SocketIO
import sqlite3

conn = sqlite3.connect('document.db')
c = conn.cursor()

app = Flask(__name__)
app.secret_key = "my secret key"
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/create',methods=['GET','POST'])
def home():
	if request.method == 'POST':
		name = request.form.get('username')
		file = request.files['file']
		c.execute("""INSERT INTO my_table(name,data) VALUES (?,?)""",(name,file.read()))
		msg = "File Uploaded"
		return render_template('upload.html',msg=msg)
	conn.commit()
	c.close()
	conn.close()
if __name__ == '__main__':
    socketio.run(app,debug=True)