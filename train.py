# 训练脚本：把 data/ 下的数据集喂给 YOLO，训出我们自己的安全帽检测模型
from ultralytics import YOLO

# 数据集的配置文件（里面有类别名和三个文件夹的路径）
DATA_YAML = "data/safety-helmet/data.yaml"

def main():
    # yolov8n 是最小的模型，训练最快，先用它跑通全流程
    # 跑通之后想提精度，可以换成 yolov8s 或 yolov8m 再训一轮做对比
    model = YOLO("yolov8n.pt")

    model.train(
        data=DATA_YAML,
        epochs=50,        # 训练多少轮：50 轮对这个小数据集够用了
        imgsz=640,        # 图片统一缩到 640
        batch=16,         # 一批喂 16 张图（显存不够就改成 8）
        name="helmet-v1", # 这次实验的名字，结果会存到 runs/detect/helmet-v1
    )

if __name__ == "__main__":
    main()
