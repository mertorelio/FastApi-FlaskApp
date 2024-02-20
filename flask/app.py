import base64
from flask import Flask, render_template, request, redirect, url_for
import requests
from PIL import Image
from io import BytesIO
from database.db import list_users,add_user

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    return render_template('home.html')

#nlp islemi sayfası
@app.route('/nlp')
def about():
    #veri tabanından verileri listeler
    sentences = (list_users())
    #son eklenen en ustte olması icin ters cevırdık 
    sentences_reversed = reversed(sentences)
    
    return render_template('index.html', sentences=sentences_reversed)

#image processing sayfasi
@app.route('/upload')
def upload2():
    return render_template('upload.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Kullanıcı tarafından yüklenen resmi al
    image = request.files['image']

    # FastAPI'ye resmi POST isteği ile gönder
    url = 'https://fastapi-image1-clejzmqjaq-uc.a.run.app/process_image'
    files = {'image': image}
    response = requests.post(url, files=files)
    # FastAPI'den gelen yanıtı al
    result = response.json()
    img = Image.open(image)
    img = img.resize((256, 256))
    
    # İşlenmiş görüntüyü base64 formatında kodlayın
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    # Sonucu kullanıcıya göster
    return render_template('result.html', result=result,res2 = img_str)

# Cümle ekleme
@app.route('/add_sentence', methods=['POST'])
def add_sentence():
    sentence = request.form['sentence']
    data = {"text": sentence} 
    # POST isteği yapma
    url = "https://fastapi-image1-clejzmqjaq-uc.a.run.app/predict_lan"
    response = requests.post(url, json=data)
    
# Yanıtı kontrol etme
    if response.status_code == 200:
        result = response.json()
        print("İşlenmiş cümle:", result)
        add_user(sentence,result["language"])
    
    else:
        print("Hata:", response.text)

    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True,threaded=False)
