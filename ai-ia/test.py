# This python file is to play around with gym library to be used in the first assignment 

from gymnasium import gym

env = gym.make("Taxi-v3", render_mode="ansi")
env.reset()

action = env.action_space.sample()

state, reward, terminated, truncated, info = env.step(action)


if __name__ == "__main__":
    # print(state)
    # print(reward)
    # print(terminated)
    # print(truncated)
    # print(info)
    print(env.render())