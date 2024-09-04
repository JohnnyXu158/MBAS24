from networks.VNet import VNet
# from networks.UNet import UNet
# from networks.UNet3D import UNet3D
# from networks.UNet3D_org import UNet3D_org
# from networks.DPBNetV1 import DPBNetV1
# from networks.DPBNetV2 import DPBNetV2       # 类似ghostNet
# from networks.DPBNetV3 import DPBNetV3      # 都是从input导出两个分支，不替换conv2 这个效果还好哦
# from networks.DPBNetV4 import DPBNetV4      # 都是从input导出两个分支，并且把conv2替换
# from networks.DPBNetV5 import DPBNetV5      # 都是从input导出两个分支，并且把conv2替换,优化了一下，先拼接
# from networks.DPBNetV6 import DPBNetV6      # 都是从input导出两个分支，优化一下先concat，把Conv2保留，不替换！
# from networks.DPBNetV7 import DPBNetV7      # 都是从input导出两个分支，优化一下先concat，把Conv2保留，不替换！
# from networks.DPBNetV8 import DPBNetV8      # 都是从input导出两个分支，优化一下先concat，把Conv2保留，不替换！
#
# from networks.UN_SMLNet import UN_SMLNet
# from networks.LiteVNet import LiteVNet
# from networks.LiteVNetV2 import LiteVNetV2
# from networks.LiteVNetV3 import LiteVNetV3
#
# from monai.networks.nets import SwinUNETR, UNETR
import torch

def net_factory(model_name="VNet", in_channels=1, num_classes=2, normalization='batchnorm', activate = 'relu', has_dropout=False, mode="train", img_size=(64,256,256)):
    if mode == 'train':
        if model_name =='UNet3D':
            net = UNet3D(in_channels=in_channels, n_classes=num_classes)
        elif model_name =='UNet3D_org':
            net = UNet3D_org(in_channels=in_channels, n_classes=num_classes)
        elif model_name == 'VNet':
            net = VNet(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout)
        elif model_name =='UN_SMLNet':
            net = UN_SMLNet(n_channels=in_channels, n_classes=num_classes, normalization=normalization, ratio=4, has_att=True, has_dropout=has_dropout)
            # net = UN_SMLNet(n_channels=in_channels, n_classes=num_classes, n_filters=16, normalization='groupnorm', ratio=4, has_att=True, has_dropout=has_dropout)
        elif model_name == 'UNETR':
            net = UNETR(in_channels=in_channels, out_channels=num_classes, img_size=img_size)
        elif model_name == 'SwinUNETR':
            net = SwinUNETR(img_size=img_size, in_channels=in_channels, out_channels=num_classes, feature_size=48, use_checkpoint=False)
            # net.load_from(weights=torch.load("/hpc/fxu244/Documents/Code/LAProject/DPBNet/pre_weight/model_swinvit.pt"))
        elif model_name == 'DPBNetV1':
            net = DPBNetV1(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout)
        elif model_name == 'DPBNetV2':
            net = DPBNetV2(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        elif model_name == 'DPBNetV3':
            net = DPBNetV3(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        elif model_name == 'DPBNetV4':
            net = DPBNetV4(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        
        elif model_name == 'DPBNetV5':
            net = DPBNetV5(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        
        elif model_name == 'DPBNetV6':
            net = DPBNetV6(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        elif model_name == 'DPBNetV7':
            net = DPBNetV7(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        elif model_name == 'DPBNetV8':
            net = DPBNetV8(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)

        elif model_name == 'LiteVNet':
            net = LiteVNet(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout)
        
        elif model_name == 'LiteVNetV2':
            net = LiteVNetV2(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        
        elif model_name == 'LiteVNetV3':
            net = LiteVNetV3(in_channels=in_channels, n_classes=num_classes, normalization=normalization, activate=activate, has_dropout=has_dropout, dhw=img_size)
        
        elif model_name == 'UNet':
            net = UNet(in_channels=in_channels, n_classes=num_classes)
        else:
            net = None
    else:
        return None
    return net