#/bin/bash python3

global _global_dict
_global_dict = {}


def set_value(key, value):
    #定义一个全局变量
    
    # print(f"setting value: {key}: {str(value)}")
    _global_dict[key] = value


def get_value(key):
    #获得一个全局变量，不存在则提示读取对应变量失败
    try:
        print('读取'+key+'成功\r\n')
        return _global_dict[key]
    except:
        print('读取'+key+'失败\r\n')
        return None
