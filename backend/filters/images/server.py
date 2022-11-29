import base64
from flask import request, Flask
import numpy as np
import cv2
import io


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

img1 = None


""" @app.route("/upload", methods=["POST"])
def upload():
    global img1
    if request.method == "POST" and "photo" in request.files:
        photo = request.files["photo"]
        in_memory_file = io.BytesIO()
        photo.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8, sep="")
        img1 = cv2.imdecode(data, cv2.IMREAD_COLOR)
        print('img uploaded')
    return {"status": 200,
            "message": "Image uploaded"} """


""" @app.route("/fetch", methods=["GET"])
def fetch():
    if (img1 is None):
        return {"status": 400,
                "message": "Image not uploaded"}
    # print(img1)
    # gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    byte_encode = base64.b64encode(
        cv2.imencode(".jpg", img1)[1]).decode()

    return {"status": 200,
            "fetched_image": byte_encode} """


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
    print(rotated_image.shape)
    byte_encode = base64.b64encode(
        cv2.imencode('.jpg', rotated_image)[1]).decode()
    return {"status": 200,
            "processed_image": byte_encode
            }


""" @app.route("/process_image", methods=["POST"])
def process_image():
    byte_encode = ""
    if request.method == "POST":
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

        # buf_decode = base64.b64decode(byte_encode)
        # buf_arr = np.fromstring(buf_decode, dtype=np.uint8, sep="")
        # img1 = cv2.imdecode(buf_arr, cv2.IMREAD_UNCHANGED)

    return {"status": 200,
            "processed_image": byte_encode} """


# Running app
if __name__ == "__main__":
    app.run(debug=True)
