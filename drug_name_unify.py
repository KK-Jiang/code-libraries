# -*- coding: utf-8 -*-
"""
# Copyright (c) 2019 LinkDoc, Inc. All Rights Reserved
# @file    : drug_name_unify.py
# @date    : 2019/12/6 2:40 下午
# @author  : kaijiang@linkdoc.com
# @brief   : 
"""

from __future__ import unicode_literals
import pandas as pd
from drug_unify.standardize.standardizer import Standardizer
from drug_unify.kb.entity import Trademark, GenericName, Constituent


def drug_name_unify(drug_list):
    std = Standardizer()

    unify_objects = []
    for origin_name in drug_list:
        try:
            res = std.run(origin_name)
        except Exception as e:
            print(e, '\t', origin_name)
            continue
        else:
            unify_objects.append(res)

    return unify_objects


def get_object_name(unify_objects, object_name):
    unify_names = []
    for single_object in unify_objects:
        flag = True
        for res in single_object:
            if isinstance(res, object_name):
                unify_names.append(res.name_zh)
                flag = False
                break
        if flag:
            unify_names.append('')
    return unify_names


if __name__ == '__main__':
    file_path = '/Users/kk_j/Documents/Bone_Marrow_Suppression/data/医大一药品名_classfiy.csv'
    drug_df = pd.read_csv(file_path, encoding='utf-8')
    print('Open file Done!')
    drug_names = drug_df['药品名'].tolist()

    unify_res_objects = drug_name_unify(drug_names)
    print('unify process done!')
    unify_drugs = get_object_name(unify_res_objects, Constituent)

    print(drug_df.shape, len(unify_res_objects), len(unify_drugs))
    drug_df['unify_name'] = unify_drugs
    drug_df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print('Done!')
