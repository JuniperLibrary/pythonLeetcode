class Solution:
    def canBeEqual(s1, s2):
        if s1 == s2:
            return True

        n = len(s1)

        if n != len(s2):
            return False

        positions_s1 = {}
        positions_s2 = {}

        for i in range(n):
            if s1[i] in positions_s1:
                positions_s1[s1[i]].append(i)
            else:
                positions_s1[s1[i]] = [i]

            if s2[i] in positions_s2:
                positions_s2[s2[i]].append(i)
            else:
                positions_s2[s2[i]] = [i]

        for char, pos_list in positions_s1.items():
            if char in positions_s2:
                if sorted(pos_list) == sorted(positions_s2[char]):
                    continue
                elif sorted(pos_list) == [pos_list[0], pos_list[0] + 1, pos_list[0] + 2, pos_list[0] + 3]:
                    return True

        return False

    def canBeEqual1(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1 = list(s1)
        s2 = list(s2)

        for i in range(3):
            if s1[i] != s2[i]:
                for j in range(i + 1, 4):
                    if s1[j] == s1[i]:
                        s1[j], s1[i] = s1[i], s1[j]
                        break
                else:
                    return False

        return True


if __name__ == '__main__':
    print(Solution().canBeEqual1("abcd", "dacb"))
