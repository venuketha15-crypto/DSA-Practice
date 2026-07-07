class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:

            if ch != "]":
                stack.append(ch)

            else:

                string = ""

                while stack[-1] != "[":
                    string = stack.pop() + string

                stack.pop()

                number = ""

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(int(number) * string)

        return "".join(stack)
