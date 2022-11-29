import base64
from flask import request, Flask
import numpy as np
import cv2
import io
# import dlib


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

img1 = None


@app.route("/greyscale", methods=["POST"])
def greyscale():
    byte_encode = ""
    if ("photo" in request.files):
        photo = request.files["photo"]
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep="")
        photo = cv2.imdecode(data, cv2.IMREAD_COLOR)
    else:
        return {"status": 400,
                "message": "no image found"}

    gray_image = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    byte_encode = base64.b64encode(
        cv2.imencode(".jpg", gray_image)[1]).decode()

    return {"status": 200,
            "processed_image": byte_encode}


@app.route('/rotate', methods=["POST"])
def rotate():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}
    rotated_image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE
                               if request.form["direction"] == "left"
                               else cv2.ROTATE_90_CLOCKWISE
                               )
    # print(rotated_image.shape)
    byte_encode = base64.b64encode(
        cv2.imencode('.jpg', rotated_image)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/cartoon', methods=["POST"])
def cartoon():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

      # img -> outImg

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Cartoonization
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    byte_encode = base64.b64encode(cv2.imencode('.jpg', cartoon)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/denoise', methods=["POST"])
def denoise():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    dst = cv2.fastNlMeansDenoisingColored(
        img, None, 10, 10, 7, 15)  # type: ignore

    byte_encode = base64.b64encode(cv2.imencode('.jpg', dst)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/edge', methods=["POST"])
def edge():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    edges = cv2.Canny(img, 80, 200)

    byte_encode = base64.b64encode(cv2.imencode('.jpg', edges)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/otsu', methods=["POST"])
def otsu():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(
        img, 120, 180, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    byte_encode = base64.b64encode(cv2.imencode('.jpg', thresh1)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/canny', methods=["POST"])
def canny():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    blur = cv2.GaussianBlur(img, (7, 7), 0)
    cann = cv2.Canny(blur, 10, 20)

    byte_encode = base64.b64encode(cv2.imencode('.jpg', cann)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/blur', methods=["POST"])
def blur():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    blurred = cv2.GaussianBlur(img, (7, 7), 0)
    # cann = cv2.Canny(blur, 10, 20)

    byte_encode = base64.b64encode(cv2.imencode('.jpg', blurred)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/addText', methods=["POST"])
def addText():
    byte_encode = ""
    if 'photo' in request.files:
        photo = request.files['photo']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    # Window name in which image is displayed
    # window_name = 'Image'
    #x,y = photo.shape[0], photo.shape[1]
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (20 * int(request.form["size"]), 50 * int(request.form["size"]))

    # fontScale
    fontScale = int(request.form["size"])

    # print("color", request.form["color"])
    color = tuple(int(request.form["color"].lstrip(
        '#')[i:i+2], 16) for i in (4, 2, 0))
    # color = (150, 150, 250)

    thickness = 3 * int(request.form["size"])

    # Using cv2.putText() method
    imgWithText = cv2.putText(img, request.form["text"], org, font,
                              fontScale, color, thickness, cv2.LINE_AA)

    # print(imgWithText.shape)
    byte_encode = base64.b64encode(
        cv2.imencode('.jpg', imgWithText)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


@app.route('/addSub', methods=["POST"])
def addSub():
    # print("Hello")
    byte_encode = ""
    if 'photo1' in request.files and 'photo2' in request.files:
        photo = request.files['photo1']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img1 = cv2.imdecode(data, color_image_flag)

        photo = request.files['photo2']
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep='')
        color_image_flag = 1
        img2 = cv2.imdecode(data, color_image_flag)
    else:
        return {"status": 400,
                "message": "no image found"}

    if (request.form["action"] == "add"):
        if (img1.shape[0]*img1.shape[1] < img2.shape[0]*img2.shape[0]):
            image = img1
            img1 = img2
            img2 = image

        # print(img1.shape, img2.shape)

        # img = Image.open(filepath2)
        img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        # img = img.resize_contain(img, [img1.shape[1], img1.shape[0]])

        open_cv_image = np.array(img)
        open_cv_image = open_cv_image[:, :, :].copy()

        # print(open_cv_image.shape, img1.shape)
        weightedSum = cv2.addWeighted(img1, 0.5, open_cv_image, 0.4, 0)
        #weightedSum = cv2.subtract(img1, open_cv_image)
        #weightedSum = cv2.subtract(open_cv_image, img1)
        byte_encode = base64.b64encode(
            cv2.imencode('.jpg', weightedSum)[1]).decode()
        return {"status": 200,
                "processed_image": byte_encode
                }
    elif (request.form["action"] == "subtract"):
        if (img1.shape[0]*img1.shape[1] < img2.shape[0]*img2.shape[0]):
            image = img1
            img1 = img2
            img2 = image

        # print(img1.shape, img2.shape)

        # img = Image.open(filepath2)
        img = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
        # img = img.resize_contain(img, [img1.shape[1], img1.shape[0]])

        open_cv_image = np.array(img)
        open_cv_image = open_cv_image[:, :, :].copy()

        # print(open_cv_image.shape, img1.shape)
        # weightedSum = cv2.addWeighted(img1, 0.5, open_cv_image, 0.4, 0)
        weightedSum = cv2.subtract(img1, open_cv_image)
        # weightedSum = cv2.subtract(open_cv_image, img1)

        byte_encode = base64.b64encode(
            cv2.imencode('.jpg', weightedSum)[1]).decode()
        return {"status": 200,
                "processed_image": byte_encode
                }


# dog filter

def put_dog_filter(dog, fc, x, y, w, h):
    face_width = w
    face_height = h

    dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
    for i in range(int(face_height * 1.75)):
        for j in range(int(face_width * 1.5)):
            for k in range(3):
                if dog[i][j][k] < 235:
                    fc[y + i - int(0.375 * h) - 1][x + j -
                                                   int(0.35 * w)][k] = dog[i][j][k]
    return fc


@app.route("/dog", methods=["POST"])
def dog():
    # global dog, face
    byte_encode = ""
    if ("photo" in request.files):
        photo = request.files["photo"]
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep="")
        photo = cv2.imdecode(data, cv2.IMREAD_COLOR)
        print("type:", type(photo))
    else:
        return {"status": 400,
                "message": "no image found"}
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier(
        './filters/haarcascade_frontalface_default.xml')
    fl = face.detectMultiScale(gray, 1.09, 7)
    # gray_image = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    dog = cv2.imread('./filters/images/dog.png')
    for (x, y, w, h) in fl:
        frame = put_dog_filter(dog, photo, x, y, w, h)

    byte_encode = base64.b64encode(
        cv2.imencode(".jpg", frame)[1]).decode()

    return {"status": 200,
            "processed_image": byte_encode}


def put_hat(hat, fc, x, y, w, h):
    face_width = w
    face_height = h
    hat_width = int(face_width * 1.2)
    hat_height = int(0.30 * face_height) + 1
    hat = cv2.resize(hat, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k] < 235:
                    fc[y + i - int(0.40 * face_height)
                       ][x + j][k] = hat[i][j][k]
    return fc


def put_glass(glass, fc, x, y, w, h):
    face_width = w
    face_height = h

    hat_width = face_width + 1
    hat_height = int(0.50 * face_height) + 1

    glass = cv2.resize(glass, (hat_width, hat_height))

    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if glass[i][j][k] < 235:
                    fc[y + i - int(-0.20 * face_height)][x +
                                                         j][k] = glass[i][j][k]
    return fc


@app.route("/hatSpec", methods=["POST"])
def hatSpec():
    # global dog, face
    byte_encode = ""
    if ("photo" in request.files):
        photo = request.files["photo"]
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(),
                             dtype=np.uint8, sep="")
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)
        print("type:", type(photo))
    else:
        return {"status": 400,
                "message": "no image found"}

    face = cv2.CascadeClassifier(
        './filters/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fl = face.detectMultiScale(gray, 1.09, 7)
    ey = face.detectMultiScale(gray, 1.09, 7)
    hat = cv2.imread('./filters/images/hat.png')
    glass = cv2.imread('./filters/images/glasses.png')

    for (x, y, w, h) in fl:
        frame = put_hat(hat, img, x, y, w, h)
    for (x, y, w, h) in ey:
        frame = put_glass(glass, img, x, y, w, h)

    byte_encode = base64.b64encode(
        cv2.imencode(".jpg", frame)[1]).decode()

    return {"status": 200,
            "processed_image": byte_encode}


# Running app
if __name__ == "__main__":
    app.run(debug=True)
