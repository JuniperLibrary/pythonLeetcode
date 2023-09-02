from collections import Counter


def find_most_frequent_word(k, input_str):
    """
    有一个很长的英文单词串，里面全是小写字母，请你统计一下里面长度大于等于的单词一共出现了多少次，然后输出出现频率最高的那个单词。
    如果有多解，输出长度较小的那一个，如果长度相同，输出字典序较小的那一个
    I输入描述
    第一行一个整数k，如题中描述。

    第二行一个字符串str，只包含小写字母，长度不给出。
    k<= 50len(str) <= 100000
    输出描述
    一行一个字符串，表示满足长度大于等于且频率最高的字符串，无解输出-1.
    1示例1
    输入输出示例仅供调试，后台判题数据一般不包含示例
    输入


    2
    abababababa
    输出
    ab

    说明
    长度大于等于2旦频率最高的单词是ab和ba，但ab的字典序比ba小，因此输出是ab。
    :param k:
    :param input_str:
    :return:
    """
    word_count = Counter()

    # 枚举所有可能的长度大于等于k的子串
    for i in range(len(input_str) - k + 1):
        substring = input_str[i:i + k]
        word_count[substring] += 1

    # 找到频率最高的单词
    max_frequency = max(word_count.values())
    most_frequent_words = [word for word, freq in word_count.items() if freq == max_frequency]

    # 按照长度和字典序排序，选择第一个单词作为结果
    most_frequent_words.sort(key=lambda x: (len(x), x))

    if most_frequent_words:
        return most_frequent_words[0]
    else:
        return -1


# 读取输入
k = int(input())
input_str = input()

# 调用函数并输出结果
result = find_most_frequent_word(k, input_str)
print(result)

