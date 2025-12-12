#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/8/28 15:00
Desc: To test intention, just write test code here!
"""

import pathlib

from akshare.datasets import get_ths_js, get_crypto_info_csv
from akshare.air_zhenqi import air_city_table, air_quality_watch_point, air_quality_hist, air_quality_rank


def test_cost_living():
    """
    just for test aim
    :return: assert result
    :rtype: assert
    """
    pass


def test_path_func():
    """
    test path func
    :return: path of file
    :rtype: pathlib.Path
    """
    temp_path = get_ths_js("ths.js")
    assert isinstance(temp_path, pathlib.Path)


def test_zipfile_func():
    """
    test path func
    :return: path of file
    :rtype: pathlib.Path
    """
    temp_path = get_crypto_info_csv("crypto_info.zip")
    assert isinstance(temp_path, pathlib.Path)

def test_by_sungang():
    air_city_table_df = air_city_table()
    print(air_city_table_df)

    air_quality_watch_point_df = air_quality_watch_point(
        city="杭州", start_date="20220408", end_date="20220409"
    )
    print(air_quality_watch_point_df)

    air_quality_hist_df = air_quality_hist(
        city="北京",
        period="day",
        start_date="20220801",
        end_date="20240402",
    )
    print(air_quality_hist_df)

    air_quality_rank_df = air_quality_rank()
    print(air_quality_rank_df)

if __name__ == "__main__":
    # test_cost_living()
    test_path_func()
    test_zipfile_func()
    test_by_sungang()
    
