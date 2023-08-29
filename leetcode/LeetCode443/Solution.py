from typing import List


class Solution:
    @staticmethod
    def compress_test(chars) -> int:
        write_idx = 0
        start = 0
        for i in range(len(chars)):
            #  检查当前字符是否与下一个字符相同
            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                chars[write_idx] = chars[start]
                write_idx += 1
            # 如果组长度大于 1 将长度数字转换为字符串并写入数组
            if i > start:
                count_str = str(i - start + 1)
                for digit in count_str:
                    chars[write_idx] = digit
                    write_idx += 1
            # 更新下一个字符的起始索引
            start = i + 1
        return write_idx

    def compress(self, chars: List[str]) -> int:
        """
        443. 压缩字符串
        给你一个字符数组 chars ，请使用下述算法压缩：
        1. 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
        2. 如果这一组长度为 1 ，则将字符追加到 s 中。
        3. 否则，需要向 s 追加字符，后跟这一组的长度。
        压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。
        请在 修改完输入数组后 ，返回该数组的新长度。
        你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

        输入：chars = ["a","a","b","b","c","c","c"]
        输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
        解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
        """
        # 初始化压缩后字符数组的写入指针
        write_idx = 0
        # 初始化当前遍历字符的起始索引
        start = 0
        # 初始化一个字典来记录字符出现的次数
        char_count = {}

        # 遍历原始字符数组
        for i in range(len(chars)):
            char = chars[i]
            char_count[char] = char_count.get(char, 0) + 1

            # 检查当前字符是否与下一个字符不同
            if i == len(chars) - 1 or char != chars[i + 1]:
                # 将当前字符写入压缩后的字符数组
                chars[write_idx] = char
                write_idx += 1

                # 如果数组长度大于1 ，将长度数字转换为字符串并写入数组
                if char_count[char] > 1:
                    s = str(char_count[char])
                    for digit in s:
                        chars[write_idx] = digit
                        write_idx += 1

                # 更新下一个字符的起始索引
                start = i + 1
                # 清空字符计数
                char_count = {}
        # 返回压缩后的字符数组的长度
        return write_idx


if __name__ == '__main__':
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
