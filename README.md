# COPPER

Available on linux only.

Copper is a simple implementation of dataflow pipes (like python generator based 'pipes' module). However instead of generators is uses coroutines.
See examples, the code is strait forward as hell.

To run examples install copper in develop mode:
```sh
python setup.py develop
```
Then, for instance:
```sh
(venv)magniff@/home/magniff/Desktop/copper$ python examples/simple_numbers.py 
1
4
9
```
