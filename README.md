# nlp-examples

Welcome to nlp-examples! 
This is the main repository that we used during the training. 
There are 12 notebooks that we used during the development of 
Literature Recommendation Software (LRS) to find best topic 
modeling technique and best model parameters.

The name of notebooks starts with a number that mostly indicates 
in which order the notebooks are run. Basically, output of the 
notebook that has lower number is given as an input to a notebook 
that has higher number. However, running notebooks over the all 
dataset might not be possible since training is taking very large 
amount of time. Also, we cannot share the input files that require 
are required for notebooks since they are very big.

The dataflow in the notebooks might be seen a bit confusing at first glance. 
Therefore, we created an explanatory notebook that contains 
whole pipeline from raw input PDF files to predicting articles given user input.
#### We strongly recommend you to check 00_FINAL_ALL_PIPELINE.ipynb 
notebook first to getting used the concept and the environment.


1. ## Install environment
   1. Create an virtual environment 
   ```shell
   virtualenv --python=python3.8 .venv
   ```

   2. Activate environment
   ```shell
   source .venv/bin/activate
   ```

   3. Install required python packages
   ```shell
   pip3 install -r requirements.txt
   ```

2. ## Run notebooks
Activate vitual environment if it is not activated. Then run the notebook:

```shell
jupyter notebook
```

3. ## Keep dependecies clear
All dependecies will be saved in `requirements.txt`. If a new library is needed for a notebook, please update dependecies on `requirements.txt` accordingly. You can follow the steps below to update it quickly:

- Be sure to activate the environment as shown in **1.ii.**
- Install the packages that you need like `pip3 install <package name>`
- Update the `requirements.txt`:
```shell
pip3 freeze -r requirements.txt > requirements.txt
```
4. ## Throubleshooting
  - Environment installation error in step 1
  If you have a problem installing requirement.txt and you got errors like below:
  ```
  Building wheels for collected packages: cytoolz
  Building wheel for cytoolz (setup.py) ... error
  ERROR: Command errored out with exit status 1:
   command: /home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"'; __file__='"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /tmp/pip-wheel-l_ovmhcc
       cwd: /tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/
  Complete output (57 lines):
  ALERT: Cython not installed.  Building without Cython.
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.linux-x86_64-3.8
  creating build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/_signatures.py -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/utils_test.py -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/__init__.py -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/compatibility.py -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/_version.py -> build/lib.linux-x86_64-3.8/cytoolz
  creating build/lib.linux-x86_64-3.8/cytoolz/curried
  copying cytoolz/curried/__init__.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
  copying cytoolz/curried/exceptions.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
  copying cytoolz/curried/operator.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
  copying cytoolz/recipes.pyx -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/utils.pyx -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/dicttoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/functoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/itertoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/functoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/__init__.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/itertoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/utils.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/dicttoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/recipes.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  copying cytoolz/cpython.pxd -> build/lib.linux-x86_64-3.8/cytoolz
  creating build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_itertoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_compatibility.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_none_safe.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_docstrings.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_embedded_sigs.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_utils.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_tlz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_doctests.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_serialization.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_dicttoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_curried.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_inspect_args.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_curried_toolzlike.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/dev_skip_test.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_dev_skip_test.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_functoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_signatures.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  copying cytoolz/tests/test_recipes.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
  running build_ext
  building 'cytoolz.dicttoolz' extension
  creating build/temp.linux-x86_64-3.8
  creating build/temp.linux-x86_64-3.8/cytoolz
  x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/include -I/usr/include/python3.8 -c cytoolz/dicttoolz.c -o build/temp.linux-x86_64-3.8/cytoolz/dicttoolz.o
  cytoolz/dicttoolz.c:17:10: fatal error: Python.h: No such file or directory
   #include "Python.h"
            ^~~~~~~~~~
  compilation terminated.
  error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for cytoolz
  Running setup.py clean for cytoolz
Failed to build cytoolz
Installing collected packages: cytoolz
    Running setup.py install for cytoolz ... error
    ERROR: Command errored out with exit status 1:
     command: /home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"'; __file__='"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-c4ppugzm/install-record.txt --single-version-externally-managed --compile --install-headers /home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/include/site/python3.8/cytoolz
         cwd: /tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/
    Complete output (57 lines):
    ALERT: Cython not installed.  Building without Cython.
    running install
    running build
    running build_py
    creating build
    creating build/lib.linux-x86_64-3.8
    creating build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/_signatures.py -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/utils_test.py -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/__init__.py -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/compatibility.py -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/_version.py -> build/lib.linux-x86_64-3.8/cytoolz
    creating build/lib.linux-x86_64-3.8/cytoolz/curried
    copying cytoolz/curried/__init__.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
    copying cytoolz/curried/exceptions.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
    copying cytoolz/curried/operator.py -> build/lib.linux-x86_64-3.8/cytoolz/curried
    copying cytoolz/recipes.pyx -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/utils.pyx -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/dicttoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/functoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/itertoolz.pyx -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/functoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/__init__.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/itertoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/utils.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/dicttoolz.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/recipes.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    copying cytoolz/cpython.pxd -> build/lib.linux-x86_64-3.8/cytoolz
    creating build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_itertoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_compatibility.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_none_safe.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_docstrings.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_embedded_sigs.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_utils.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_tlz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_doctests.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_serialization.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_dicttoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_curried.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_inspect_args.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_curried_toolzlike.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/dev_skip_test.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_dev_skip_test.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_functoolz.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_signatures.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    copying cytoolz/tests/test_recipes.py -> build/lib.linux-x86_64-3.8/cytoolz/tests
    running build_ext
    building 'cytoolz.dicttoolz' extension
    creating build/temp.linux-x86_64-3.8
    creating build/temp.linux-x86_64-3.8/cytoolz
    x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -I/home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/include -I/usr/include/python3.8 -c cytoolz/dicttoolz.c -o build/temp.linux-x86_64-3.8/cytoolz/dicttoolz.o
    cytoolz/dicttoolz.c:17:10: fatal error: Python.h: No such file or directory
     #include "Python.h"
              ^~~~~~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command errored out with exit status 1: /home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"'; __file__='"'"'/tmp/pip-install-wxiy022a/cytoolz_d9b580d4b55243bfb0ef77dd375bca11/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /tmp/pip-record-c4ppugzm/install-record.txt --single-version-externally-managed --compile --install-headers /home/melike/Desktop/IDP_NLP/ProjectCode/nlp-examples/.venv/include/site/python3.8/cytoolz Check the logs for full command output.
  ```
  
  <a href="https://github.com/ethereum/web3.py/issues/531#issuecomment-365486495">This thread</a> may help you to fix the problem:
  `sudo apt install python3.8-dev`
