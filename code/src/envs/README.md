# KAZ CORE

## Description

- `KAZ_core/`contains my vanilla implementations of the KAZ environment for both one (SingleKAZ) and two players (DoubleKAZ). These two implementations are based on PettingZoo's original KAZ code, which I have altered to support both single and double agent training in `OpenAI Gym`. Some files I have left completely untouched including everything in `./envs/kaz_core/src`, except for the `skill_levels/` directory.

+ `double_player.py` = Vanilla, variable-horizon KAZ implementation for two players, where one agent's policy (the knight's) must be passed into the environment as an *** argument *** before performing episodic training in `OpenAI gym` using `SB3`.

+ `single_player.py` = Vanilla, variable-horizon KAZ implementation for one player, where the type of player to be trained is controlled by the value of the `type_of_player` argument.

+ `fixed_horizon_double_player.py` = Vanilla, fixed-horizon KAZ implementation for two players, where the `horizon limit` is accepted as an argument.

+ `fixed_horizon_single_player.py` = Vanilla, fixed-horizon KAZ implementation for one player, where the `horizon limit` is accepted as an argument.

- `img/` contains the images for rendering the game environment (using Pygame), players and weapons - provided by PettingZoo.


## skill_levels

This directory contains three Python ***constant*** files for controlling the difficulty level of the game by changing the speed of the ***archer's arrows*** - since this will impact how much it can assist/protect the knight.

- `vanilla.py` : The default configuration for Players and their Weapons. Archer arrow speed = 45

- `medium.py` : Archer arrow speed = 35

- `hard.py` : Archer arrow speed = 25


# KAZ Variants
This directory contains KAZ implementations derived from my algorithms in `kaz_core`, where certain functions have been ***overidden** to produce some new behaviour in the game.



## fixed_horizon

- `fixed_horizon_full_obs_double_player.py` = Fixed-horizon, double player KAZ implementation, where the observation returned by the environment has been changed from ***local*** to ***global** scope in the `step` and `reset` methods.

- `fixed_horizon_random_double_player.py` = Fixed-horizon, double player KAZ implementation, where the `step` function has been overidden so that the action passed by the Archer (each timestep) is ignored. Instead, the Knight and Archer take random actions sampled from their respective action spaces, unless `share_random_policy=True` then the two agents perform the same random action.

- `fixed_horizon_single_policy_double_player.py` = Fixed-horizon, double player KAZ implementation, where the `step` function has been updated so that both agents perform the same action (if the action is fire arrow, then the knight will swing its sword). This allows a single RL policy to be learned for controlling ***both agents***.



## variable_horizon

- `full_obs_double_player.py` = Variable-horizon, double player KAZ implementation, where the observation returned by the environment has been changed from ***local*** to ***global** scope in the `step` and `reset` methods.

- `random_double_player.py` = Variable-horizon, double player KAZ implementation, where the `step` function has been overidden so that the action passed by the Archer (each timestep) is ignored. Instead, the Knight and Archer take random actions sampled from their respective action spaces, unless `share_random_policy=True` then the two agents perform the same random action.

- `single_policy_double_player.py` = Variable-horizon, double player KAZ implementation, where the `step` function has been updated so that both agents perform the same action (if the action is fire arrow, then the knight will swing its sword). This allows a single RL policy to be learned for controlling ***both agents***.


## eval
This directory stores KAZ environments ***only*** used for evaluating the performance of learned policies. Rather than returning the reward of the `archer` like the other double-player KAZ implementations, these methods return the ***combined*** reward of the two agents per timestep. Therefore, this gives a better overall measure of their combined game performance rather than measuring it by the `archer's reward`.

- `double_player_eval.py` = Variable horizon, double player KAZ environment where returned reward formula has been updated as described above.

- `fixed_horizon_double_player_eval.py` = Fixed-horizon equivalent of `double_player_eval.py`.

- `full_obs_double_player_eval.py` = Variable horizon, double player, ***combined reward*** KAZ environment, which gives the `archer` agent a full game observation per timestep rather than a local observation.

- `fixed_horizon_full_obs_double_player_eval.py` = Fixed-horizon equivalent of `fixed_horizon_double_player_eval.py`.



## Links

- PettingZoo (https://pettingzoo.farama.org/environments/butterfly/knights_archers_zombies/) 

- Pygame (https://www.pygame.org/news)