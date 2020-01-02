from flask import Flask, render_template, redirect, url_for

from detector.detector import Detector
from folders_move import *
from reid import make_reid

app = Flask(__name__)

with open('camera_data.json', 'r') as f:
    camera_data = json.load(f)
    camera_data = [camera for camera in camera_data if camera['cluster_id'] != '0']


@app.route('/')
def index():
    return render_template('map.html', markers=camera_data)


@app.route('/camera/<int:cluster>/<int:id>/')
def camera_detail(cluster, id):
    img_catalog = make_camera_img_catalog(cluster, id)
    address = get_address_from_id(str(cluster) + str(id))
    return render_template('camera_detail.html', cluster=cluster, id=id, address=address, image_catalog=img_catalog)


@app.route('/camera/<int:cluster>/<int:id>/detect')
def detect(cluster, id):
    img_catalog = make_camera_img_catalog(cluster, id)
    predictor = Detector(config_path='detector/configs/faster_rcnn_X_101_32x8d_FPN_3x.yaml',
                         weight_path='detector/configs/faster_rcnn_X_101.pkl')
    img_catalog = add_static_to_catalog(img_catalog)
    bboxes_catalog = 'static/img/cameras/cluster_' + str(cluster) + '/camera_' + str(id) + '/detected'
    clean_directory(bboxes_catalog)
    camera_cluster_id = str(cluster) + str(id)
    predictor.save_bboxes(img_catalog, camera_cluster_id)
    bboxes = make_camera_detected_img_catalog(cluster, id)
    return render_template('detected_images.html', image_catalog=bboxes, cluster=cluster, id=id)


@app.route('/camera/<int:cluster>/<int:id>/detect/toquery')
def detected_to_query(cluster, id):
    move_bboxes_to(cluster, id, 'query')
    return redirect(url_for('query'))


@app.route('/camera/<int:cluster>/<int:id>/detect/togalery')
def detected_to_galery(cluster, id):
    move_bboxes_to(cluster, id, 'galery')
    return redirect(url_for('galery'))


@app.route('/query')
def query():
    query_catalog = prepare_query()
    used_cameras = find_unique_camera_id('static/img/query')
    return render_template('images.html',
                           image_catalog=query_catalog,
                           used_cameras=used_cameras,
                           query=True)


@app.route('/query/clean')
def clean_query():
    clean_directory('static/img/query')
    return redirect(url_for('query'))


@app.route('/galery')
def galery():
    galery_catalog = prepare_galery()
    used_cameras = find_unique_camera_id('static/img/galery')
    return render_template('images.html',
                           image_catalog=galery_catalog,
                           used_cameras=used_cameras,
                           address=get_address_from_id,
                           galery=True)


@app.route('/galery/clean')
def clean_galery():
    clean_directory('static/img/galery')
    return redirect(url_for('galery'))


@app.route('/reid')
def reid():
    result_path = 'static/img/result'
    clean_directory(result_path)
    camera_count = len(find_unique_camera_id('static/img/galery'))
    make_reid(camera_count)
    result_imgs = os.listdir(result_path)
    result_catalog = []
    for img in result_imgs:
        result_catalog.append('img/result/' + img)
    return render_template('result_imgs.html', image_catalog=result_catalog)


if __name__ == '__main__':
    app.run(debug=True)
