# How to run my experiments

## Python Setup

CWD: `~/cs5199-dissertation/`

To run my experiments, you will need to install the required Python packages (listed in `./code/requirements.txt`), which can be stored in a Python virtual environment (venv). The below commands explain how to do this:

- `python3 -m venv env` - Creates a Python virtual environment to manage the project's packages
- `source env/bin/activate` - Activates the virtual environment
- `pip3 install -r ./code/requirements.txt` - Installs the required packages

## Running the experiments

CWD: `~/cs5199-dissertation/code/src/`

To run the baseline tests, use:
- `python3 ./run_kaz_baselines.py <path-to-configuration-file?>` 
OR
- `./run_kaz_baseline_tests.sh`


To run the main experiments, use:
- `python3 ./run_main_experiment.py <path-to-configuration-file?>`
OR
- `./run_main_experiment_tests.sh`


### How to change the experiment hyperparameters

To alter the **baseline** and **main experiment** hyperparameters, modify their respective configuration files stored in `./configuration`:
- `kaz_baselines_config.yaml` = The KAZ Baselines configuration file
- `main_experiment_config.yaml` = The Main Experiment configuration file