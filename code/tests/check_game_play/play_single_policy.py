"""
    This is a small program which loads the agents trained during the baseline test `test_single_rl_policy_full_observation`, 
    and plays them on the *SingleRLPolicyDoubleKAZ* environment (variable time horizon). 

"""

import gym
from gym.envs.registration import register

from Wrappers import KAZTrainingWrapper
from MyAgents.Objects.EnvObject import EnvObject
from MyAgents.Assistant import Assistant
from MyAgents.Owner import Owner

from common.constants import IGNORE_HORIZON
from common.common import select_skill_level

# Register Environment

register(
    id="SingleRLPolicyDoubleKAZ-v0",
    entry_point="envs.kaz_variants.variable_horizon.single_policy_double_player:SingleRLPolicyDoubleKAZ",
    max_episode_steps=None,
)

# Set Skill Level
select_skill_level('vanilla')


# Load model
controller = Owner() # Single policy so don't need distinct Owner and Archer agent objects
path = "./example_models/single_policy/"
controller.load_policy(path, policy_type="PPO")


# Play Game

env_kwargs = {
    "env_output":False,
    "user_seed":900,
    "fixed_horizon_num_steps" : IGNORE_HORIZON,
    "max_zombies": 10,
}

# Object to describe game environment
env_obj = EnvObject(
    env_id="SingleRLPolicyDoubleKAZ-v0",
    n_envs=1,
    total_timesteps=100000,
    env_kwargs=env_kwargs,
    seed=900,
)

print("HERE")

controller.play_game_with_rl_policy(env_obj=env_obj)