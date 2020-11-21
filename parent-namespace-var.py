nsp={'global':None}
nsv={}

def add(namespace,var):
    nsv[var]=namespace
    return()
def create(namespace,parent):
    nsp[namespace]=parent
    return()

def get(namespace,var):
    if var in nsv and nsv[var]==namespace:
        print(namespace)
        return namespace
    elif namespace == 'global':
        print(None)
        return None
    else:
        namespace=nsp[namespace]
        return get(namespace,var)
n=int(input())
for i in range(n):
    cmd, namespace, var = input().split()
    if cmd == "add":
        add(namespace,var)
    elif cmd == 'create':
        create(namespace,var)
    elif cmd == 'get':
        get(namespace,var)
'''
add("global","a")

create('foo','global')
#print(nsp)
add('foo','b')
#print(nsv)
get('foo','a')
get('foo','c')
create('bar','foo')
add('bar','a')
get('bar','a')
get('bar','b')
'''