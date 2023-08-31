"""
set.up  打包和发布管理
requirements.txt  开发依赖.


装饰器

装饰器就是一个函数或类。他可以包装（或装饰）一个函数或方法。被装饰的函数或方法会替换原来的函数或方法
"""
from datetime import datetime


class MetaReadOnly(type):
    def __setattr__(cls, name, val):
        raise AttributeError(f"{cls.__name__}.{name} is readonly.")


class MetaEnumContainer(type):

    def __new__(mcs, name, bases, attrs):
        _enum = {}
        for k, v in attrs.items():
            if not k.startswith('_'):
                _enum[v] = k
        attrs['__enum'] = _enum
        _cls = super().__new__(mcs, name, bases, attrs)
        return _cls

    def __setattr__(cls, name, val):
        raise AttributeError(f"{cls.__name__}.{name} is readonly.")

    def __call__(cls, value):
        return getattr(cls, "__enum", {}).get(value, None)

    def __contains__(cls, item):
        return item in getattr(cls, "__enum")


class EnumContainer(metaclass=MetaEnumContainer):
    """
    枚举容器类
    usage:
            class Seq(EnumContainer):
                FIRST = 0
                SECOND = 1
            0 in Seq is True
            2 in Seq is False
            0 == Seq.FIRST
            Seq.THIRD = 3 will raise AttributeError
            Seq(1) -> return FIRST
    """


class Source(EnumContainer):
    """
    行情及下单渠道
    """
    UNKNOWN = "UNKNOWN"
    XBOND = "XBOND"
    QB = "QB"
    CFETS = "CFETS"
    ESP = "ESP"
    AGG = "AGG"
    RT = "RT"
    URT = "URT"
    XSWAP = "XSWAP"  # XSWAP融合行情
    CFFEX = "CFFEX"
    SBF = "SBF"
    EXECUTOR_ESP = "FIESP"  # 执行端用的ESP名称


class func:
    @staticmethod
    def check_param(count=None, begin_time=None, end_time=None, method=None, source=None):
        if count is not None and count < 1:
            print(f'{method} count数量错误，count数量应大于0')
            raise print(f'{method} count数量错误，count数量应大于0')
        # if begin_time is not None:
        #     if not self.is_valid_date(begin_time):
        #         print(f'{method} 时间格式错误，请按照yyyy-MM-dd HH:mm:ss传参')
        #         raise print(f'{method} 时间格式错误，请按照yyyy-MM-dd HH:mm:ss传参')
        #
        # if end_time is not None:
        #     if not is_valid_date(end_time):
        #         print(f'{method} 时间格式错误，请按照yyyy-MM-dd HH:mm:ss传参')
        #         print(f'{method} 时间格式错误，请按照yyyy-MM-dd HH:mm:ss传参')
        # if end_time is not None and begin_time is not None:
        #     start = datetime.datetime.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
        #     end = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        #     if start > end:
        #         print(f'{method} 时间范围错误，开始时间应小于截止时间')
        #         raise print(f'{method} 时间范围错误，开始时间应小于截止时间')
        if source is not None and source not in Source:
            print(f'{method} source不存在，请重新选择')
            raise print(f'{method} source不存在，请重新选择')

    @staticmethod
    def printinfo(arg1, *vartuple):
        """打印任何传入的参数"""
        """
        不定长参数
        你可能需要一个函数处理比当初生命时更多的参数。这些参数叫做不定长参数
        
        * 的参数会以元祖(tuple)的形式导入，存放所有未命名的参数
        ** 的参数会以字典的形式导入
        
        """
        print("输出：")
        print(arg1)
        print(vartuple)

    def f(a, b, *, c):
        return a + b + c

    # f(1,2,3) error
    # f(1,2,c=3) error
    # 如果单独出现 * ,则 * 后面的参数必须用关键字传入

    """
    匿名函数
    Python使用lambda来创建函数。所谓匿名，不再使用def这样的标准来定义函数
    
    lambda [arg1 [,arg2,.....argn]]:expression    
    """


if __name__ == '__main__':
    # 推导式
    """
    [out_exp_res for out_exp in input_list]
    或者
    [表达式 for 变量 in 列表 if 条件]
    """
    # print(func.check_param(count=2, end_time=datetime, begin_time=datetime, source=Source.QB))
    x = lambda a: a + 10
    print(x(5))
