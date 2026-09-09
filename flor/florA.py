import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation, PillowWriter

NUM_PETALOS = 12        
RADIO_CENTRO = 0.6        
LARGO_PETALO = 1.6        
ANCHO_PETALO = 0.7        
DISTANCIA_PETALO = 1.1    
COLOR_PETALO = "#FFD700"  
COLOR_CENTRO = "#8B4513"  
FRAMES_POR_PETALO = 6     
TEXTO = "Text"   
COLOR_TEXTO = "#333333"   
TAMANO_TEXTO = 20         
POSICION_Y_TEXTO = 2.4    

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor("white")

centro = patches.Circle((0, 0), RADIO_CENTRO, color=COLOR_CENTRO, zorder=5)
ax.add_patch(centro)

texto = ax.text(
    0, POSICION_Y_TEXTO, TEXTO,
    ha="center", va="center",
    fontsize=TAMANO_TEXTO, color=COLOR_TEXTO,
    fontweight="bold", alpha=0, zorder=10,
)

angulos = np.linspace(0, 360, NUM_PETALOS, endpoint=False)

petalos = []
for angulo in angulos:
    rad = np.deg2rad(angulo)
    x = DISTANCIA_PETALO * np.cos(rad)
    y = DISTANCIA_PETALO * np.sin(rad)
    petalo = patches.Ellipse(
        (x, y),
        width=LARGO_PETALO,
        height=ANCHO_PETALO,
        angle=angulo,
        color=COLOR_PETALO,
        alpha=0,          
        zorder=1,
    )
    ax.add_patch(petalo)
    petalos.append(petalo)

FRAMES_TEXTO = 15  
FRAMES_PETALOS = NUM_PETALOS * FRAMES_POR_PETALO
TOTAL_FRAMES = FRAMES_PETALOS + FRAMES_TEXTO


def actualizar(frame):
    
    indice_petalo = frame // FRAMES_POR_PETALO
    progreso_dentro_petalo = (frame % FRAMES_POR_PETALO) / FRAMES_POR_PETALO

    for i in range(min(indice_petalo, len(petalos))):
        petalos[i].set_alpha(1)

    if indice_petalo < len(petalos):
        petalos[indice_petalo].set_alpha(progreso_dentro_petalo)

    if frame >= FRAMES_PETALOS:
        progreso_texto = (frame - FRAMES_PETALOS) / FRAMES_TEXTO
        texto.set_alpha(min(progreso_texto, 1))

    return petalos + [centro, texto]

anim = FuncAnimation(
    fig, actualizar, frames=TOTAL_FRAMES + FRAMES_POR_PETALO,
    interval=80, blit=True, repeat=False
)

#Gif animado
anim.save("Flor.gif", writer=PillowWriter(fps=15))
print("Animación guardada como 'Flor.gif'")

