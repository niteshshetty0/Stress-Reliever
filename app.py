import os

from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__, template_folder='template')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'port': '3306',
    'database': 'stress_reliever'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/memory')
def memory():
    return render_template('memmory.html')


@app.route('/pop')
def pop():
    return render_template('pop.html')


@app.route('/morehelp')
def morehelp():
    return render_template('morehelp.html')


@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')


@app.route('/activies')
def activies():
    return render_template('activies.html')


@app.route('/emoji_page')
def emoji_page():
    return render_template('emoji page.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/admin')
def admin():
    return render_template('login.html')


@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html')


@app.route('/addMusic', methods=['POST', 'GET'])
def add_music():
    music_title = request.form['music-title']
    music_url = request.files['music-url']
    # File upload configuration
    UPLOAD_FOLDER = "C:\\Users\\NITESH SHETTY\\Desktop\\StressReliever\\static\\music"

    # Generate a unique filename for the video
    filename = music_url.filename
    music_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save the video file to the upload folder
    music_url.save(music_path)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_music = "INSERT INTO music(music_title, music_url) VALUES (%s, %s)"
    values = (music_title, filename)

    cursor.execute(insert_music, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Music added successfully!")
    return render_template('adminpage.html')


@app.route('/addVideo', methods=['POST', 'GET'])
def addVideo():
    video_title = request.form['video-title']
    video_url = request.files['video-url']
    # File upload configuration
    UPLOAD_FOLDER = "C:\\Users\\NITESH SHETTY\\Desktop\\StressReliever\\static\\video"

    # Generate a unique filename for the video
    filename = video_url.filename
    video_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save the video file to the upload folder
    video_url.save(video_path)

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_video = "INSERT INTO video (vid_title, vid_url) VALUES (%s, %s)"
    values = (video_title, filename)

    cursor.execute(insert_video, values)
    conn.commit()
    cursor.close()
    conn.close()
    print("Video added successfully!")
    return render_template('adminpage.html')


@app.route('/videos')
def videos():
    query = "SELECT vid_id, vid_title, vid_url FROM video"
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    videos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('video.html', videos=videos)


@app.route('/music')
def music():
    query = "SELECT music_id, music_title, music_url FROM music"
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query)
    musics = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('music.html', musics=musics)


@app.route('/consult', methods=['POST'])
def consult():
    return render_template('consult.html')


@app.route('/client', methods=['POST'])
def client():
    client_name = request.form['client-name']
    client_email = request.form['client-name']
    consulting_time = request.form['consulting-time']
    client_upi = request.form['client-upi']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    sql = "insert into client_data(client_name, client_email, consulting_time, client_upi) values(%s, %s, %s, %s)"
    values = (client_name, client_email, consulting_time, client_upi)

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    print("client added successfully!")
    return render_template('thankyou.html')



@app.route('/thankyou', methods=['POST'])
def thankyou():
    print("Thank you route accessed!")
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
