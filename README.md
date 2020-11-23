# pyQT_data_plotting

This program is aimed to plot scatter chart from large data( e.g 100MB+ ).



## How does it work

* Front end: QT 
* Back end: python 3.8

<img src="/Users/y.k.shang/Google Drive/Fang/pyQT_data_plotting/README.assets/Screen Shot 2020-11-24 at 01.01.34.png" alt="Screen Shot 2020-11-24 at 01.01.34" style="zoom: 25%;" />



## How to start

#### Step1 Set up your environment

* For **MacOS** or **Linux**: Do nothing : )

* For Windows : (

You'd better install WLS

Here is the tutoral on how to install WLS in windows:[WSL 使用指南——02 安装配置](https://zhuanlan.zhihu.com/p/34885182)

After you have finished, you can use Windows just like Linux.



#### Step2 Install anaconda

[两行代码下载安装Anaconda（linux环境）](https://blog.csdn.net/lwgkzl/article/details/89329383)

After you have set up **anaconda** environment, things will be easy and clear.:1st_place_medal:

use this command to check if anaconda is installed correctly.

```shell
conda -V
```

if the output is :

<img src="/Users/y.k.shang/Google Drive/Fang/pyQT_data_plotting/README.assets/Screen Shot 2020-11-24 at 01.13.02.png" alt="Screen Shot 2020-11-24 at 01.13.02" style="zoom:50%;" />

Congratulations!

For more infomation about anaconda, you can search google or visit their [office site](https://www.anaconda.com)

#### Step3 Check your data file 

In this step, you should place your **data file** in right place.

Actually, you can place data file in any place, if you remember to change the file path code in `get_img.py`.

**In this program**, you can just put `pyQT_data` file in the same direction.



The structure of this program is as follows:

```
.
├── pyQT_data
├── pyQT_data_plotting
    ├── LICENSE
    ├── README.assets
    │   ├── Screen\ Shot\ 2020-11-24\ at\ 01.01.34.png
    │   └── Screen\ Shot\ 2020-11-24\ at\ 01.13.02.png
    ├── README.md
    ├── main.py
    ├── resources
    │   └── img
    └── src
        ├── __pycache__
        │   ├── get_img.cpython-37.pyc
        │   └── get_img.cpython-38.pyc
        └── get_img.py
```



#### Step4 Run and enjoy :P

In `pyQT_data_plotting` file , type

```shell
python main.py
```

to start QT.



**There are three modes in total:**

* Weekend mode :

red dot for `weekday`

blue dot for `weekend`

![Screen Shot 2020-11-24 at 01.24.36](/Users/y.k.shang/Google Drive/Fang/pyQT_data_plotting/README.assets/Screen Shot 2020-11-24 at 01.24.36.png)



* Day_night mode:

green dot for `night time` 

black dot for `night time`

<img src="/Users/y.k.shang/Google Drive/Fang/pyQT_data_plotting/README.assets/Screen Shot 2020-11-24 at 01.25.42.png" alt="Screen Shot 2020-11-24 at 01.25.42" style="zoom:50%;" />



* season mode

Green dot for `spring`

Red dot for `summer`

Orange  dot for `fall`

Blue dot for `winter`

![Screen Shot 2020-11-24 at 01.26.55](/Users/y.k.shang/Google Drive/Fang/pyQT_data_plotting/README.assets/Screen Shot 2020-11-24 at 01.26.55.png)