import unicodedata


def _is_punctuation(char):
    """Checks whether `chars` is a punctuation character."""
    cp = ord(char)
    # We treat all non-letter/number ASCII as punctuation.
    # Characters such as "^", "$", and "`" are not in the Unicode
    # Punctuation class but we treat them as punctuation anyways, for
    # consistency.
    if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or
            (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)):
        return True
    cat = unicodedata.category(char)
    if cat.startswith("P"):
        return True
    return False


def filter_space(line):
    n = len(line)
    c = ""
    c.isalnum()
    if len(line) == 0:
        return ""
    l2 = line[0].strip()
    for i in range(1, n):
        if ("a" > line[i - 1].lower() or line[i - 1].lower() > "z" or line[i - 1] == " ") and line[i] == " ":
            continue
        l2 += line[i]

    return l2


def general_clear():
    input_path = "./example_data/text/wiki_corpus.txt"
    output_path = "./example_data/text/wiki_corpus_clear.txt"
    result = []
    with open(input_path, encoding="utf-8") as rfile:
        for line in rfile.readlines():
            line = line.strip().replace("=", "").replace("*", "").replace("#", "").strip()
            line = filter_space(line)
            result.append(line)

    with open(output_path,'w',encoding="utf-8") as wfile:
        for line  in result:
            wfile.writelines(line+"\n")


if __name__ == '__main__':
    general_clear()

    # text = "计划、973计划，强调科学研究，"
    # s = filter_space(text)
    # print(s)
    # input_path = "./example_data/text/wiki_corpus.txt"
    # output_path = "./example_data/text/wiki_part_enum_corpus.txt"
    #
    # result = []
    # count = 0
    # with open(input_path, encoding="utf-8") as rfile:
    #     for line in rfile.readlines():
    #         line = line.strip().replace("=", "").replace("*", "").replace("#", "").strip()
    #         line = filter_space(line)
    #         if len(line) < 4:
    #             continue
    #         # if count< 100000:
    #         #     continue
    #         if count == 200000:
    #             break
    #         # result.append(line)
    #         end = len(line)
    #         start = 0
    #         while start< end:
    #             shift = random.randint(8,20)
    #             text = line[start: start+shift]
    #             text = text.strip()
    #             while len(text) and _is_punctuation(text[-1]):
    #                 text = text[:-1]
    #             start += shift
    #
    #             if len(text)< 8:
    #                 continue
    #
    #             text += random.choice(["。","，"])
    #             result.append(text)
    #             count += 1
    #
    #
    #
    # with open(output_path, 'w', encoding="utf-8") as wfile:
    #     for line in result:
    #         wfile.writelines(line + "\n")

    # path = "/data/wufan/text_renderer/example_data/text/wiki_part_enum_corpus.txt"
    # res = []
    # count = 0
    # with open(path, encoding="utf-8") as rfile:
    #     for line in  rfile.readlines():
    #         count +=1
    #         if count > 100000 and count< 200000:
    #             res.append(line)
    #         if count> 200000:
    #             break
    #
    # path = "/data/wufan/text_renderer/example_data/text/wiki_part_enum_corpusB.txt"
    # with open(path,'w',encoding="utf-8") as wfile:
    #     for line  in  res:
    #         wfile.writelines(line)