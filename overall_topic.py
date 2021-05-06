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

REP = os.getenv('knowledge', '').strip()
IGNORE = [folder.strip() for folder in os.getenv('ignore', '').split(",")]


def get_file_paths():
    """
    遍历知识库，获得知识库下每个子文件夹的名字与路径
    Returns: 字典对象，所有知识库下的子文件夹
    """
    sub_dirs = {}
    # 遍历知识库中的所有文件夹，对每个文件夹获取绝对路径
    for item in os.listdir(REP):
        unhidden_folder_path = os.path.join(REP, item.strip("."))
        rule_1 = os.path.isdir(unhidden_folder_path)
        rule_2 = item not in IGNORE
        if rule_1 & rule_2:
            sub_dirs[item] = unhidden_folder_path

    return sorted(sub_dirs)


def get_all_markdown_file_paths():
    sub_dirs = get_file_paths()
    file_dic = {}
    # 对获取的路径按文件夹名字进行排序，并遍历统计次数
    for sub_dir in sub_dirs:
        folder_path = os.path.join(REP, sub_dir)
        for root, dirs, files in os.walk(folder_path):
            for doc in files:
                if doc.endswith(".md"):
                    file_path = os.path.join(root, doc)
                    file_dic[file_path] = doc
                else:
                    pass
    return file_dic


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
    total = 0

    # 对获取的路径按文件夹名字进行排序，并遍历统计次数
    for sub_dir in get_file_paths():
        count_dic[sub_dir] = 0
        folder_path = os.path.join(knowledge_path, sub_dir)
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
                            count_dic[sub_dir] += 1
                            total += 1

    path = os.path.join(knowledge_path, tag_path, "%s.md" % keyword)
    wf.add_item(
        title="%d matched notes in sum." % total,
        subtitle="Create '%s' as your 'Topic'?" % keyword,
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
    for item in sorted(count_dic):
        wf.add_item(
            title=item,
            subtitle="There are %s related results in this category." % count_dic[item],
            valid=False,
            arg=query
        )


def main(wf):
    # Get query from Alfred
    query = wf.args[0]
    if not isinstance(query, unicode):
        query = query.decode('utf-8')
    else:
        query = query.strip().lower()

    # If script was passed a query, use it to filter file
    count = search_files_content(wf, query)
    save_fre_into_item(wf, count, query)
    # Send feedbacks into alfred
    wf.send_feedback()


if __name__ == u"__main__":
    workflow = Workflow()
    sys.exit(workflow.run(main))
