import matplotlib; matplotlib.use("TkAgg")
import time
from edempy import Deck
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import strftime

start = time.time()
#test czy umiem wrzucac na gita123
path = "C:\\Users\\Jakub\\PycharmProjects\\test2\\testownik11_prof_Robert_Krol\\projekt_2\\POLKOWICE_etap_2\\simulation_0\\simulation_0.dem"
deck = Deck(path)

print("liczba krokow czasowych", deck.numTimesteps)

# nGeoms = len(deck.geometryNames)  #to show all geometries
nGeoms_name = deck.geometryNames


def draw_trajectory(is_lupek=True, is_piaskowiec=True, is_dolomit=True,
                    is_draw=True, is_draw_geometry=False, is_save=False):
    # Step 3: Setup figure
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('RockBox Streamlines')

    if is_lupek:
        """ LUPEK """
        tab_lupek = []
        for i in range(0, 5):
            try:
                for j in deck.timestep[i].particle[0].getIds():
                    if j not in tab_lupek and 30 > (deck.timestep[i].particle[0].getSphereRadii(j) * 2000) > 20:
                        tab_lupek.append(j)
            except Exception:
                continue
        part_lupek = tab_lupek  # [values]
        for i in part_lupek:
            tab = []
            for j in range(0, 260):
                try:
                    tab.append(deck.timestep[j].particle[0].getPositions(i))
                except Exception:
                    continue
            pos_tab = np.array(tab)
            ax.plot(pos_tab[:, 0], pos_tab[:, 1], pos_tab[:, 2], color='b')

    if is_piaskowiec:
        """ PIASKOWIEC """
        tab_piaskowiec = []
        for i in range(0, 5):
            try:
                for j in deck.timestep[i].particle[1].getIds():
                    if j not in tab_piaskowiec and 30 > (deck.timestep[i].particle[1].getSphereRadii(j) * 2000) > 10:
                        tab_piaskowiec.append(j)
            except Exception:
                continue
        part_piaskowiec = tab_piaskowiec  # [values]
        for i in part_piaskowiec:
            tab = []
            for j in range(0, 260):
                try:
                    tab.append(deck.timestep[j].particle[1].getPositions(i))
                except Exception:
                    continue
            pos_tab = np.array(tab)
            ax.plot(pos_tab[:, 0], pos_tab[:, 1], pos_tab[:, 2], color='r')

    if is_dolomit:
        """ DOLOMIT """
        tab_dolomit = []
        for i in range(0, 5):
            try:
                for j in deck.timestep[i].particle[2].getIds():
                    if j not in tab_dolomit and 30 > (deck.timestep[i].particle[2].getSphereRadii(j) * 2000) > 10:
                        tab_dolomit.append(j)
            except Exception:
                continue
        part_dolomit = tab_dolomit[::3]  # [values]
        for i in part_dolomit:
            tab = []
            for j in range(0, 260):
                try:
                    tab.append(deck.timestep[j].particle[2].getPositions(i))
                except Exception:
                    continue
            pos_tab = np.array(tab)
            ax.plot(pos_tab[:, 0], pos_tab[:, 1], pos_tab[:, 2], color='g')


    if is_draw_geometry:
        # GEOMETRY
        tab_geoms = list([nGeoms_name.index("fabryka"), nGeoms_name.index("oslona"), nGeoms_name.index("tyl"),
                          nGeoms_name.index("ruszt"), nGeoms_name.index("gora"),  # nGeoms_name.index("wirnik"),
                          nGeoms_name.index("przod"), nGeoms_name.index("bok_l"), nGeoms_name.index("bok_p"), ])

        # Step 4: Plot geometries
        for i in tab_geoms:
            x = deck.creatorData.geometry[i].getXCoords()
            y = deck.creatorData.geometry[i].getYCoords()
            z = deck.creatorData.geometry[i].getZCoords()
            tri = deck.creatorData.geometry[i].getTriangleNodes()
            ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, triangles=tri, alpha=0.2, color='lightgrey')

    if is_save:
        plt.savefig(f"trajectory_{time.strftime('%m_%d_%Y-%H_%M_%S')}.png")

    if is_draw:
        plt.show()

koniec = time.time()
print("czas: ", koniec - start)

draw_trajectory(is_save=True, is_draw_geometry=True)