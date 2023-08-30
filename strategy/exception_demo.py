"""
在python中，异常处理是一种机制，用于在代码在执行过程中捕获和处理错误情况，以确保程序能够继续运行或适当地处理错误。

try:
    # 可能会引发异常的代码
    # ...
except ExceptionType1:
    # 处理特定类型的异常1
    # ...
except ExceptionType2:
    # 处理特定类型的异常2
    # ...
else:
    # 如果没有异常发生时执行的代码
    # ...
finally:
    # 无论是否有异常，都会执行的清理代码
    # ...

1.try：在这个块中放置可能引发异常的代码。如果异常发生，程序会跳转到对应的except块。
2.except：在这个块中放置处理特定类型异常的代码。你可以通过提供异常类型来指定要捕获的异常。如果不指定异常类型，它将捕获所有异常。可以有多个except块来处理不同类型的异常。
3.else：这个块中的代码在没有发生异常时执行。如果在try块中没有引发异常，那么将执行这个块中的代码。
4.finally：这个块中的代码无论是否有异常发生都会执行。通常用于执行清理操作，比如释放资源。


"""
import json

from lief import Object


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def divide(x, y) -> None:
    try:
        result = x / y
        if y == 13:
            raise CustomError("Unlucky number!")
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero.")
    except TypeError as e:
        raise ValueError(f"Invalid input: {e}")
    else:
        return result


def process_data(data):
    try:
        processed = []
        for item in data:
            try:
                result = divide(10, item)
            except CustomError as ce:
                result = str(ce)
            except ValueError as ve:
                result = str(ve)
            finally:
                processed.append(result)
    except Exception as e:
        print(f"An error occurred while processing data: {e}")
    else:
        print("Data processed successfully:", processed)


class exception_demo(Object):
    def demo(self) -> None:
        try:
            x = int(input("Enter a number: "))
            result = 10 / x
            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        else:
            print("No exception occurred.")
        finally:
            print("Execution complete.")


"""
在Python中，处理JSON是非常简单的，因为python内置了用于处理JSON的模块。主要用于JSON的处理的模块是'json'模块，它提供了将python对象转换为json格式字符串
以及将json格式字符串换回python对象的功能。

`json.dump(obj,indent=None)`：将python对象转换为JSON格式字符串。'obj'是要转换的python对象，'ident'参数是可选的，用于制定缩进的级别，使生成的JSON字符串更易读

`json.loads(json_string)`: 将JSON格式字符串解析为python对象。'json_string'是JSON格式的字符串

"""

data0 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


class json_obj(Object):
    def json_to_obj(self, data) -> None:
        loads = json.loads(data)
        print(loads)

    def obj_to_json(self, data):
        dumps = json.dumps(data, indent=4)
        print(dumps)


if __name__ == '__main__':
    # data = [5, 0, 2, '4', 10, 13]
    # print(process_data(data))
    print(json_obj().json_to_obj(data0))
    # print(json_obj().obj_to_json(Person("Jon", 30, "xian")))
