import json
import os
import os.path as osp
import shutil


def prepare_galery():
    galery_path = 'static/img/galery'
    galery_imgs = os.listdir(galery_path)
    galery_catalog = []
    for file in galery_imgs:
        galery_catalog.append('img/galery/' + file)
    return galery_catalog


def prepare_query():
    query_path = 'static/img/query'
    query_imgs = os.listdir(query_path)
    query_catalog = []
    for file in query_imgs:
        query_catalog.append('img/query/' + file)
    return query_catalog


with open('camera_data.json', 'r') as f:
    camera_data = json.load(f)


def clean_directory(path):
    if osp.exists(path):
        files = os.listdir(path)
        for file in files:
            os.remove(osp.join(path, file))


def make_camera_img_catalog(cluster, camera_id):
    cluster = str(cluster)
    camera_id = str(camera_id)
    path_to_camera = 'static/img/cameras/cluster_' + cluster + '/camera_' + camera_id
    try:
        os.listdir(path_to_camera)
    except FileNotFoundError:
        os.makedirs(path_to_camera)
    camera_imgs = os.listdir(path_to_camera)
    camera_full_paths = []
    for img in camera_imgs:
        if img != 'detected':
            camera_full_paths.append(osp.join('img/cameras/cluster_' + cluster + '/camera_' + camera_id, img))
    return camera_full_paths


def add_static_to_catalog(camera_paths):
    camera_full_paths = []
    for path in camera_paths:
        camera_full_paths.append(osp.join('static', path))
    return camera_full_paths


def make_camera_detected_img_catalog(cluster, camera_id):
    path_to_bboxes = 'static/img/cameras/cluster_' + str(cluster) + '/camera_' + str(camera_id) + '/detected'
    bboxes = os.listdir(path_to_bboxes)
    full_paths = []
    for bbox in bboxes:
        full_paths.append(
            osp.join('img/cameras/cluster_' + str(cluster) + '/camera_' + str(camera_id) + '/detected', bbox)
        )
    return full_paths


def move_bboxes_to(cluster, camera_id, target):
    path_to_bboxes = 'static/img/cameras/cluster_' + str(cluster) + '/camera_' + str(camera_id) + '/detected'
    bboxes = os.listdir(path_to_bboxes)
    target_path = 'static/img/' + str(target)
    if target == 'query':
        clean_directory(target_path)
    for bbox in bboxes:
        shutil.move(
            osp.join(path_to_bboxes, bbox),
            osp.join(target_path, bbox)
        )
