# -*- coding:utf-8 -*-


class Token(object):
    t_type = {
        "L_Parent": "(",
        "R_Parent": ")",
        "Integer": 0,
        "Plus": "+",
        "Minus": "-",
        "Multiply": "*",
        "Division": "/"
    }


class LexicalAnalyzer(Token):
    value = ""

    def __init__(self, value):
        self.value = value

    def get_slice_text(self):
        return_list = []
        sign_list = ['+', '-', '*', '/']
        parent_flag = False
        value_length = len(self.value)
        temp_value = ''

        def __append_temp(value):
            if value.replace(' ', '') != '':
                return_list.append(value)
                value = ''
            return value

        for x in xrange(value_length):
            if self.value[x] in sign_list:
                temp_value = __append_temp(temp_value)
                return_list.append(self.value[x])
            elif self.value[x] != '':
                if self.value[x] != '('and self.value[x] != ')':
                    temp_value += self.value[x]

            if self.value[x] == '(':
                parent_flag = True
                return_list.append(self.value[x])
            elif x+1 < value_length and self.value[x+1] == ')':
                parent_flag = False
                temp_value = __append_temp(temp_value)
                return_list.append(self.value[x+1])
        if self.value[value_length-1] != ')':
                temp_value = __append_temp(temp_value)
        return return_list

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
        for value in self.get_slice_text():
            return_list.append(self.get_token(value))
        return return_list


if __name__ == '__main__':
    text = "(10+20) - 30 + (1 + 2) * 30 / 47"
    analyzed = LexicalAnalyzer(text)
    results = analyzed.get_analyzed()
    for result in results:
        print "type: "+result['type']+", value: "+result['value']