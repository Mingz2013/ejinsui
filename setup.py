# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import ejinsui


def main():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

    data_dir = 'data'
    ejinsui.run(data_dir)
    pass


if __name__ == '__main__':
    main()