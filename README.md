# CPython 2.7 Bytecode Interpreter written in Python

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