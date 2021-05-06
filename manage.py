#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2021/5/6
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9


from overall_topic import *
from to_anki import match_markdowns
from workflow import Workflow
reload(sys)
sys.setdefaultencoding("utf-8")

CHOICES = {
    'anki': "Export experts notes to anki.",
    'clean': "Clean untitled rubbish files.",
}


def show_choices(wf, query):
    """
    展示所有功能，利用 query 可以查询功能
    Args:
        wf: Alfred WorkFlow
        query: 查询关键词

    Returns:

    """
    for choice in CHOICES:
        # 利用注释可以尽快找到对应的功能
        if query in CHOICES[choice]:
            wf.add_item(
                title=choice,
                subtitle=CHOICES[choice],
                valid=True,
                arg=choice
            )
    wf.send_feedback()


def main(wf):
    """
    管理 Obsidian 的一系列工具，自动展示我已经做了哪些工具
    Args:
        wf: Alfred Workflow
    Returns:
    """
    query = wf.args[0]
    if not isinstance(query, unicode):
        query = query.decode('utf-8')
    else:
        query = query.strip().lower()

    if query in CHOICES:
        if query == 'anki':
            match_markdowns(wf)
    else:
        show_choices(wf, query)
    pass


if __name__ == u'__main__':
    workflow = Workflow()
    sys.exit(workflow.run(main))
