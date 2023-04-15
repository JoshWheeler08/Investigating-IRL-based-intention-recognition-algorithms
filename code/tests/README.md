# Explanation of API tests

Tests used to check my experiments are working as expected.


**Please Note that these tests must be run from inside the working directory, `src/`, due to Python import issues**

E.g. - src
        - play_different_envs.py
        - example_models/
        - MyAgents/
        - Wrapper/
        - test_full_framework_functionality.py
    

## Configuration information 
- **All tests must be run from the working directory `./src/` due to Python import issues**

## check_game_play/
- I created this directory to store my Python programs for running the learned `Owner` (knight) and `Assistant`(archer) agent policies in the KAZ game environment after training. Since these policies were generated during my experiments, I already had graphical visualisations of their performance, but I included these tests so that I could *see* the behaviour exhibited by both agents in the game. This would allow me to identify how (i.e. what behaviour) the `IRL-based assistant agent` had learned to protect the `knight` in order to maximise its *expected return*.

- The directory contains 5 tests for showing the agents playing on some variants of the KAZ environment:

1. `play_different_envs_full_obs.py` loads the agents trained during the baseline test `test_train_on_different_envs_full_observation`, and plays them on the *FullObsDoubleKAZ* environment (variable time horizon).

2. `play_different_envs.py` loads the agents trained during the baseline test `test_train_on_different_envs`, and plays them on the *Double-KAZ* environment (variable time horizon).

3. `play_single_policy.py` loads the agents trained during the baseline test `test_single_rl_policy_full_observation`, and plays them on the *SingleRLPolicyDoubleKAZ* environment (variable time horizon). 

4. `play_separate_policies.py` loads the agents trained during the baseline test `test_separate_policies`, and plays them on the *DoubleKAZ* environment (variable time horizon).

5. `play_main_experiment_fixed_horizon_3000.py` loads the agents trained during a main experiment test investigating the performance impact of using a *fixed-horizon* version of KAZ set to 3000 timesteps. I wanted to see the agents trained in this particular experiment because my IRL-based assitive agent demonstrated improved cooperation with the knight as shown by the W&Bs experiment tracking visuations. Therefore, I was intrigued to see how the archer's behaviour had changed.

## check_game_play/example_models/
- This directory stores some of the learned agent policies from my experiments, which are then loaded into KAZ by one of the programs in `check_game_play/`.


## env_tests/
**These tests must also be run from inside the `src/` directory due to issues with Python's import feature.**

- This directory contains tests for ensuring my `fixed-horizon` and `variable-horizon` variants of the KAZ environment work before I try to include them in the experiment pipeline.

+ `test_fixed_horizon_kaz_works.py` checks that fixed-horizon KAZ variants can be registered/rendered in `OpenAI Gym` and used for training agents with `Stable-Baselines3`.

+ `test_variable_horizon_kaz_works.py` checks that variable-horizon KAZ variants can be registered/rendered in `OpenAI Gym` and used for training agents with `Stable-Baselines3`.


## Other API tests

- `test_classic_gym_game_set_up.py` : Small program used to verify that my KAZ game environments (`./src/envs/`) can be rendered and played before including any trained agents. As a result, the *knight's* and *archer's* actions per timestep are randomly selected by sampling from their respective actions spaces.

- `test_full_framework_functionality.py` : Program to test all the API commands in my *Owner* and *Assistant* agent implementations by running through the experiment pipeline, which consists of:  
    * Registering the KAZ environments with OpenAI Gym library
    * Creating the Owner Agent
    * Training the Owner Agent
    * Evaluating the Owner Agent
    * Playing a game with the Owner Agent (not necessary for experiment but included to test functionality)
    * Saving the Owner Agent's Policy
    * Loading the Owner Agent's Policy
    * Creating the Assistant Agent
    * Training the Assistant Agent
    * Evaluating the Assistant Agent's RL policy (for learning single player behaviour)
    * Evaluating the Assistant Agent's internal model (for intention recognition)
    * Evaluating the Assistant Agent's Final Policy (RL + IRL)
    * Saving the Assistant Policy
    * Loading the Assistant Policy
    * Playing a game with the Assistant's RL policy
    * Playing a game with the Assistant's learned Internal Model of the Owner agent (knight)
    * Playing a game with the Assistant's Final policy, where the `knight` is also acting in the game