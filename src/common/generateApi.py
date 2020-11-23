import os

import read_config


class MyTools:
    @staticmethod
    def MakeClass(className, filepath, p=[]):
        """
            自动生成类和getter setter
        :param className: 类名字符串
        :param filepath: 路径字符串，最好绝对路径
        :param p: 类中的属性列表
        :return:
        """
        lines = [
            "from src.api.baseApi import BaseApi\n\n"
            "\nclass {0}(BaseApi)".format(className) + ":",
            "\tdef __init__(self):"
        ]
        lines += ["\t\tsuper().__init__()"]
        lines += ["\t\tself.__{0} = None".format(param) for param in p]
        lines += ["\t\tpass", ""]

        for param in p:
            methodLines = []
            methodLines.append("\t@property")
            methodLines.append("\tdef {0}(self):".format(param))
            methodLines.append("\t\treturn self.__{0}".format(param))
            methodLines.append("")
            methodLines.append("\t@{0}.setter".format(param))
            methodLines.append("\tdef {0}(self, value):".format(param))
            methodLines.append("\t\tself.__{0} = value".format(param))
            methodLines.append("")
            lines += methodLines
            pass
        lines.append("\tdef toDict(self):")
        lines.append('\t\tdict1 = {')
        lines += ['\t\t\t{0}: {1},'.format("'" + p1 + "'", 'self.__' + p2) for p1, p2 in zip(p, p)]
        lines.append('\t\t\t}\n\t\treturn dict1\n\tpass')
        print(lines)
        lines = [i + "\n" for i in lines]
        with open(filepath, "a+", encoding="utf-8") as fp:
            fp.writelines(lines)
            print("类{0}生成成功".format(className))
            pass
        pass

    pass


if __name__ == '__main__':
    path = read_config.get_path()
    api_dir = os.path.join(path, 'src', 'interface', 'api', 'testApi.py')
    MyTools.MakeClass("TestGen", api_dir, p=["code", "msg"])
