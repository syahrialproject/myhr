p = [15,12,8,8,7,7,7,6,5,3]
h = [10,25,17,11,13,17,20,13,9,15]

def mean(x):
    return sum(x)/len(x)

def slope(x, y):
    meanx = mean(p)
    meany = mean(h)

    cov = 0
    var = 0
    for i in range(len(p)):
        cov += (p[i]-meanx)*(h[i]-meany)
        var += (p[i]-meanx)**2
    return cov/var

def cont(x, y):
    return (mean(h)-(slope(p, h))*mean(p))

result = (10*slope(p,h))+cont(p, h)

print("{:.1f}".format(result))
