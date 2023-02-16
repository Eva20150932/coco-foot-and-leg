# coco-foot-and-leg
a yolo-format dataset for human foot and legs(source:[Human Foot Keypoint Dataset](https://cmu-perceptual-computing-lab.github.io/foot_keypoint_dataset/), its license:[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode))
modification of anno-json: the original json file doesn't match coco format that well. I changed it a little for using the json with pycocotools(exactly：json["catagories"]={catA}→json["catagories"]=[{catA}])
usage of anno-json: I tried to use the keypoints in annotation json to get bbox for foot and legs to generate a dataset with yolo format. Dealing details here :[description in CN and dealing code in python](https://blog.csdn.net/weixin_44338329/article/details/129037393)

