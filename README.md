# nlp-examples

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
