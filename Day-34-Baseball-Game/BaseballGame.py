class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:

            if i.lstrip("-").isdigit():
                stack.append(int(i))

            elif i == "+":
                stack.append(stack[-1] + stack[-2])

            elif i == "C":
                stack.pop()

            else:      # D
                stack.append(2 * stack[-1])

        return sum(stack)
