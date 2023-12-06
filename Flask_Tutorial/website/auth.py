from flask import Blueprint , render_template
import requests
auth = Blueprint('auth',__name__)

@auth.route('/top_10')
def top_10():

    url = "https://imdb188.p.rapidapi.com/api/v1/getWeekTop10"
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    dic = response.json()
    return render_template('top_10.html',vr=dic)

@auth.route('/stream_plato')
def stream():

    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    ln = len(dict['data'])
    dc = {}
    for i in range(ln):
        dc[dict['data'][i]['providerName']] = i
    return render_template('stream_plato.html',component = dict,length = ln)

@auth.route('/netflix',endpoint = 'netflix')
def netflix():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Netflix']]['edges'])
    return render_template('ntf.html',component = dict,ln = lne2,cmp = dc)

@auth.route('/prime_video',endpoint='prime_video')
def prime_video():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Prime Video']]['edges'])
    return render_template('prime_video.html',component = dict,ln = lne2,cmp = dc)

@auth.route('/apple_tv',endpoint='apple_tv')
def apple_tv():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Apple TV+']]['edges'])
    return render_template('apple_tv.html',component = dict,ln = lne2,cmp = dc)

@auth.route('/hulu',endpoint='hulu')
def hulu():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Hulu']]['edges'])
    return render_template('hulu.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/max',endpoint='max')
def max():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Max']]['edges'])
    return render_template('max.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/peacock',endpoint='peacock')
def peacock():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Peacock']]['edges'])
    return render_template('peacock.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/freevee',endpoint='freevee')
def prime_video():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Freevee']]['edges'])
    return render_template('freevee.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/paramount',endpoint='paramount')
def prime_video():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['Paramount+']]['edges'])
    return render_template('paramount.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/amc+',endpoint='amc')
def prime_video():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['AMC+']]['edges'])
    return render_template('amc.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/starz',endpoint='starz')
def starz():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['STARZ']]['edges'])
    return render_template('starz.html',component = dict,ln = lne2, cmp = dc)

@auth.route('/showtime',endpoint='showtime')
def showtime():
    url = "https://imdb188.p.rapidapi.com/api/v1/getWhatsStreaming"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    lne = len(dict['data'])
    dc = {}
    for i in range(lne):
        dc[dict['data'][i]['providerName']] = i
    lne2 = len(dict['data'][dc['SHOWTIME']]['edges'])
    return render_template('showtime.html',component = dict,ln = lne2,cmp = dc)

@auth.route('/fan_fav',endpoint='fan_fav')
def fan_fav():

    url = "https://imdb188.p.rapidapi.com/api/v1/getFanFavorites"
    querystring = {"country":"US"}
    headers = {
        "X-RapidAPI-Key": "7f18323693mshc227f576bb55532p1ee401jsnc72ea41dc09c",
        "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    dict = response.json()
    length = len(dict['data']['list'])
    return render_template('fan_fav.html',component=dict, ln = length)



