def convert_ubb_to_markdown(s):
    # 定义UBB标签和对应的转换规则
    tags = {
        'quote': '[quote]',
        'quote_end': '[/quote]',
        'b': '[b]',
        'b_end': '[/b]',
        'u': '[u]',
        'u_end': '[/u]',
        'del': '[del]',
        'del_end': '[/del]',
        'color': '[color=blue]',
        'color_end': '[/color]'
    }

    # 将UBB标签转换为Markdown和HTML混合格式
    replacements = {
        'quote': '>',
        'b': '**',
        'u': '<u>',
        'del': '~~',
        'color': '<font color="#0000FF">',
        'quote_end': '',  # 去除[/quote]标记
        'b_end': '**',
        'u_end': '</u>',  # Markdown中下划线需要使用两个下划线包围内容
        'del_end': '~~',
        'color_end': '</font>'
    }

    # 遍历转换规则并应用到字符串s上
    for ubb, md in replacements.items():
        s = s.replace(tags[ubb], md)

    # 单独处理url标签
    s = s.replace('[url=', '[查看原帖](https://www.cc98.org/')
    s = s.replace('>>查看原帖<<', '')
    s = s.replace('[/url]', '')

    return s

# 读取输入
s1 = input("请输入UBB: ")
# 转换UBB到Markdown和HTML混合格式
s_new = convert_ubb_to_markdown(s1)

# 输出结果
print("markdown: ", s_new)
