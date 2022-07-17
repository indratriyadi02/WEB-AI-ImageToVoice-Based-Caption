from flask import Flask, render_template, redirect, request
import cv2
import predict as p

# __name__ == __main__
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def marks():
    if request.method == 'POST':

        f = request.files['userfile']
        path = "./static/{}".format(f.filename)  # ./static/images.jpg
        f.save(path)
        print(f.filename)
        caption = p.caption_this_image(path)

        result_dic = {
            'image': path,
            'caption': caption
        }

    return render_template("index.html", your_result=result_dic)


if __name__ == '__main__':
    app.run(debug=True, threaded=False)
