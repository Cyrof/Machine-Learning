# This python file is to play around with gym library to be used in the first assignment 

import gymnasium as gym
import pickle

env = gym.make("Taxi-v3", render_mode="ansi")
env.reset(seed=10)

print(env.render())

def move(steps=0, direction=None): 
    points = 0
    directions = [0,1,2,3]
    if direction not in directions:
        raise "unknown direction"
    
    if steps == 0: 
        return

    for _ in range(steps):
        obs, reward, done, moved, info = env.step(direction)
        print(env.render())
        points += reward
        # if done or moved:
        #     testEnv.reset()
        if moved:
            env.reset()
        if done:
            env.reset(seed=10)
    
    print(f"Total points is {points}")


if __name__ == "__main__":
    # print(observation)
    # print(reward)
    # print(terminated)
    # print(truncated)
    # print(info)
    # print(env.render())
    # print(tuple(env.decode(observation)))
    # print(tuple(env.unwrapped.decode(observation))) # this is used to find out taxi loc, passenger, and dropoff
    move(steps=2, direction=1)
    print(env.render())