import numpy as np
import gym

from gym import spaces

# This wrapper is only used for augmenting vector-state observations not pixel-based ones (see DoubleKAZ - observe())

class KAZTrainingWrapper(gym.Wrapper):

    """ OpenAI Gym Wrapper for augmenting the observation returned by the environment before giving it to the Assistant agent """

    def __init__(self, env, rl_policy, internal_model_policy, running_in_gym_flag=False):
        super().__init__(env)
        self.rl_policy = rl_policy
        self.internal_model_policy = internal_model_policy
        self.running_in_gym_flag=running_in_gym_flag
        

        # Final Assistant policy is trained on observations of the entire game, rather than having a local scope, 
        # so need to update num_tracked formula 
        self.num_tracked = (
            self.env.num_archers + self.env.num_knights + self.env.max_zombies + self.env.num_knights + self.env.max_arrows
        )

        # Modifying the observation space to include the two extra pieces of information that are being appended 
        # (rl_policy(Archer_Observation), internal_model_policy(Knight_Observation))
        shape = (
            [512, 512, 3]
            if not self.vector_state
            else [1, ((self.num_tracked + 1) * (self.vector_width + 1)) + 2] # + 2 for the extra values
        )
        low = 0 if not self.vector_state else -1.0
        high = 255 if not self.vector_state else 1.0
        dtype = np.uint8 if not self.vector_state else np.float64
        
        # Updating observation space
        self.observation_space = spaces.Box(low=low, high=high, shape=shape, dtype=dtype)


    def _update_observation(self, obs):
        """ Adds the RL policy and internal model policy predictions to the observation """

        rl_action, _states = self.rl_policy.predict(obs)

        owner_obs = self.env.get_knight_observation()

        internal_action, _states = self.internal_model_policy.predict(owner_obs)

        # Combine the two predictions to make a new observation
        full_game_obs = self.env.get_full_observation() # full game observation from the perspective of assistant

        new_obs = np.append(full_game_obs, [rl_action, internal_action])

        new_obs = new_obs.reshape([1, len(new_obs)]) # output has to be a flattened 

        return new_obs


    def step(self, action):
        obs, reward, done, info = self.env.step(action)

        ############ Modifying environment output here #############

        new_obs = self._update_observation(obs)

        ############ end #################

        return new_obs, reward, done, info


    def reset(self):
        
        if self.running_in_gym_flag:
            obs, info = self.env.reset()

            ############ Modifying environment output here #############
            new_obs = self._update_observation(obs)
            ############ end #################

            return new_obs, info

        else:
            obs = self.env.reset()

            ############ Modifying environment output here #############
            new_obs = self._update_observation(obs)
            ############ end #################

            return new_obs