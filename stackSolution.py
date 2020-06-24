from stacks import ArrayStack

# 괄호 유효성 검사
def validityOfParentheses(expr):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    S = ArrayStack()

    for c in expr:
        if c in '({[' :
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()


# 수가 문자열로 주어져 있을 때 (몇자리수인지 모르는상태) 
# 각각을 피연산자인 수와 연산자인 기호로 분리해서 리스트로 만드는 작업
# exprStr -> 중위 표현식으로된 수식
def splitTokens(exprStr):
    tokens = []
    val = 0                 # 각 자리 숫자를 담는 변수
    valProcessing = False   # 
    
    for c in exprStr:
        # 빈칸이 들어있으면 그냥 넘어감
        if c == ' ':
            continue
        
        # 숫자를 만나면 10진수로 변환하는 과정
        if c in '0123456789' :
            val = val * 10 + int(c)
            valProcessing = True # 수를 만났으므로 true
        
        # 숫자가 아니라면 (괄호 또는 연산자를 만났다고 간주) 10진수 표현이 끝난것
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            
            valProcessing = False # 지금 10진수를 처리하고있지 않다
            tokens.append(c)
        
    # 마지막 수 처리
    if valProcessing:
        tokens.append(val)
        
    return tokens



# 중위 표기법 -> 후위 표기법으로 바꾸는 함수
def infixToPostfix(tokenList):
    prec = {
        '*' : 3,
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1
    }
    
    opStack = ArrayStack()
    postfixList = []
    
    for token in tokenList:
        # 피연산자이면 리스트에 추가
        if type(token) is int:
            postfixList.append(token)
            
        # '('이면 스택에 push
        elif token == '(':
            opStack.push(token)
            
        # ')' 이면 '('가 나올때까지 pop
        elif token == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        
        # 연산자이면 +-*/
        else:
            # 스택이 비어있을 경우 스택에 push
            if opStack.isEmpty():
                opStack.push(token)
                
            # 스택이 비어있지 않다면 비교
            else:
                
                # 스택에 값이 존재할 동안에 반복
                while opStack.size() > 0:
                    # 우선 순위가 스택안에 있는게 높으면 꺼낸다
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                
                opStack.push(token)
    
    # 반복문을 다 돌고 스택이 빌때까지 pop
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    
    # 리스트로 리턴한다
    return postfixList


# 후위 표기법을 계산하는 함수
def postfixEval(tokenList):
    valStack = ArrayStack()
    
    for token in tokenList:
        # 피연산자를 만나면 스택에 push
        if type(token) is int:
            valStack.push(token)
            
        # 연산자를 만나면
        elif token == '+':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2+n1)
        
        elif token == '-':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2-n1)
            
        elif token == '*':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(n2*n1)
            
        elif token == '/':
            n1 = valStack.pop()
            n2 = valStack.pop()
            valStack.push(int(n2/n1))
        
    return valStack.pop()



def solution(expr):
    # 중위표현식을 tokens의 리스트 형태로 변환(피연산자, 연산자, 괄호)
    tokens = splitTokens(expr)
    # 리스트 형태로 저장된 토큰을 순서대로 후위표현식으로 변환
    postfix = infixToPostfix(tokens)
    # 후위표현식을 계산
    val = postfixEval(postfix)
    
    return val


expr = "10/2"
tokens = splitTokens(expr)
postfix = infixToPostfix(tokens)
val = postfixEval(postfix)

print(tokens)
print(postfix)
print(val)