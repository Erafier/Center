import torch
import os.path as osp
import os
import cv2
import matplotlib.pyplot as plt
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


class Detector:
    def __init__(
            self,
            config_path: str = 'configs/faster_rcnn_X_101_32x8d_FPN_3x.yaml',
            weight_path: str = 'configs/faster_rcnn_X_101.pkl',
            thresh: float = 0.7
    ):
        torch.cuda.empty_cache()
        self.cfg = get_cfg()
        self.cfg.merge_from_file(config_path)
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = thresh
        self.cfg.MODEL.WEIGHTS = weight_path
        self.predictor = DefaultPredictor(self.cfg)
        print('Сеть успешно загружена')

    def detect_image(self, image_path):
        image = cv2.imread(image_path)
        output = self.predictor(image)
        v = Visualizer(image[:, :, ::-1], MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]), scale=1.2)
        v = v.draw_instance_predictions(output["instances"].to("cpu"))
        plt.imshow(v.get_image()[:, :, ::-1])

    def save_bboxes(self, image_path_catalog, camera_cluster_id):
        frame_id = 0
        image_count = 0
        for image_path in image_path_catalog:
            image_count += 1
            image = cv2.imread(image_path)
            if image is not None:
                output = self.predictor(image)
                bboxes = output['instances'].pred_boxes
                classes = output['instances'].pred_classes
                for i, (cl, coordinates) in enumerate(zip(classes, bboxes)):
                    if cl == 0:
                        coordinates = coordinates.tolist()
                        x1 = int(coordinates[0])
                        y1 = int(coordinates[1])
                        x2 = int(coordinates[2])
                        y2 = int(coordinates[3])
                        cropped = image[y1:y2, x1:x2]
                        if cropped.shape[1] > 35 and (cropped.shape[0] / cropped.shape[1] >= 2.0):
                            # cropped = cv2.resize(cropped, (128, 256))
                            save_path = osp.join(osp.split(image_path)[0], 'detected')
                            if not osp.exists(save_path):
                                os.makedirs(save_path)
                            # save_path = osp.join(osp.split(image_path)[0], 'detected', osp.split(image_path)[1])
                            cv2.imwrite(osp.join(save_path, str(frame_id) + '_c' + str(camera_cluster_id)
                                                 + '_image_' + str(image_count) + '.jpg'), cropped)
                            frame_id += 1


if __name__ == '__main__':
    predictor = Detector()
    predictor.save_bboxes('../static/img/cameras/cluster_5/camera_1/2019-12-11-11:35:50.png')
    path = osp.abspath('')
    print(path)
