import random
from fractions import Fraction
import os
questions = []      #用来盛放问题的列表
answers = []        #用来盛放答案的列表

def add(a, b):      #加法
    return a + b

def minus(a, b):    #减法
    return a - b

def multiply(a, b): #乘法
    return a * b

def divide(a, b):   #除法
    return Fraction(a, b)


def operation_one(a, b, op):                    #一个运算符的题目
    if op == 1:
        questions.append(str(a)+'+'+str(b)+'=?')
        answers.append(str(add(a,b)))
    elif op == 2:
        questions.append(str(a)+'-'+str(b)+'=?')
        answers.append(str(minus(a,b)))
    elif op == 3:
        questions.append(str(a)+'*'+str(b)+'=?')
        answers.append(str(multiply(a,b)))
    else :
        questions.append(str(a)+'/'+str(b)+'=?')
        answers.append(str(divide(a,b)))

    return questions,answers

def operation_two(a, b, c, op1, op2):           #两个运算符的题目
        if op1 == 1:
            if op2 == 1:
                questions.append(str(a)+'+'+str(b)+'+'+str(c)+'=?')
                answers.append(str(add(add(a,b),c)))
            elif op2 == 2:
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'=?')
                answers.append(str(minus(add(a,b),c)))
            elif op2 == 3:
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'=?')
                answers.append(str(add(a,multiply(b, c))))
            else :
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'=?')
                answers.append(str(add(a,divide(b, c))))
        elif op1 == 2:
            if op2 == 1:
                questions.append(str(a)+'-'+str(b)+'+'+str(c)+'=?')
                answers.append(str(add(minus(a,b),c)))
            elif op2 == 2:
                questions.append(str(a)+'-'+str(b)+'-'+str(c)+'=?')
                answers.append(str(minus(minus(a,b),c)))
            elif op2 == 3:
                questions.append(str(a)+'-'+str(b)+'*'+str(c)+'=?')
                answers.append(str(minus(a,multiply(b, c))))
            else :
                questions.append(str(a)+'-'+str(b)+'/'+str(c)+'=?')
                answers.append(str(minus(a,divide(b, c))))
        elif op1 == 3:
            if op2 == 1:
                questions.append(str(a)+'*'+str(b)+'+'+str(c)+'=?')
                answers.append(str(add(multiply(a,b),c)))
            elif op2 == 2:
                questions.append(str(a)+'*'+str(b)+'-'+str(c)+'=?')
                answers.append(str(minus(multiply(a,b),c)))
            elif op2 == 3:
                questions.append(str(a)+'*'+str(b)+'*'+str(c)+'=?')
                answers.append(str(multiply(a,multiply(b, c))))
            else :
                questions.append(str(a)+'*'+str(b)+'/'+str(c)+'=?')
                answers.append(str(multiply(a,divide(b, c))))
        else :
            if op2 == 1:
                questions.append(str(a)+'/'+str(b)+'+'+str(c)+'=?')
                answers.append(str(add(divide(a,b),c)))
            elif op2 == 2:
                questions.append(str(a)+'/'+str(b)+'-'+str(c)+'=?')
                answers.append(str(minus(divide(a,b),c)))
            elif op2 == 3:
                questions.append(str(a)+'/'+str(b)+'*'+str(c)+'=?')
                answers.append(str(multiply(divide(a,b),c)))
            else :
                questions.append(str(a)+'/'+str(b)+'/'+str(c)+'=?')
                answers.append(str(divide(divide(a,b),c)))
        return questions,answers

