# helmet-detection：安全帽检测小项目

用 YOLO 训练一个模型，看工地照片里的人有没有戴安全帽。
这个仓库是我学习 YOLO 的"实跑证据"：从找数据、训练、到出结果，全流程都留在这里。

## 这个项目做什么

- **输入**：一张工地/车间的照片
- **输出**：在照片上框出每个人，并标出「戴了安全帽」还是「没戴安全帽」
- **用途**：可以当成工地安全监控的最小原型

## 数据集

来源：Roboflow Universe 上的 [safety-helmet](https://universe.roboflow.com/helmet-tf/safety-helmet-4mhdt/dataset/4)

- 类别只有两个：`Helmet`（戴了）、`No Helmet`（没戴）
- 已经按 train / valid / test 分好文件夹
- 下载时选 **YOLOv8 格式**（解压后直接是 ultralytics 要求的样子）

> 下载需要在 Roboflow 免费注册一个账号，浏览器里点 Export → YOLOv8 即可。
> 数据集不放在仓库里（体积大），放到本地 `data/` 目录，路径见 `train.py` 注释。

## 目录结构

```
helmet-detection/
├── README.md            # 本文件
├── requirements.txt     # 要装哪些库
├── train.py             # 训练脚本
├── detect.py            # 用训好的模型检测图片
├── data/                # 数据集放这里（不上传）
├── runs/                # 训练结果（不上传，只截关键图放 experiments/）
└── experiments/         # 实验记录：每组实验的截图、指标、结论
```

## 怎么跑

### 1. 装依赖

```bash
pip install -r requirements.txt
```

### 2. 下载数据集，解压到 data/ 下

```
data/
└── safety-helmet/
    ├── data.yaml
    ├── train/
    ├── valid/
    └── test/
```

### 3. 训练

```bash
python train.py
```

> 没有独立显卡的话，建议在 Google Colab 或 Kaggle 的免费 GPU 上跑同样这段代码。

### 4. 检测一张图

```bash
python detect.py --source data/test_images/xxx.jpg
```

## 实验记录

所有实验组、指标和结论都写在 [experiments/experiments-log.md](experiments/experiments-log.md)，
每一轮训练做了什么改动、效果如何，都能对上号。

## 学习背景

- 证书：Ultralytics Academy（academy.ultralytics.com）课程同步进行中
- 技术文章：配套文章会引用本仓库的实验结果
