from main.interface.test.TestInterface import TestInterface
from main.interface.test.raise_funds_interface import RaiseFundsInterface
from main.support.http.HttpExecutor import HttpExecutor

if __name__ == '__main__':
    print(HttpExecutor.executor(TestInterface()))
    print(HttpExecutor.executor(RaiseFundsInterface()))
