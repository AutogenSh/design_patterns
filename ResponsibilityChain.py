from abc import abstractmethod
from enum import IntEnum

"""
责任链模式

在这种模式中，通常每个接收者都包含对另一个接收者的引用。如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。

意图：避免请求发送者与接收者耦合在一起，让多个对象都有可能接收请求，将这些对象连接成一条链，并且沿着这条链传递请求，直到有对象处理它为止。

主要解决：职责链上的处理者负责处理请求，客户只需要将请求发送到职责链上即可，无须关心请求的处理细节和请求的传递，所以职责链将请求的发送者和请求的处理者解耦了。

何时使用：在处理消息的时候以过滤很多道。

"""


class LogLevel(IntEnum):
    ALL = 0
    TRACE = 1
    DEBUG = 2
    INFO = 3
    WARN = 4
    ERROR = 5
    FATAL = 6
    OFF = 7


class Logger:
    def __init__(self, level=LogLevel.DEBUG) -> None:
        super().__init__()
        self.level = level
        self.next_logger = None

    def set_next_Logger(self, logger):
        self.next_logger = logger

    def log(self, level, message):
        if self.level <= level:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log(level, message)

    @abstractmethod
    def write(self, message):
        pass


class ConsoleLogger(Logger):
    def __init__(self, level=LogLevel.DEBUG) -> None:
        super().__init__(level)

    def write(self, message):
        print('DEBUG Console::Logger:', message)


class ErrorLogger(Logger):
    def __init__(self, level=LogLevel.DEBUG) -> None:
        super().__init__(level)

    def write(self, message):
        print('ERROR Console::Logger:', message)


class FileLogger(Logger):
    def __init__(self, level=LogLevel.DEBUG) -> None:
        super().__init__(level)

    def write(self, message):
        print('INFO File::Logger:', message)


class LoggerFactory:
    __logger = None

    @staticmethod
    def logger():
        if LoggerFactory.__logger is None:
            LoggerFactory.__logger = ErrorLogger(LogLevel.ERROR)
            loggers = [ConsoleLogger(LogLevel.DEBUG), FileLogger(LogLevel.INFO)]

            prev = LoggerFactory.__logger
            for logger in loggers:
                prev.next_logger = logger
                prev = logger
        return LoggerFactory.__logger


if __name__ == '__main__':
    logger = LoggerFactory.logger()

    logger.log(LogLevel.INFO, 'This is an information.')
    print('===============================\n')
    logger.log(LogLevel.DEBUG, 'This is an debug level information.')
    print('===============================\n')
    logger.log(LogLevel.ERROR, 'This is an error information.')
