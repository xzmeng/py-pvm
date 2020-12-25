# CPython 2.7 Bytecode Interpreter written in Python
This repo is an imitation of nedbat's [byterun](https://github.com/nedbat/byterun/).
## CPython Workflow

1. Lexical Analysis -> tokens
2. Syntactic Analysis -> AST
3. Compile -> bytecode
4. Evaluate -> result

So the goal is to implement the step 4.

## code object
```python
code = compile(open(filename).read(), filename, "exec")
```
With the built-in ```compile``` Python provides, we can easily get a ```code``` object which includes the bytecode, names etc.

## How to use
```python
python -m pvm demo.py
```

Comfirm all test cases are passed
```bash
coverage run -m pytest
coverage report
```

## Support

- Python 2.7 is compelely supported
- Python 3.5 has a limited support
- Don't support Python 3.6 and above

## References
1. https://github.com/nedbat/byterun/
2. https://pg.ucsd.edu/cpython-internals.htm
3. https://docs.python.org/2.7/library/dis.html
4. https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
5. http://qingyunha.github.io/taotao/
6. Python源码剖析(陈儒 2008)