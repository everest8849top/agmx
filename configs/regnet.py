
from . import constant

parameters = {
        'RegNet' : { "lr": 0.1, "epochs": 100, "weight_decay": 5e-5, "batch_size": 128, "nesterov": True,  "init_backbone":True, "init_extractor":True,},
        }



backbone_config = {
        "RegNetX002" : {"channels": 3, "dropout": 0.2,},
        "RegNetY004" : {"channels": 3, "dropout": 0.2,},
        }


train = { 
        # RegNetX002
        'RegNetX002-standard': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'RegNetX002-cutmix': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetX002-standard-agmax': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'RegNetX002-auto_augment-cutmix-agmax': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetX002-auto_augment-mixup-agmax': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'RegNetX002-auto_augment-cutmix': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetX002-auto_augment-mixup': {  "backbone": 'RegNetX002',
                                        "backbone_config": backbone_config['RegNetX002'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        # RegNetY004
        'RegNetY004-standard': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.standard_weights_std,
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'RegNetY004-cutmix': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetY004-standard-agmax': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": False,  "no_basic_augment": False, "cutmix": False, "mixup" : False,
                                     },
        'RegNetY004-auto_augment-cutmix-agmax': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetY004-auto_augment-mixup-agmax': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.agmax_weights_std, 
                                        "agmax" : True,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },
        'RegNetY004-auto_augment-cutmix': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": True, "mixup" : False,
                                     },
        'RegNetY004-auto_augment-mixup': {  "backbone": 'RegNetY004',
                                        "backbone_config": backbone_config['RegNetY004'],
                                        "weights_std": constant.standard_weights_std, 
                                        "agmax" : False,
                                        "parameters" : parameters['RegNet'],
                                        "cutout": False, "auto_augment": True,  "no_basic_augment": False, "cutmix": False, "mixup" : True,
                                     },

        }