def operation_three(a, b, c, d, op1, op2, op3): #三个运算符的题目
    if op1 == 1:
        if op2 == 1:
            if op3 == 1:
                questions.append(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(add(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=?')
                answers.append(str(minus(add(add(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(multiply(c,d),b),a)))
            else :
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(divide(c,d),b),a)))
        elif op2 == 2:
            if op3 == 1:
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(add(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(add(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'*'+str(d)+'=?')
                answers.append(str(add(minus(b,multiply(c,d)),a)))
            else :
                questions.append(str(a)+'+'+str(b)+'-'+str(c)+'/'+str(d)+'=?')
                answers.append(str(add(minus(b,divide(c,d)),a)))
        elif op2 == 3:
            if op3 == 1:
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(multiply(b,c),a),d)))
            elif op3 == 2:
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(add(multiply(b,c),a),d)))
            elif op3 == 3:
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'*'+str(d)+'=?')
                answers.append(str(add(multiply(b,multiply(c,d)),a)))
            else :
                questions.append(str(a)+'+'+str(b)+'*'+str(c)+'/'+str(d)+'=?')
                answers.append(str(add(multiply(b,divide(c,d)),a)))
        else :
            if op3 == 1:
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(divide(b,c),a),d)))
            elif op3 == 2:
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(add(divide(b,c),a),d)))
            elif op3 == 3:
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'*'+str(d)+'=?')
                answers.append(str(add(divide(b,multiply(c,d)),a)))
            else :
                questions.append(str(a)+'+'+str(b)+'/'+str(c)+'/'+str(d)+'=?')
                answers.append(str(add(divide(b,divide(c,d)),a)))
    elif op1 == 2:
        if op2 == 1:
            if op3 == 1:
                questions.append(str(a)+'-'+str(b)+'+'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(minus(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'-'+str(b)+'+'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(add(minus(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'-'+str(b)+'+'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(add(multiply(c,d),a),b)))
            else :
                questions.append(str(a)+'-'+str(b)+'+'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(add(divide(c,d),a),b)))
        elif op2 == 2:
            if op3 == 1:
                questions.append(str(a)+'-'+str(b)+'-'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(minus(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'-'+str(b)+'-'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(minus(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'-'+str(b)+'-'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(a,minus(b,multiply(c,d)))))
            else :
                questions.append(str(a)+'-'+str(b)+'-'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(a,minus(b,divide(c,d)))))
        elif op2 == 3:
            if op3 == 1:
                questions.append(str(a)+'-'+str(b)+'*'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(a,multiply(b,c)),d)))
            elif op3 == 2:
                questions.append(str(a)+'-'+str(b)+'*'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(a,multiply(b,c)),d)))
            elif op3 == 3:
                questions.append(str(a)+'-'+str(b)+'*'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(a,multiply(b,multiply(c,d)))))
            else :
                questions.append(str(a)+'-'+str(b)+'*'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(a,multiply(b,divide(c,d)))))
        else :
            if op3 == 1:
                questions.append(str(a)+'-'+str(b)+'/'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(a,divide(b,c)),d)))
            elif op3 == 2:
                questions.append(str(a)+'-'+str(b)+'/'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(a,divide(b,c)),d)))
            elif op3 == 3:
                questions.append(str(a)+'-'+str(b)+'/'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(a,divide(divide(b,c),d))))
            else :
                questions.append(str(a)+'-'+str(b)+'/'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(a,divide(divide(b,c),d))))
    elif op1 == 3:
        if op2 == 1:
            if op3 == 1:
                questions.append(str(a)+'*'+str(b)+'+'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(multiply(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'*'+str(b)+'+'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(add(multiply(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'*'+str(b)+'+'+str(c)+'*'+str(d)+'=?')
                answers.append(str(add(multiply(a,b),multiply(c,d))))
            else :
                questions.append(str(a)+'*'+str(b)+'+'+str(c)+'/'+str(d)+'=?')
                answers.append(str(add(multiply(a,b),divide(c,d))))
        elif op2 == 2:
            if op3 == 1:
                questions.append(str(a)+'*'+str(b)+'-'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(multiply(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'*'+str(b)+'-'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(multiply(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'*'+str(b)+'-'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(multiply(a,b),multiply(c,d))))
            else :
                questions.append(str(a)+'*'+str(b)+'-'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(multiply(a,b),divide(c,d))))
        elif op2 == 3:
            if op3 == 1:
                questions.append(str(a)+'*'+str(b)+'*'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(multiply(a,multiply(b,c)),d)))
            elif op3 == 2:
                questions.append(str(a)+'*'+str(b)+'*'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(multiply(a,multiply(b,c)),d)))
            elif op3 == 3:
                questions.append(str(a)+'*'+str(b)+'*'+str(c)+'*'+str(d)+'=?')
                answers.append(str(multiply(a,multiply(b,multiply(c,d)))))
            else :
                questions.append(str(a)+'*'+str(b)+'*'+str(c)+'/'+str(d)+'=?')
                answers.append(str(divide(multiply(multiply(a,b),c),d)))
        else :
            if op3 == 1:
                questions.append(str(a)+'*'+str(b)+'/'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(divide(multiply(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'*'+str(b)+'/'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(divide(multiply(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'*'+str(b)+'/'+str(c)+'*'+str(d)+'=?')
                answers.append(str(multiply(divide(multiply(a,b),c),d)))
            else :
                questions.append(str(a)+'*'+str(b)+'/'+str(c)+'/'+str(d)+'=?')
                answers.append(str(divide(divide(multiply(a,b),c),d)))
    else :
        if op2 == 1:
            if op3 == 1:
                questions.append(str(a)+'/'+str(b)+'+'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(add(divide(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'/'+str(b)+'+'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(add(divide(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'/'+str(b)+'+'+str(c)+'*'+str(d)+'=?')
                answers.append(str(add(divide(a,b),multiply(c,d))))
            else :
                questions.append(str(a)+'/'+str(b)+'+'+str(c)+'/'+str(d)+'=?')
                answers.append(str(add(divide(a,b),divide(c,d))))
        elif op2 == 2:
            if op3 == 1:
                questions.append(str(a)+'/'+str(b)+'-'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(minus(divide(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'/'+str(b)+'-'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(minus(divide(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'/'+str(b)+'-'+str(c)+'*'+str(d)+'=?')
                answers.append(str(minus(divide(a,b),multiply(c,d))))
            else :
                questions.append(str(a)+'/'+str(b)+'-'+str(c)+'/'+str(d)+'=?')
                answers.append(str(minus(divide(a,b),divide(c,d))))
        elif op2 == 3:
            if op3 == 1:
                questions.append(str(a)+'/'+str(b)+'*'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(multiply(divide(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'/'+str(b)+'*'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(multiply(divide(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'/'+str(b)+'*'+str(c)+'*'+str(d)+'=?')
                answers.append(str(multiply(multiply(divide(a,b),c),d)))
            else :
                questions.append(str(a)+'/'+str(b)+'*'+str(c)+'/'+str(d)+'=?')
                answers.append(str(divide(multiply(divide(a,b),c),d)))
        else :
            if op3 == 1:
                questions.append(str(a)+'/'+str(b)+'/'+str(c)+'+'+str(d)+'=?')
                answers.append(str(add(divide(divide(a,b),c),d)))
            elif op3 == 2:
                questions.append(str(a)+'/'+str(b)+'/'+str(c)+'-'+str(d)+'=?')
                answers.append(str(minus(divide(divide(a,b),c),d)))
            elif op3 == 3:
                questions.append(str(a)+'/'+str(b)+'/'+str(c)+'*'+str(d)+'=?')
                answers.append(str(multiply(divide(divide(a,b),c),d)))
            else :
                questions.append(str(a)+'/'+str(b)+'/'+str(c)+'/'+str(d)+'=?')
                answers.append(str(divide(divide(divide(a,b),c),d)))
        return questions,answers
    
def write_in(questions,answers):                #将题目和答案分别写入文件
    for i,question in enumerate(questions):
        f1 = open('questions.txt','a')
        f1.write("第"+str(i+1)+"题:")
        f1.write(question)
        f1.write('\n')
        f1.close()
    for i,answer in enumerate(answers):
        f2 = open('answers.txt','a')
        f2.write("第"+str(i+1)+"题答案:")
        f2.write(answer)
        f2.write('\n')
        f2.close()
        


def main():
    for i in range(0,10000):
        a = random.randint(1,9)
        b = random.randint(1,9)
        c = random.randint(1,9)
        d = random.randint(1,9)
        op_count = random.randint(1,3)  #通过随机的op_count控制运算符个数
        op1 = random.randint(1,4)       #第一个运算符
        op2 = random.randint(1,4)       #第二个运算符
        op3 = random.randint(1,4)       #第三个运算符
        if op_count == 1:       
            contents = operation_one(a, b, op1)
        elif op_count == 2:
            operation_two(a, b, c, op1, op2)
        else :
            operation_three(a, b, c, d, op1, op2, op3)
    write_in(contents[0],contents[1])

if __name__ == "__main__":
    main()