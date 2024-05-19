1. Make the environment: `python3 -m venv .venv`
2. Activate the environment: `source .venv/bin/activate`
3. Download packages: `python3 -m pip install -r requirements.txt`
4. Install ipykernel: `python -m ipykernel install --user --name trading`
5. Fire up a jupyter notebook: `jupyter notebook`
6. Install new libraries: `pip install new_library`
7. Update the requirements.txt: `pip freeze > requirements.txt`
8. For using the functions in the folder utils, I recommend that to install that as a library in dev mode: `pip install -e .`
9. After installation, one can use the library as `import utils` in  notebooks

For the trading exercises, majority of the experiments were inspired by notebooks in https://github.com/stefan-jansen/machine-learning-for-trading