import gymnasium as gym
import time

env=gym.make('CartPole-v1',render_mode='human')

env.reset()
env.render()
action = env.action_space.sample()
for i in range(1000):
    observation, reward, terminated, truncated, info = env.step(action)
    cp, cv, pa, pv = observation
    action = 1 if pa > 0 else 0
    time.sleep(0.05)

