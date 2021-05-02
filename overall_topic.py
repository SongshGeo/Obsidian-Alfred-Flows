#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import sys
import os
from workflow import Workflow
reload(sys) 
sys.setdefaultencoding("utf-8")


def search_files_content(wf, keyword):
    """
    搜索知识库，查看有多少匹配搜索的关键词
    Args:
        wf: WorkFlow 对象
        keyword: 搜索的关键词
    Returns: 对知识库中所有文件夹内的匹配次数进行统计
    """
    # 在知识库中搜索
    knowledge_path = os.getenv('knowledge', '').strip()
    tag_path = os.getenv('topic_path', '').strip()

    # 一个计数字典，数每个文件夹里
    count_dic = {}
    sub_dirs = {}
    total = 0

    # 遍历知识库中的所有文件夹，对每个文件夹获取绝对路径
    for item in os.listdir(knowledge_path):
        unhidden_folder_path = os.path.join(knowledge_path, item.strip("."))
        rule_1 = os.path.isdir(unhidden_folder_path)
        if rule_1:
            sub_dirs[item] = unhidden_folder_path

    # 对获取的路径按文件夹名字进行排序，并遍历统计次数
    for folder in sorted(sub_dirs):
        count_dic[folder] = 0
        folder_path = os.path.join(knowledge_path, folder)
        for root, dirs, files in os.walk(folder_path):
            for doc in files:
                if doc.endswith(".md"):
                    filename = os.path.join(root, doc)
                    try:
                        file_obj = open(filename, 'r')
                    except IOError, e:
                        print "File open error: ", e
                    else:
                        # 遍历行
                        text = file_obj.read()
                        # 判断是否包括搜索的关键字
                        if keyword in text:
                            count_dic[folder] += 1
                            total += 1

    path = os.path.join(knowledge_path, tag_path, "%s.md" % keyword)
    wf.add_item(
        title="%d matched in sum." % total,
        subtitle="Create this keyword as your 'Topic'?",
        valid=True,
        arg=path
    )
    return count_dic


def save_fre_into_item(wf, count_dic, query):
    """
    将每个文件夹单独的统计频次保存到 Alfred 中并反馈。
    Args:
        wf: WorkFlow 对象
        count_dic: 统计频次的文件夹
        query: 查询词
    """
    for folder in sorted(count_dic):
        wf.add_item(
            title=folder,
            subtitle="There are %s related results in this category." % count_dic[folder],
            valid=False,
            arg=query
        )


def main(wf):
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    # If script was passed a query, use it to filter file
    if query:
        count = search_files_content(wf, query)
        save_fre_into_item(wf, count, query)
    # Send feedbacks into alfred
    wf.send_feedback()


if __name__ == u"__main__":
    workflow = Workflow()
    sys.exit(workflow.run(main))
