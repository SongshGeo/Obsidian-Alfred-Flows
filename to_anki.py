#!/usr/bin/env python
# -*-coding:utf-8 -*-
# Created date: 2021/5/6
# @Author  : Shuang Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Research Gate: https://www.researchgate.net/profile/Song_Shuang9

import re
from overall_topic import *
from workflow import Workflow
reload(sys)
sys.setdefaultencoding("utf-8")
ANKI_OUTPUT = os.getenv('anki_output', '').strip()


# 这是一个案例，我们的代码就是从文档中查找类似的结构
# This is a demo for template.
test = """
Experts (2021-05-05): 
> Text: 当然主旋律和主流是不同的，不要怕主流语言。这个时代已经新到你在说边缘的适合，你已经在主流当中了。包括另类，另类现在已经变主流了。
> Source: *p77, 李玉*
> Notes: 有人随着大潮沉浮，有人追逐着浪尖儿，而有远见的人早已预测了浪潮奔去的方向

Experts (2021-05-05): 
> Text: 电影与文学一样，想象力很重要。但电影往往要将想象力具体化，是一种受到限制的想象力。文学你怎么努力地描写也不可能把描写对象复原成一个实物吧，这样读者就有了一个想象的空间，想象的余地。
> Source: *p167 万玛*
> Notes: 电影与文学想象力的不同。
"""


def match_markdowns(wf):
    """
    查询所有有摘录的文档，并展示
    Args:
        wf: Alfred Workflow

    Returns: 列表，里面是知识库里所有的摘录，按以下顺序组成元组 (0, 1, 2, 3, 4)：
    date, text, source, notes, name
        0: date, 摘录的时间,
        1: text, 摘录的文本,
        2: source, 摘录源（具体的页码、谁说的话）
        3: notes, 自己在书页边做的批注
        4: name, 摘录的笔记名（通常就是书名）
    """
    wf.add_item(
        title="Export all experts.",
        subtitle="",
        valid=True,
        arg=","
    )
    markdowns = get_all_markdown_file_paths()

    matched_files = {}
    pattern = r"\W+Experts.+(\d{4}-\d{2}-\d{2}).+\n+>\W+(.*)\n+>\W+(.*)\n+>\W+(.*)"
    all_results = []
    for filepath in markdowns:
        filename = markdowns[filepath].strip(".md")
        with open(filepath, 'r') as file_obj:
            text = file_obj.read()
        if "Experts" in text:
            search_obj = re.findall(pattern, text, re.M | re.I)
            search_obj = [obj + (filename, ) for obj in search_obj]
        else:
            continue
        experts = len(search_obj)
        if experts > 0:
            all_results.extend(search_obj)
            matched_files[filename] = experts
    sorted_dic = sorted(matched_files.items(), key=lambda item: item[1], reverse=True)
    for filename, experts in sorted_dic:
        wf.add_item(
            title=filename,
            subtitle="%d experts in this note." % experts,
            valid=False,
        )
    wf.send_feedback()
    return all_results


def main(wf):
    """
    将所有摘录导出为anki卡片
    Args:
        wf: Alfred 工作流对象
    """
    # 获取所有满足条件的摘录
    matched_results = match_markdowns(wf)
    lines = []
    for date, text, source, notes, name in matched_results:
        # Anki 卡的正面：摘录原文、笔记名称
        front = text + "    ——<%s>" % name
        # Anki 卡的背面：摘录笔记、摘录来源、摘录时间
        back = "    ".join([notes, "——<%s>" % source, "(%s)" % date])

        # 用分号分割，导出到 Anki 可以直接导入的 txt 文件中
        tup = (front, back, name)
        line = ";".join(tup)
        lines.append(line)
    anki = "\n".join(lines)

    with open(ANKI_OUTPUT+r"/anki_output.txt", 'w') as anki_file:
        anki_file.write(anki)
        anki_file.close()


if __name__ == u"__main__":
    workflow = Workflow()
    sys.exit(workflow.run(main))
