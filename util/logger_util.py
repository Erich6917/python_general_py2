# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 
# @Author  : ErichLee ErichLee@qq.com
# @File    : logger_util.py
# @Comment : 打印工具
#            
import logging


def infos(*args):
    if args:
        # str_list = []
        # for each in args:
        #     str_list.append(str(each))
        # msg = ' '.join(str_list)
        # print msg

        msg_arr = [str(each) for each in args]
        msg = ' '.join(msg_arr)
        print msg
        logging.info(args)


def ljinfos(lmgs, *args):
    """
    :param lmgs: 左对齐打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print '[{}]:'.format(lmgs.ljust(30)),
    else:
        print '[{}]'.format("".ljust(30)),

    if any(args):
        for each in args:
            print each,
    print


def cinfos(lmgs, *args):
    """
    :param lmgs: 居中打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print '[{}]:'.format(lmgs.center(30)),
    else:
        print '[{}]'.format("".center(30)),

    if any(args):
        for each in args:
            print each,
    print


def println():
    print '================================'


def errors(*args):
    if args:
        # str_list = []
        # for each in args:
        #     str_list.append(str(each))
        # msg = ' '.join(str_list)
        msg_arr = [str(each) for each in args]
        msg = ' '.join(msg_arr)
        # print msg
        print '[ERROR]: {}'.format(msg)
        logging.info(args)
