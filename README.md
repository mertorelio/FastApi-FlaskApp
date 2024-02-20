# FastApi-FlaskApp
Model deployment with FastApi-Flask-Docker

# Kullanılan teknolojiler
    pydantic 
    requests
    fastapi
    uvicorn
    numpy
    pillow
    tensorflow 
    scikit-learn
    scikit-image
    python-multipart
    


## FastApi Docker
[Docker Hub](https://hub.docker.com/r/mertbozkurt0/fastapi_image)

    docker pull mertbozkurt0/fastapi_image
   
Çalıştırmak için

    docker run -p 8000:8000  mertbozkurt0/fastapi_image

    
## Flask App Docker
[Docker Hub](https://hub.docker.com/r/mertbozkurt0/flask_app)

    docker pull mertbozkurt0/flask_app


Çalıştırmak için

    docker run -d -p 5000:5000 mertbozkurt0/flask_app

  
# Kullanılan model
[Veriseti](https://www.kaggle.com/datasets/mertbozkurt5/image-colorization/data) 

[Notebook](https://www.kaggle.com/code/mertbozkurt5/basic-image-colorization)
