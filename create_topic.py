#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# Created date: 2021-05-02
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import sys
from datetime import date
from workflow import Workflow
reload(sys)
sys.setdefaultencoding("utf-8")


def main(wf):
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    d = date.today().strftime("%Y-%m-%d")
    text = """创建日期: %s\n中译：\n变体：""" % d

    with open(query, 'w') as markdown_file:
        markdown_file.write(text)
        markdown_file.close()
    pass


if __name__ == u"__main__":
    workflow = Workflow()
    sys.exit(workflow.run(main))
