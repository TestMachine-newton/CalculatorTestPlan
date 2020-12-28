import pytest
from Calculator import Calculator
import yaml


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)

        add_datas = datas["data1"]
        sub_datas = datas["data2"]
        mul_datas = datas["data3"]
        div_datas = datas["data4"]
        return [add_datas,sub_datas,mul_datas,div_datas]

def setup_module():
    print("这个测试要开始咯")

def teardown_module():
    print("整个测试执行完毕")

class TestCalc:
    def setup_class(self):
        print("\n计算开始")
        self.calc = Calculator()


    def teardown_class(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a,b,expect", get_datas()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if result == expect:
            print("\n加法结果与期望值相等")
        else:
            print("\n加法结果与期望值不相等")
        assert result == expect


    @pytest.mark.parametrize("a,b,expect", get_datas()[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
