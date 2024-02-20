import base64
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
from skimage.color import rgb2lab, lab2rgb
from pydantic import BaseModel
from model import predict_pipeline


app = FastAPI()

#İşlemler için veri modeli
class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

# "/predict_lan" endpoint'i için bir POST yöntemi tanımlıyoruz
@app.post("/predict_lan", response_model=PredictionOut)
def predict(payload: TextIn):
    # Tahminleme işlemini gerçekleştirmek için predict_pipeline fonksiyonunu kullanarak dil tahmini yapıyoruz
    language = predict_pipeline(payload.text)
    
    # Tahmin edilen dili PredictionOut veri modeline uygun bir şekilde döndürüyoruz
    return {"language": language}


@app.get("/")
async def root():
    return {"hello": "world"}

#Modelin yuklenmesi
model = tf.keras.models.load_model("models/image-colorization.h5")

def process_image_1(img):
    img_resized = img.resize((256, 256))
    img_resized_np = np.array(img_resized)

    # RGB görüntüyü Lab renk uzayına dönüştürme
    img_lab = rgb2lab(img_resized_np / 255.0)

    # Sadece L (luminance) kanalını alarak boyutları yeniden düzenleme
    img_lab = img_lab[:, :, 0]

    # Modelin girişi için uygun şekilde boyutları yeniden düzenleme
    img_lab_input = np.expand_dims(img_lab, axis=0)
    img_lab_input = np.expand_dims(img_lab_input, axis=-1)

    # Modeli kullanarak renklendirme yapma
    output = model.predict(img_lab_input)
    output = output * 128

    # Sonuç görüntüsünü oluşturma
    result = np.zeros((256, 256, 3))
    result[:,:,0] = img_lab
    result[:,:,1:] = output[0]
    result_image = lab2rgb(result)

    return Image.fromarray((result_image * 255).astype(np.uint8))

@app.post("/process_image")
async def process_image(image: UploadFile = File(...)):
    # Gelen dosyayı işleyin
    img = Image.open(BytesIO(await image.read()))
    processed_img = process_image_1(img)

    # İşlenmiş görüntüyü base64 formatında kodlayın
    buffered = BytesIO()
    processed_img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # İşlenmiş görüntüyü ve diğer sonuçları döndür
    return {"processed_image": img_str}



 