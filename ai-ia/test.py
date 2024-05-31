# This python file is to play around with gym library to be used in the first assignment 

import gymnasium as gym
from collections import deque

env = gym.make("Taxi-v3", render_mode="ansi")
env.reset(seed=2)
# env.reset()
# print(env.action_space.n) 

# print(env.render())

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

def testPassenger(movement=[]):
    totalPoint = 0
    if len(movement) > 0:
        for dir in movement: 
            obs, reward, done, moved, info = env.step(dir)
            print(env.render())
            print(tuple(env.unwrapped.decode(obs)))
            totalPoint += reward
            print(f"reward is {reward}")
            print(info)
            if moved or done: 
                env.reset()
    
    print(f"total point is {totalPoint}")

def dfs(env):
    # stack = deque()
    # visited = set()

    # initial_state = env.reset()
    # stack.append((initial_state, []))

    # while stack:
    #     state, path = stack.pop()

    #     if state in visited:
    #         continue

    #     visited.add(state)

    #     env.render()

    #     for action in range(env.action_space.n):
    #         next_state, reward, done, info = env.step(action)
    #         env.render()
    #         if done: 
    #             print(f"Goal reached with path: {path + [action]}")
    #             return path + [action]
            
    #         stack.append((next_state, path + [action]))

    #         env.reset()
    #         env.s = state

     visited = set()
     
     initial_state = env.reset(seed=2)
     print(initial_state)
     print(env.render())

     next_state, reward, done, moved, info = env.step(0)
     print(next_state)
     print(env.render())



if __name__ == "__main__":
    # print(observation)
    # print(reward)
    # print(terminated)
    # print(truncated)
    # print(info)
    # print(env.render())
    # print(tuple(env.decode(observation)))
    # print(tuple(env.unwrapped.decode(observation))) # this is used to find out taxi loc, passenger, and dropoff
    # move(steps=2, direction=1)
    # print(env.render())
    # testPassenger([0, 3, 0, 0])
    # dfs(env)
    # print(env.reset()[0]) 
    initial_state = env.reset()[0]
    print(env.P[initial_state])