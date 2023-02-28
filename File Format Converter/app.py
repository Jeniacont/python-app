import io
from PIL import Image
from flask import Flask, request, Response, make_response, send_file
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/jpgtopng")
def jpg_to_png():
    return render_template("jpgtopng.html")


@app.route("/pngtojpg")
def png_to_jpg():
    return render_template("pngtojpg.html")


@app.route("/webptopng")
def webp_to_png():
    return render_template("webptopng.html")


@app.route("/bmptopng")
def bmp_to_png():
    return render_template("bmptopng.html")


@app.route("/pngtopdf")
def png_to_pdf():
    return render_template("pngtopdf.html")


@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png_api():
    # check if image is uploaded or not
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # get the image from request
    image = request.files['image']

    # check if image is in JPG format
    if not image.filename.lower().endswith('.jpg') and not image.filename.lower().endswith('.jpeg'):
        return 'Image is not in JPG format', 400

    # check if image size is less than 5 MB
    if len(image.read()) > 5 * 1024 * 1024:
        return 'Image size is greater than 5 MB', 400

    # reset the file pointer to the start of the file
    image.seek(0)

    # open image using PIL and convert to PNG
    img = Image.open(io.BytesIO(image.read()))
    png_image = io.BytesIO()
    img.save(png_image, format='PNG')
    png_image.seek(0)

    # create response object with PNG image as attachment and return it
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition',
                         'attachment', filename='image.png')
    return response


@app.route('/api/pngtojpg', methods=['POST'], endpoint='png_to_jpg_api')
def png_to_jpg_api():
    # check if image is uploaded or not
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # get the image from request
    image = request.files['image']

    # check if image is in PNG format
    if not image.filename.lower().endswith('.png'):
        return 'Image is not in PNG format', 400

    # check if image size is less than 5 MB
    if len(image.read()) > 5 * 1024 * 1024:
        return 'Image size is greater than 5 MB', 400

    # reset the file pointer to the start of the file
    image.seek(0)

    # open image using PIL and convert to JPG
    img = Image.open(io.BytesIO(image.read()))
    jpg_image = io.BytesIO()
    img.convert('RGB').save(jpg_image, format='JPEG')
    jpg_image.seek(0)

    # create response object with JPG image as attachment and return it
    response = make_response(jpg_image.getvalue())
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set('Content-Disposition',
                         'attachment', filename='image.jpg')
    return response


@app.route('/api/webptopng', methods=['POST'], endpoint='webp_to_png_api')
def webp_to_png_api():
    # check if image is uploaded or not
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # get the image from request
    image = request.files['image']

    # check if image is in PNG format
    if not image.filename.lower().endswith('.webp'):
        return 'Image is not in webp format', 400

    # check if image size is less than 5 MB
    if len(image.read()) > 5 * 1024 * 1024:
        return 'Image size is greater than 5 MB', 400

    # reset the file pointer to the start of the file
    image.seek(0)

    # open image using PIL and convert to PNG
    img = Image.open(io.BytesIO(image.read()))
    png_image = io.BytesIO()
    img.convert('RGB').save(png_image, format='PNG')
    png_image.seek(0)

    # create response object with PNG image as attachment and return it
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition',
                         'attachment', filename='image.png')
    return response


@app.route('/api/bmptopng', methods=['POST'], endpoint='bmp_to_png_api')
def bmp_to_png_api():
    # check if image is uploaded or not
    if 'image' not in request.files:
        return 'No image uploaded', 400

    # get the image from request
    image = request.files['image']

    # check if image is in BMP format
    if not image.filename.lower().endswith('.bmp'):
        return 'Image is not in bmp format', 400

    # check if image size is less than 5 MB
    if len(image.read()) > 5 * 1024 * 1024:
        return 'Image size is greater than 5 MB', 400

    # reset the file pointer to the start of the file
    image.seek(0)

    # open image using PIL and convert to BMP
    img = Image.open(io.BytesIO(image.read()))
    png_image = io.BytesIO()
    img.convert('RGB').save(png_image, format='PNG')
    png_image.seek(0)

    # create response object with PNG image as attachment and return it
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition',
                         'attachment', filename='image.png')
    return response


@app.route('/api/pngtopdf', methods=['POST'])
def png_to_pdf_api():
    # Check if request contains a file
    if 'image' not in request.files:
        return 'No file uploaded', 400

    image = request.files['image']

    # Check if file is a PNG image
    if not image.filename.endswith('.png'):
        return 'File is not a PNG image', 400

    # Check if file size is less than 5 MB
    if len(image.read()) > 5 * 1024 * 1024:
        return 'File size is too large (greater than 5 MB)', 400
    image.seek(0)

    # Convert PNG image to PDF
    with io.BytesIO() as output:
        with Image.open(image) as img:
            img.save(output, 'PDF', resolution=100.0)
        output.seek(0)

        response = make_response(output.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response


if __name__ == "__main__":
    app.run(debug=True)
