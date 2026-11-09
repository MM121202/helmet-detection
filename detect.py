# 检测脚本：用训好的模型去检测图片，结果会画好框存到 runs/detect/predict
import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="要检测的图片或文件夹路径")
    parser.add_argument("--weights", default="runs/detect/helmet-v1/weights/best.pt",
                        help="用哪个模型，默认用第一轮训练训出的最好的那个")
    args = parser.parse_args()

    model = YOLO(args.weights)
    model.predict(
        source=args.source,
        conf=0.5,        # 置信度门槛：模型觉得有五成把握才画框
        save=True,       # 把画好框的结果图存下来
    )

if __name__ == "__main__":
    main()
