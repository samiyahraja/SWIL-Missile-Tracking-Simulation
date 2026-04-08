import numpy as np

def get_noisy_measurement(true_position):
    noise = np.random.normal(0, 0.5, size=2)
    return true_position + noise
