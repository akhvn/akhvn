import time

def write(file_w,s):
    file_w.writelines(s)
    return

def dec(w):
    def decor(function):
        def the_wrapper(*args, **kwargs):
            begin=time.time()
            ans=function(*args, **kwargs)
            end=time.time()
            tm=begin-end
            out=[]
            out.append(time.ctime(begin))
            out.append('\n')
            if args:
                for i in args:
                    out.append(str(i)+' ')
            if kwargs:
                for j in kwargs:
                    out.append(str(j)+ ' ')
            out.append('\n')
            if ans:
                out.append(str(ans))
                out.append('\n')
            else:
                out.append(' - ')
                out.append('\n')
            out.append(time.ctime(end))
            out.append('\n')
            out.append(str(tm))
            out.append('\n')
            a=open(w,'w')
            write(a,out)
            return ans
        return the_wrapper
    return decor

@dec('7.txt')
def f(x,y,show):
    res=x*y
    return res

print(f(2,3,True))
