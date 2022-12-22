import re
from math import log, exp, sqrt, factorial


def process_pair_with_percent(pair):
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    first_operand_patt_percent = r'^([+-]?\d+\.?\d*|\.\d+)%?'
    second_operand_patt_percent = r'(\d+\.?\d*|\.\d+)%?$'
    sign_patt = r'[\+\-\/\*]'
    first_operand_percent = re.search(first_operand_patt_percent, pair).group()
    first_operand = re.search(first_operand_patt, pair).group()
    sign = re.search(sign_patt, pair).group()
    pair = pair.replace(first_operand_percent, "", 1)
    second_operand_percent = re.search(second_operand_patt_percent, pair).group()
    second_operand = re.search(second_operand_patt, pair).group()

    if "%" in second_operand_percent and not("%" in first_operand_percent):
        if sign == "+":
            return float(first_operand) + float(first_operand) * (float(second_operand) / 100)
        if sign == "-":
            return float(first_operand) - float(first_operand) * (float(second_operand) / 100)
        if sign == "*":
            return float(first_operand) * (float(second_operand) / 100)
        if sign == "/":
            return float(first_operand) / (float(second_operand) / 100)

    if "%" in first_operand_percent and not("%" in second_operand_percent):
        if sign == "+":
            return (float(first_operand) / 100) + float(second_operand) 
        if sign == "-":
            return (float(first_operand) / 100) - float(second_operand)
        if sign == "*":
            return (float(first_operand) / 100) * float(second_operand)
        if sign == "/":
            return (float(first_operand) / 100) / float(second_operand)

    if "%" in first_operand_percent and "%" in second_operand_percent:
        if sign == "+":
            return (float(first_operand) / 100) +  (float(first_operand) / 100) * (float(second_operand) / 100)
        if sign == "-":
            return (float(first_operand) / 100) -  (float(first_operand) / 100) * (float(second_operand) / 100)
        if sign == "*":
            return (float(first_operand) / 100) *  (float(second_operand) / 100)
        if sign == "/":
            return float(first_operand) / float(second_operand)

def process_pair_with_power(pair):
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    first_operand = re.search(first_operand_patt, pair).group()
    pair = pair.replace(first_operand, "", 1)
    second_operand = re.search(second_operand_patt, pair).group()
    operands = [first_operand, second_operand]

    return float(operands[0]) ** float(operands[1])

def process_pair_with_root(pair):
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    first_operand = re.search(first_operand_patt, pair).group()
    pair = pair.replace(first_operand, "", 1)
    second_operand = re.search(second_operand_patt, pair).group()
    operands = [first_operand, second_operand]
    if float(operands[0]) == 2:
        return sqrt(float(operands[1]))
    return exp(log(float(operands[1])) / float(operands[0]))

def process_pair_with_fact(text):
    operand_patt = r'\d+\.?\d*\!+|\.\d+\!+'
    operand = re.search(operand_patt, text).group()[:-1]
    return factorial(float(operand))
    
def process_pair_with_brack(text):
    brack_patt = r'\(.*\)'
    brack_construction = re.search(brack_patt, text).group()[1:-1]
    return brack_construction

def process_pair_with_div(text):
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    div_patt = r'[+-]?((\d+\.?\d*)|(\.\d+))%?\!?[\/][+-]?((\d+\.?\d*)|(\.\d+))%?\!?'
    div = re.search(div_patt, text).group()
    first_operand = re.search(first_operand_patt, div).group()
    div = div.replace(first_operand, "", 1)
    second_operand = re.search(second_operand_patt, div).group()
    try:
        return float(first_operand) / float(second_operand)
    except ZeroDivisionError:
        return "I can't divide by zero, sorry."

def process_pair_with_mult(text):
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    div_patt = r'[+-]?((\d+\.?\d*)|(\.\d+))%?\!?[\*][+-]?((\d+\.?\d*)|(\.\d+))%?\!?'
    mult = re.search(div_patt, text).group()
    first_operand = re.search(first_operand_patt, mult).group()
    mult = mult.replace(first_operand, "", 1)
    second_operand = re.search(second_operand_patt, mult).group()

    return float(first_operand) * float(second_operand)
    

    


