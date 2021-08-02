import matplotlib.pyplot as plt
import numpy as np
from thetas import thetas
from theta_hat import prob_A as theta_hat_prob_A, l_A as theta_hat_l_A, prob_B as theta_hat_prob_B, l_B as theta_hat_l_B
from quantity import prob_A as quantity_prob_A, l_A as quantity_l_A, prob_B as quantity_prob_B, l_B as quantity_l_B



# plt.plot(thetas, theta_hat_prob_A, color="green")
# plt.plot(thetas, quantity_prob_A, color="blue")
plt.plot(thetas, theta_hat_prob_B, color="green")
plt.plot(thetas, quantity_prob_B, color="blue")
plt.axline((-4, 0.05), (4, 0.05), color="red")
plt.yticks([0, 0.05, 0.5, 1.0])
plt.ylabel("Função Poder")
plt.xlabel("theta")
plt.savefig("theta_2.png")