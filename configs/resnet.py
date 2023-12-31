
from . import constant

parameters = {
        'ResNet' : { "lr": 0.1, "epochs": 90, "weight_decay": 1e-4, "batch_size": 256, "nesterov": True,  "init_backbone":True, "init_extractor":True,},
        }

backbone_config = {
        "ResNet50" : {"layers": [3, 4, 6, 3], "dropout": 0, "groups": 1, "width_per_group": 64, "channels": 3,},
        "ResNet101" : {"layers": [3, 4, 23, 3], "dropout": 0, "groups": 1, "width_per_group": 64, "channels": 3,},
        }

train = { 
        # ResNet 50
        'ResNet50-standard': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-auto_augment': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-cutout': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-cutmix': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet50-mixup': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'ResNet50-standard-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-auto_augment-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-cutout-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-cutmix-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet50-mixup-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },

        'ResNet50-auto_augment-cutout-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-auto_augment-cutmix-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet50-auto_augment-mixup-agmax': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'ResNet50-auto_augment-cutout': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet50-auto_augment-cutmix': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet50-auto_augment-mixup': {  "backbone": 'ResNet50',
                                        "backbone_config": backbone_config['ResNet50'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        # ResNet101
        'ResNet101-standard': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-auto_augment': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-cutout': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-cutmix': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet101-mixup': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'ResNet101-standard-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-auto_augment-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-cutout-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-cutmix-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet101-mixup-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },

        'ResNet101-auto_augment-cutout-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-auto_augment-cutmix-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet101-auto_augment-mixup-agmax': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'ResNet101-auto_augment-cutout': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": True, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'ResNet101-auto_augment-cutmix': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'ResNet101-auto_augment-mixup': {  "backbone": 'ResNet101',
                                        "backbone_config": backbone_config['ResNet101'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['ResNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        }
