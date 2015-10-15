# (\x(\y xy))y
# ["app",["lam","x",["lam","y",["var","xy"]]],["var","y"]]

def replacement(exp, count):
    return ["var", str(count)]


def replace_all(exp, a):
    # exp = ["xy"]
    # a = {'x' : 1, 'y' : 2}
    for r in a:
        exp = exp.replace(r, str(a[r]))
    return exp


def rename(exp, a={}, count=0):
    if exp[0] == "var":
        return ["var", replace_all(exp[1], a)]
    elif exp[0] == "lam":
        count += 1
        a[exp[1]] = count
        return ["lam", str(count), rename(exp[2], a, count)]
    else: # app
        return ["app", rename(exp[1]), replacement(exp[2], count)]

#print rename(["app",["lam","x",["lam","y",["var","xy"]]],["var","y"]])
#print rename(["app",["lam","a",["app",["var","a"],["var","a"]]],["lam","b",["lam","c",["var","c"]]]])



#  \b (\c c)(a))d
# ["app",["lam","a",["lam","b",["app",["lam","c",["var","c"]],["var","a"]]]],["var","d"]] 

def sub(l, x, a):
    # l = ["lam","a",["lam","b",["app",["lam","c",["var","c"]],["var","a"]]]]
    # a = ["var","d"]
    print 'l=',l 
    if l[0] == "var" or l[0] == "app":
        return l
    elif l[2][0] == "var":
        if l[1] == x:
            l[2] = a
        return l
    else:
        # move on
        l = l[2]
        x = l[1]
        return sub(l, x, a)


def weak_normal_form(exp):
    if exp[0] == "var":
        return exp
    elif exp[0] == "lam":
        return exp
    else:
        a = exp[2]
        l = exp[1]
        exp = sub(l, '', a)
        return weak_normal_form(exp)

#print weak_normal_form(["app",["lam","x",["lam","y",["var","x"]]],["lam","x",["lam","y",["var","y"]]]])
#print weak_normal_form(["app",["lam","a",["lam","b",["app",["lam","c",["var","c"]],["var","a"]]]],["var","d"]])
#print weak_normal_form(["lam","b",["app",["lam","c",["var","c"]],["var","d"]]])

#print weak_normal_form(["app",["lam","c",["var","c"]],["var","d"]])


def normal_form(exp):
   # ["lam","b",["app",["lam","c",["var","c"]],["var","d"]]] 
    if exp[0] == "var":
        return exp
    elif exp[0] == "lam":
        return ["lam", exp[1], normal_form(exp[2])]
    else: # app
        # ["app",["lam","c",["var","c"]],["var","d"]]
        exp = weak_normal_form(exp)
        return normal_form(exp)


print normal_form(["app",["lam","true",["app",["lam","false",["app",["lam","and",["app",["app",["var","and"],["var","true"]],["var","true"]]],["lam","a",["lam","b",["app",["app",["var","a"],["var","b"]],["var","false"]]]]]],["lam","a",["lam","b",["var","b"]]]]],["lam","a",["lam","b",["var","a"]]]])
    
