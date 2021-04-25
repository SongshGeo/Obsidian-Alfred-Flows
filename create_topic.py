#!/usr/bin/env python 3.83
# -*-coding:utf-8 -*-
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

from os import path
import sys, os
from workflow import Workflow, Variables
reload(sys) 
sys.setdefaultencoding("utf-8")


def search_files_content(knowledge_path, keyword):
    """[Retrieve recent Topic-files from Knowledge Rep.]
    """
    # 一个计数字典，数每个文件夹里
    count_dic = {}
    sub_dirs = {}
    for item in os.listdir(knowledge_path):
        unhidden_folder_path = os.path.join(knowledge_path, item.strip("."))
        rule_1 = os.path.isdir(unhidden_folder_path)
        if rule_1:
            sub_dirs[item] = unhidden_folder_path

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
                        for line in file_obj:
                            # 判断是否包括搜索的关键字
                            if keyword in line:
                                count_dic[folder] += 1
    return count_dic


def save_fre_into_item(wf, count_dic):
    for folder in sorted(count_dic):
        wf.add_item(
            title=folder,
            subtitle="There are %d related notes in this category." % count_dic[folder],
            valid=True
        )
    wf.send_feedback()


def main(wf):
    # Get query from Alfred
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    # 在知识库中搜索
    knowledge_path = os.getenv('knowledge', '').strip()

    # If script was passed a query, use it to filter file
    if query:
        count = search_files_content(knowledge_path, query)
        save_fre_into_item(wf, count)


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
