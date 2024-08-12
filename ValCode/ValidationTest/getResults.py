import numpy as np
from medpy import metric
from tqdm import tqdm
import os
import pandas as pd
from collections import OrderedDict
import SimpleITK as sitk

def test_all(gt_pth, pred_prefixs, test_save_path, test_part=2):
    total_metric = 0.0
    metric_dict = OrderedDict()
    metric_dict['name'] = list()
    metric_dict['dice'] = list()
    metric_dict['95hd'] = list()

    with open(gt_pth, 'r') as file:
        gt_list = [line.strip() for line in file]
    gt_list = sorted(gt_list)

    for gt_single_path in tqdm(gt_list):
        id_name = os.path.split(gt_single_path)[-1]
        pred_single_pth = gt_single_path.replace('0_ValidationWithLabelGT', pred_prefixs)

        gt_label = sitk.ReadImage(gt_single_path)
        gt_label = sitk.GetArrayFromImage(gt_label) == test_part        # get corresponding gt label

        pred_label = sitk.ReadImage(pred_single_pth)
        pred_label = sitk.GetArrayFromImage(pred_label) == test_part    # get corresponding prediction label

        single_metric = calculate_metric_percase(gt_label, pred_label)

        metric_dict['name'].append(id_name)
        metric_dict['dice'].append(single_metric[0])
        metric_dict['95hd'].append(single_metric[1])
        total_metric += np.asarray(single_metric)

    # average metrics
    average_metric = total_metric / len(gt_list)
    metric_dict['name'].append('Average metrics: ')
    metric_dict['dice'].append(average_metric[0])
    metric_dict['95hd'].append(average_metric[1])

    metric_csv = pd.DataFrame(metric_dict)

    if test_part == 1:
        save_name = pred_prefixs[-4:] + '_Wall'
    elif test_part == 2:
        save_name = pred_prefixs[-4:] + '_RA'
    elif test_part == 3:
        save_name = pred_prefixs[-4:] + '_LA'
    else: save_name = 'None'

    metric_csv.to_csv(os.path.join(test_save_path, f'metric_{save_name}.csv'), index=False)
    print('average metric {} is {}'.format(save_name, average_metric))

    return average_metric


def calculate_metric_percase(pred, gt):
    dice = metric.binary.dc(pred, gt)
    hd95 = metric.binary.hd95(pred, gt, voxelspacing=(2.5, 0.625, 0.625))
    print('dice, hd95', dice, hd95)
    return dice, hd95


if __name__ == '__main__':
    gt_pth = '../ValidationPhaseFiles/0_gt_label.list'
    pred_prefixs_all = ['Team1_TeamName_TeamLeader/TeamName_ValPhase_Try1']
    result_Wall, result_RA, result_LA = [], [], []

    for pred_prefixs in pred_prefixs_all:
        test_save_path = os.path.join('../ValidationPhaseFiles/', os.path.split(pred_prefixs)[0])
        wall_score = test_all(gt_pth, pred_prefixs, test_save_path, test_part=1)
        ra_score = test_all(gt_pth, pred_prefixs, test_save_path, test_part=2)
        la_score = test_all(gt_pth, pred_prefixs, test_save_path, test_part=3)
        result_Wall.append(wall_score)
        result_RA.append(ra_score)
        result_LA.append(la_score)

    print('result_Wall: ', result_Wall)
    print('result_RA: ', result_RA)
    print('result_LA: ', result_LA)

