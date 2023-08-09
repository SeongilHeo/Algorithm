# Algorithm

P : Programmers  
B : Backjoon  
H : Hufs  
Hack : Hackerrank
E : Etc  
C : CodeTree

##### file
```python #
# 2021-01-01
# src : ...
code ...
```

##### when use jupyter
```python
which= ""
problem_name=""
with open("%s-%s.py"%(which,problem_name),'w') as f:
    f.write(code)
```

ex)
```python
which= "B"
problem_name="No."+code.split('\n')[0].split('/')[-1]
with open("C:/Users/tjddl/Desktop/algom/%s-%s.py"%(which,problem_name),'w') as f:
    f.write(code)
```
