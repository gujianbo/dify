# coding=utf-8
import jieba
import re

class Tokenizer:
    def __init__(self):
        self.patterns = []
        self.patterns.append(r"[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)+")

    def extract_pattern(self, text):
        matches = []
        for pattern in self.patterns:
            # print(pattern)
            for match in re.finditer(pattern, text):
                matches.append((match.start(), match.end(), match.group(0)))
                # print(match)
        sorted_matches = sorted(matches, key=lambda x: x[0])
        return sorted_matches

    def tokenize(self, words):
        # print(words)
        matches = self.extract_pattern(words)
        # print(matches)
        segmentation = jieba.tokenize(words, mode="search")
        if len(matches) == 0:
            return [x[0] for x in segmentation]
        new_seg = []
        m_idx = 0
        for tk in segmentation:
            word = tk[0]
            start = tk[1]
            end = tk[2]
            need_insert = False
            match_str = ""
            if m_idx < len(matches):
                if matches[m_idx][1] < end:
                    need_insert = True
                    match_str = matches[m_idx][2]
                    m_idx += 1
                elif matches[m_idx][1] == end and matches[m_idx][0] == start:
                    m_idx += 1
                elif matches[m_idx][1] == end and matches[m_idx][0] != start:
                    need_insert = True
                    match_str = matches[m_idx][2]
                    m_idx += 1
            new_seg.append(word)
            if need_insert:
                new_seg.append(match_str)
        return new_seg

tokenizer = Tokenizer()

# if __name__ == "__main__":
#     tokenizer = Tokenizer()
#     t = tokenizer.tokenize("示例字符串如9.1.1.a、2.b.c，或x.y.z a1.bdsaf2.")
#     print(" ".join(t))