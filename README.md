# SAPNet for image deraining
Python 3320 Project. \
Changjie Lu, Yinhao Liu

# Model Architecture
Click this following link to view the pdf.

![Model Architecture Figure](resources/main_figure.pdf)

# Comparison on Synthetic Rainy Images
From left to right, Rainy, PreNet (CVPR 2019), MSPFN (CVPR 2020), MPRNet (CVPR 2021), SAPNet (Ours)

<p float="left">
<p align="middle">
  <img src="resources/rain-064.jpg" width="170" />
  <img src="resources/PreNet-064.jpg" width="170" /> 
  <img src="resources/MSPFN-064.jpg" width="170" />
  <img src="resources/MPRNet-064.png" width="170" />
  <img src="resources/Ours-064.jpg" width="170" /> 
</p>

# Comparison on Real-World Rainy Images
From left to right, Rainy, PreNet (CVPR 2019), MSPFN (CVPR 2020), MPRNet (CVPR 2021), SAPNet (Ours)

<p float="left">
<p align="middle">
  <img src="resources/rainy_.jpg" width="170" />
  <img src="resources/PreNet.jpg" width="170" /> 
  <img src="resources/MSPFN.jpg" width="170" />
  <img src="resources/MPRNet.png" width="170" />
  <img src="resources/ours.jpg" width="170" /> 
</p>

# Prerequisites
* Windows or Linux
* CUDA 10.0, or CPU
* Python 3.6+
* Pytorch 1.2+
* torchvision 0.4+
* opencv-python
* scikit-image
* numpy

# Preparing Dataset
- Download training and testing dataset from either link 
[BaiduYun](https://pan.baidu.com/s/1J0q6Mrno9aMCsaWZUtmbkg#list/path=%2Fsharelink3792638399-290876125944720%2Fdatasets&parentPath=%2Fsharelink3792638399-290876125944720)
[OneDrive](https://onedrive.live.com/?cid=066ce859ab42dfa2&id=66CE859AB42DFA2%2130078&authkey=%21AIYIy8ZKL9kkmd4)

- Create a new folder called `dataset`.
- Create sub-folders called `train` and `test` under that folder. 
- Place the unzipped folders into `datasets/train/` (training data) and `datasets/test/` (testing data)

# Training
Run the following script in terminal
```
python train.py
```

# Testing
Run the following script in terminal
```
bash main.sh
```

You can modify the content of `main.sh` according to your hyperparameters. For example.
```
python test.py \
      --save_path logs/SAPNet/Model11 \
      --test_data_path datasets/test/Rain100H \
      --output_path results/Rain100H/Model11 \
      --use_dilation True
```

# Hyperparameters
## General Hyperparameters
| Name       | Type  | Default             | Description |
|------------|-------|---------------------|-------------|
| preprocess | bool  | False               | Whether to preprocess the training images as h5 file            |
| batch_size | int   | 12                  | training batch size            |
| epochs     | int   | 100                 | training epochs            |
| milestone  | int   | [30,50,80]          | when to decay the learning rate            |
| lr         | float | 0.001               | learning rate            |
| save_path  | str   | logs/SAPNet/Model11 | where to save the weight            |
| save_freq  | int   | 1                   | frequency for saving the weight            |

## Train/Test Hypeparameters
| Name            | Type | Default                   | Description |
|-----------------|------|---------------------------|-------------|
| test_data_path  | str  | datasets/test/Rain100H    | testing data path           |
| output_path     | str  | results/Rain100H/Model11  | testing result path        |
| data_path       | str  | datasets/train/RainTrainH | training data path            |
| use_contrast    | bool | True                      | whether to use contrast learning            |
| use_seg_stage1  | bool | True                      | whether to use segmentation            |
| use_stage1      | bool | True                      | whether to use deraining            |
| use_dilation    | bool | True                      | whether to use dilation            |
| recurrent_iter  | int  | 6                         | numbers of recurrence            |
| num_of_SegClass | int  | 21                        | numbers of segmentation classes            |


