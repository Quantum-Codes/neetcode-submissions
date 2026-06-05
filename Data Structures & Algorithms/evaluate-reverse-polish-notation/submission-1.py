class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        soln = 0
        cur_tokens = []
        operators = ["*", "-", "+", "/"]

        for item in tokens:
            if not item in operators:
                cur_tokens.append(item)
                continue
            else:
                op_2 = int(cur_tokens.pop())
                op_1 = int(cur_tokens.pop())
                match item:
                    case "+": res = op_1 + op_2
                    case "-": res = op_1 - op_2
                    case "*": res = op_1 * op_2
                    case "/": res = op_1 / op_2

                cur_tokens.append(res)

        return int(cur_tokens.pop())
                
