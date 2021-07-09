import matplotlib.pyplot as plt
import numpy as np

medias = np.array([7.88, 5.21, 6.85, 5.90,  6.28, 8.46, 7.08, 3.41, 5.11, 8.11])

nomes = np.array(["Lucia","Ana", "Léo", "Bruno", "Michel", "Raul", "Lucas","Caio","Paulo", "Vitor"])

plt.plot(nomes, medias, 'bo')
plt.title('Médias x Alunos')
plt.show()
