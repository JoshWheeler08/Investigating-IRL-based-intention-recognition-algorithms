# src

## Description

This directory contains the source code for running my baseline and main experiments (IRL-agents enabled), which are organised into a few files and some directories:

- `./baselines/kaz/kaz_baselines.py` contains the source code for my KAZ environment baseline tests of which there are six.

- `./common/` contains common code shared by both experiment programs.

- `./configuration/` contains my configuration files for tweaking the hyperparameters of the experiments.

- `./envs/` contains my KAZ environment implementations (single and double player) as well as its variants.

- `./irl_training/` contains my IRL algorithm implementations.

- `./MyAgents/` contains Python classes for representing the Owner/Human player and Assistant player.

- `./Wrappers/` contains my OpenAI Gym Wrapper implementations which are used to change the behaviour of the environment without modifying its underlying code.

- `./main_experiment_output` stores the output of my main experiments.

- `main_experiment_core.py` is a Python file containing the core code for running my experiments, which investigate the performance of IRL-based assistive agents in KAZ (or any suitable) environment.  

- `run_main_experiment.py` is a Python program for running my main experiments (i.e. tests investigating the performance impact of IRL-based agents) by calling methods in `main_experiment_core.py`.

- `run_kaz_baselines.py` is a Python program for running my KAZ environment baseline tests (i.e. no IRL-based agents) by calling methods in `kaz_baselines.py` and `common.py`.