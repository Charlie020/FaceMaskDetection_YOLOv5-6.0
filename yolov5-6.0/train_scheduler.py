import os

# 第一个命令
command_1 = 'python train.py --data mask.yaml --cfg models/yolov5s_SmallTarget+CBAM(BefSPPF).yaml --weights yolov5s.pt --batch-size 16 --epochs 200'
os.system(command_1)

# 第二个命令
command_2 = 'python train.py --data mask.yaml --cfg models/yolov5s_SmallTarget+CBAM(AftSPPF).yaml --weights yolov5s.pt --batch-size 16 --epochs 200'
os.system(command_2)
