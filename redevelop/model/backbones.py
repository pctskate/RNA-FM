# encoding: utf-8
"""
@author:  Jiayang Chen
@contact: yjcmydkzgj@gmail.com
"""

import fm

def choose_backbone(backbone_name, model_location=None):
    if backbone_name == 'rna-fm':
        backbone, backbone_alphabet = fm.pretrained.rna_fm_t12(model_location)
    elif backbone_name == 'mrna-fm':
        backbone, backbone_alphabet = fm.pretrained.cds_fm_t12(model_location)
    else:
        raise Exception("Wrong Backbone Type! {}".format(backbone_name))

    return backbone, backbone_alphabet