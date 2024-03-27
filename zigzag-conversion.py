class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        output = [
            [
                None for _ in range(0, len(s))
            ] for _ in range(0, numRows)
        ]

        col = -1
        for d in range(0, len(s)):
            dd = d % (numRows * 2 - 2)

            if dd < numRows:
                if dd == 0:
                    col += 1
                row = dd
                output[row][col] = s[d]
            else:
                col += 1
                row = (numRows - 1) - dd % (numRows - 1)
                output[row][col] = s[d]

        s = ''
        for row in output:
            for c in row:
                if c is not None:
                    s += c

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
