import os
import torch
import argparse
import SimpleITK as sitk
import numpy as np
from networks.ABCNet import ABCNet

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=str, default='0', help='GPU to use')
    parser.add_argument('--input_dir', type=str, default='/input', help='path to input')
    parser.add_argument('--output_dir', type=str, default='/output', help='path to input')
    parser.add_argument('--model_pth', type=str, default='./save_pths/ABC_test.pth', help='model saved pth')  #
    args = parser.parse_args()

    # load your model parameters, here is just an example code.
    # model = ABCNet()
    # model.load_state_dict(torch.load(args.model_pth)['model_state_dict'])

    # predict the results, here is just an example. Pls build your own logic here
    for subdir, dirs, files in os.walk(args.input_dir):
        for file in files:
            if file.endswith('_gt.nii.gz'):
                file_path = os.path.join(subdir, file)
                img = sitk.ReadImage(file_path)
                predict = sitk.BinaryThreshold(img, lowerThreshold=400, upperThreshold=500)

                '''
                pls check the resolution of the predict mask, making it same with the input 
                For example: input (640,640,44)--> output (640,640,44)
                '''
                pred_file_name = file.replace('_gt', '_label')
                sitk.WriteImage(predict, os.path.join(args.output_dir, pred_file_name))

    print('Generate finished!')