def process_str(text):
    pair_patt = r'[+-]?((\d+\.?\d*)|(\.\d+))%?\!?[\+\-\/\*\^√][+-]?((\d+\.?\d*)|(\.\d+))%?\!?'
    once_factorial_patt = r'\d+\.?\d*\!+|\.\d+\!+'
    brack_patt = r'\(.*\)'
    div_patt = r'((\d+\.?\d*)|(\.\d+))%?\!?[\/][+-]?((\d+\.?\d*)|(\.\d+))%?\!?'
    mult_patt = r'((\d+\.?\d*)|(\.\d+))%?\!?[\*][+-]?((\d+\.?\d*)|(\.\d+))%?\!?'
    first_operand_patt = r'^[+-]?\d+\.?\d*|\.\d+'
    second_operand_patt = r'\d+\.?\d*|\.\d+$'
    sign_patt = r'[\+\-\/\*]'
    dot_zero_patt = r'\.0$'

    if re.search(brack_patt, text):
        brack_construction = re.search(brack_patt, text).group()
        result = str(process_pair_with_brack(text))
        if(re.search(dot_zero_patt, result)):
            result = result.replace(".0", "")
        text = text.replace(brack_construction, process_str(result))
        return process_str(text)
    
    if re.search(div_patt, text):
        div = re.search(div_patt, text).group()
        result = str(process_pair_with_div(text))
        if(re.search(dot_zero_patt, result)):
            result = result.replace(".0", "")
        text = text.replace(div, process_str(result))
        return process_str(text)
    
    if re.search(mult_patt, text):
        mult = re.search(mult_patt, text).group()
        result = str(process_pair_with_mult(text))
        if(re.search(dot_zero_patt, result)):
            result = result.replace(".0", "")
        text = text.replace(mult, process_str(result))
        return process_str(text)

    if re.search(once_factorial_patt, text):
        fact_operand = re.search(once_factorial_patt, text).group()
        result = str(process_pair_with_fact(text))
        if(re.search(dot_zero_patt, result)):
            result = result.replace(".0", "")
        text = text.replace(fact_operand, result)
        return process_str(text)

    if not re.search(pair_patt, text):
        return text
    else:
        pair = re.search(pair_patt, text).group()
        if "!" in pair:
            result = str(process_pair_with_fact(pair))
            if(re.search(dot_zero_patt, result)):
                result = result.replace(".0", "")
            text = text.replace(pair, "")
            text = result+text
            return process_str(text)
        if "%" in pair:
            result = str(process_pair_with_percent(pair))
            if(re.search(dot_zero_patt, result)):
                result = result.replace(".0", "")
            text = text.replace(pair, "")
            text = result+text
            return process_str(text)
        if "^" in pair:
            result = str(process_pair_with_power(pair))
            if(re.search(dot_zero_patt, result)):
                result = result.replace(".0", "")
            text = text.replace(pair, "")
            text = result+text
            return process_str(text)
        if "√" in pair:
            result = str(process_pair_with_root(pair))
            if(re.search(dot_zero_patt, result)):
                result = result.replace(".0", "")
            text = text.replace(pair, "")
            text = result+text
            return process_str(text)

        text = text.replace(pair, "") 
        operands = [re.search(first_operand_patt, pair).group(), re.search(second_operand_patt, pair).group()]
        first_operand = re.search(first_operand_patt, pair).group()
        pair = pair.replace(first_operand, "", 1)
        second_operand = re.search(second_operand_patt, pair).group()
        operands = [first_operand, second_operand]

        sign = re.search(sign_patt, pair).group()
        text = text.replace(pair, "")
        
        if sign == '+':
            result = float(operands[0]) + float(operands[1])
        if sign == '-':
            result = float(operands[0]) - float(operands[1])
        if sign == '/':
            result = float(operands[0]) / float(operands[1])
        if sign == '*':
            result = float(operands[0]) * float(operands[1])
        result = str(result)

        if(re.search(dot_zero_patt, result)):
            result = result.replace(".0", "")
        
        text = result+text
        return process_str(text)












