import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

music_data = {
    '民谣': [
        {'song': '成都', 'artist': '赵雷', 'url': 'https://music.163.com/song/media/outer/url?id=488191644.mp3'},
        {'song': '南方姑娘', 'artist': '赵雷', 'url': 'https://music.163.com/song/media/outer/url?id=25853881.mp3'},
        {'song': '画', 'artist': '赵雷', 'url': 'https://music.163.com/song/media/outer/url?id=25853882.mp3'},
        {'song': '我记得', 'artist': '赵雷', 'url': 'https://music.163.com/song/media/outer/url?id=1989187119.mp3'},
        {'song': '同桌的你', 'artist': '老狼', 'url': 'https://music.163.com/song/media/outer/url?id=283894.mp3'}
    ],
    '流行': [
        {'song': '七里香', 'artist': '周杰伦', 'url': 'https://music.163.com/song/media/outer/url?id=186161.mp3'},
        {'song': '告白气球', 'artist': '周杰伦', 'url': 'https://music.163.com/song/media/outer/url?id=411214222.mp3'},
        {'song': '后来', 'artist': '刘若英', 'url': 'https://music.163.com/song/media/outer/url?id=364479.mp3'},
        {'song': '小幸运', 'artist': '田馥甄', 'url': 'https://music.163.com/song/media/outer/url?id=368727.mp3'},
        {'song': '演员', 'artist': '薛之谦', 'url': 'https://music.163.com/song/media/outer/url?id=363566.mp3'}
    ],
    '摇滚': [
        {'song': '夜曲', 'artist': '周杰伦', 'url': 'https://music.163.com/song/media/outer/url?id=186163.mp3'},
        {'song': '光辉岁月', 'artist': 'Beyond', 'url': 'https://music.163.com/song/media/outer/url?id=188527.mp3'},
        {'song': '海阔天空', 'artist': 'Beyond', 'url': 'https://music.163.com/song/media/outer/url?id=188526.mp3'},
        {'song': '怒放的生命', 'artist': '汪峰', 'url': 'https://music.163.com/song/media/outer/url?id=4876.mp3'},
        {'song': '蓝莲花', 'artist': '许巍', 'url': 'https://music.163.com/song/media/outer/url?id=167876.mp3'}
    ],
    '古典': [
        {'song': '月光奏鸣曲', 'artist': '贝多芬', 'url': 'https://music.163.com/song/media/outer/url?id=176538.mp3'},
        {'song': '致爱丽丝', 'artist': '贝多芬', 'url': 'https://music.163.com/song/media/outer/url?id=176536.mp3'},
        {'song': '命运交响曲', 'artist': '贝多芬', 'url': 'https://music.163.com/song/media/outer/url?id=176543.mp3'},
        {'song': '梁祝', 'artist': '俞丽拿', 'url': 'https://music.163.com/song/media/outer/url?id=167278.mp3'},
        {'song': '高山流水', 'artist': '中国古典', 'url': 'https://music.163.com/song/media/outer/url?id=167280.mp3'}
    ],
    'R&B': [
        {'song': '爱你', 'artist': '王心凌', 'url': 'https://music.163.com/song/media/outer/url?id=167879.mp3'},
        {'song': '听妈妈的话', 'artist': '周杰伦', 'url': 'https://music.163.com/song/media/outer/url?id=186158.mp3'},
        {'song': '黑色毛衣', 'artist': '周杰伦', 'url': 'https://music.163.com/song/media/outer/url?id=186162.mp3'},
        {'song': '唯一', 'artist': '王力宏', 'url': 'https://music.163.com/song/media/outer/url?id=167903.mp3'},
        {'song': '大城小爱', 'artist': '王力宏', 'url': 'https://music.163.com/song/media/outer/url?id=167907.mp3'}
    ],
    '电子': [
        {'song': 'Faded', 'artist': 'Alan Walker', 'url': 'https://music.163.com/song/media/outer/url?id=374697.mp3'},
        {'song': 'The Spectre', 'artist': 'Alan Walker', 'url': 'https://music.163.com/song/media/outer/url?id=488925632.mp3'},
        {'song': 'Unity', 'artist': 'TheFatRat', 'url': 'https://music.163.com/song/media/outer/url?id=425487864.mp3'},
        {'song': 'Monody', 'artist': 'TheFatRat', 'url': 'https://music.163.com/song/media/outer/url?id=399351667.mp3'},
        {'song': 'Sky', 'artist': 'Steerner/Martell', 'url': 'https://music.163.com/song/media/outer/url?id=33155980.mp3'}
    ]
}

mood_emojis = {
    '民谣': '🎸',
    '流行': '🎤',
    '摇滚': '🤘',
    '古典': '🎻',
    'R&B': '🎷',
    '电子': '🎧'
}

@app.route('/')
def index():
    moods = list(music_data.keys())
    return render_template('index.html', moods=moods, mood_emojis=mood_emojis)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    mood = request.args.get('mood') or request.form.get('mood')
    if mood not in music_data:
        return redirect(url_for('index'))
    
    songs = music_data[mood]
    return render_template('result.html', mood=mood, songs=songs, emoji=mood_emojis.get(mood, ''), moods=list(music_data.keys()))

@app.route('/upload', methods=['POST'])
def upload():
    mood = request.form.get('mood')
    song_name = request.form.get('song_name')
    artist = request.form.get('artist')
    url = request.form.get('url')
    
    if mood and song_name and artist:
        if mood in music_data:
            music_data[mood].append({'song': song_name, 'artist': artist, 'url': url})
    
    return redirect(url_for('recommend', mood=mood))

@app.route('/delete', methods=['POST'])
def delete():
    mood = request.form.get('mood')
    index = request.form.get('index', type=int)
    
    if mood in music_data and index is not None:
        if 0 <= index < len(music_data[mood]):
            del music_data[mood][index]
    
    return redirect(url_for('recommend', mood=mood))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)