# -*- coding:utf-8 -*-


class Token(object):
    t_type = {
        "L_Parent": "(",
        "R_Parent": ")",
        "Integer": 0,
        "Plus": "+",
        "Minus": "-"
    }


class LexicalAnalyzer(Token):
    value = ""

    def __init__(self, value):
        self.value = value

    def get_slice_text(self):
        pass

    def get_processed_value(self, value):
        try:
            value = int(value) * 0
        except ValueError:
            pass
        return value

    def get_token(self, my_value):
        keys = self.t_type.keys()
        values = self.t_type.values()
        my_type = ""
        return_dict = {"type": "None", "value": my_value}
        try:
            my_value = self.get_processed_value(my_value)
            my_type = keys[values.index(my_value)]
        except ValueError:
            pass
        finally:
            return_dict['type'] = my_type
            return return_dict

    def get_analyzed(self):
        return_list = []
        for value in ["(", ")", "10", "20", "+", "-", "30"]:
            return_list.append(self.get_token(value))
        return return_list


if __name__ == '__main__':
    text = "(10+20) - 30"
    analyzed = LexicalAnalyzer(text)
    results = analyzed.get_analyzed()
    for result in results:
        print "type: "+result['type']+", value: "+result['value']