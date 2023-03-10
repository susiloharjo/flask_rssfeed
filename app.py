from flask import Flask, jsonify, render_template
import feedparser

app = Flask(__name__)

# RSS feed URL untuk Wired.com
rss_url = "https://www.wired.com/feed/rss"

@app.route('/')
def get_wired_rss():
    # parsing RSS feed dengan feedparser
    feed = feedparser.parse(rss_url)

    # inisialisasi list untuk menyimpan data yang akan diambil dari feed
    data_list = []

    # loop melalui setiap artikel di feed dan mengambil data yang dibutuhkan
    for entry in feed.entries:
        # mengambil data yang dibutuhkan dari artikel
        title = entry.title
        published_date = entry.published
        link = entry.link
        description = entry.description
        categories = entry.category
        keywords = entry.media_keywords
        thumbnail = entry.media_thumbnail[0]['url']

        # menyimpan data dalam dictionary
        data = {
            "title": title,
            "published_date": published_date,
            "link": link,
            "description": description,
            "categories": categories,
            "keywords": keywords,
            "thumbnail": thumbnail
        }

        # menambahkan dictionary ke list data_list
        data_list.append(data)

    # merender file HTML dengan menggunakan data_list
    return render_template('index.html', data=data_list)

if __name__ == '__main__':
    app.run(debug=True)
