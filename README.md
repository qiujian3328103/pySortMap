# pySortMap

pySortMap is a PyQt5 based Graphic User Interface used in Semiconductor Yield Analysis

[![Travis](https://img.shields.io/travis/dougthor42/wafer_map.svg)](https://travis-ci.org/dougthor42/wafer_map)
[![AppVeyor](https://img.shields.io/appveyor/ci/dougthor42/wafer-map.svg)](https://ci.appveyor.com/project/dougthor42/wafer-map)
[![PyPI](https://img.shields.io/pypi/v/wafer_map.svg)](https://pypi.python.org/pypi/wafer_map/)
[![PyPI](https://img.shields.io/pypi/pyversions/wafer_map.svg)](https://pypi.python.org/pypi/wafer_map/)
<!-- [![PyPI](https://img.shields.io/pypi/wheel/wafer_map.svg)](https://pypi.python.org/pypi/wafer_map/) -->

# Summary 

pySortMap is a graphical user interface (GUI) visulization tools developed using PyQt5 to 

# Functionality

- Interactive Wafer Sort Map Visualization 
- Post Fab Inkoff Function 
- Auto inkoff 
- Auto Inkoff file and ink off map generation and download 
- Wafer Stack and Heat Map Analysis 

## Import Data Type
Three **.csv files** needs to upload 

1. **ucs_map.csv** - use to define the differnet product sort map layout 
2. ***bin_config.csv*** - use to define the each die pass/fail type and bin color setting after the sort test 
3. **bin_data.csv** - each die pass or fail info

## UCS Map Define

The wafer universal coordinate system (UCS) is use to define the wafer layout during the sort test , inline test or other semiconductor process steps. pySortMap use the .csv files to define the wafer layout before load the bin data. The program can be also customized and modified by developers to suit different file types such as STDF file or dirrectly connect to the database. 

The usc_map.csv must contains the following 7 columns:

| ORGIN_X | ORIGIN_Y | Width | Height | DIE_X | DIE_Y | TEST_FLAG |
| :-----: | :------: | :---: | :----: | :---: | :---: | :-------: |
| -112008 |  66372   | 6223  |  5098  |   0   |   1   |     T     |

