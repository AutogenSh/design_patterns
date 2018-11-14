from abc import abstractmethod

"""
解释器模式
解释器模式（Interpreter Pattern）提供了评估语言的语法或表达式的方式，它属于行为型模式。
这种模式实现了一个表达式接口，该接口解释一个特定的上下文。
这种模式被用在 SQL 解析、符号处理引擎等。

意图：
给定一个语言，定义它的文法表示，并定义一个解释器，这个解释器使用该标识来解释语言中的句子。

主要解决：
对于一些固定文法构建一个解释句子的解释器。

何时使用：
如果一种特定类型的问题发生的频率足够高，那么可能就值得将该问题的各个实例表述为一个简单语言中的句子。
这样就可以构建一个解释器，该解释器通过解释这些句子来解决该问题。

如何解决：
构件语法树，定义终结符与非终结符。
"""


class Expression:
    @abstractmethod
    def interpret(self, context) -> bool:
        pass


class TerminalExpression(Expression):
    def __init__(self, data: str) -> None:
        self.data = data

    def interpret(self, context: str) -> bool:
        if self.data in context:
            return True
        return False


class OrExpression(Expression):
    def __init__(self, expr1, expr2) -> None:
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context) -> bool:
        return self.expr1.interpret(context) or self.expr2.interpret(context)


class AndExpression(Expression):
    def __init__(self, expr1, expr2) -> None:
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)

def isMale():
    robert = TerminalExpression('Robert')
    john = TerminalExpression('John')
    return OrExpression(robert, john)

def isMarriedWoman():
    julie = TerminalExpression('Julie')
    married = TerminalExpression('Married')
    return AndExpression(julie, married)

if __name__ == '__main__':
    isMale = isMale()
    isMarriedWoman = isMarriedWoman()
    print('John is male? %s' % isMale.interpret('John'))
    print('Julie is a married women? %s' % isMarriedWoman.interpret('Married Julie'))