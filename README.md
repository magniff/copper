# COPPER

Available on linux only.

Copper is a simple implementation of dataflow pipes (like python generator based 'pipes' module). However instead of generators is uses coroutines.
See examples, the code is strait forward as hell.

Works on Linux machines, win is not supported.

To run examples install copper in develop mode:
```sh
python setup.py develop
```
Then, for instance:
```sh
(venv)magniff@/home/magniff/Desktop/copper$ python examples/factorial.py 
factorial 1
factorial 2
factorial 6
factorial 24
factorial 120
factorial 720
factorial 5040
factorial 40320
factorial 362880
factorial 3628800
End of stream.
```
