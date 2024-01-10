import os
from collections import OrderedDict
from operator import add
from random import randrange

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data una colonna del dataframe e un elenco di chiavi da tenere,
# per ogni cella nella colonna (contenente un simil-dizionario) ricreo una entry chiave: valore
# con default a 0 se la chiave non c'è (i.e. c'erano zero token di quel tipo)
def mangle_dict_value(cell_data, what):
    ret = []
    for x in cell_data:
        x = dict((a.strip(" {}'"), int(b.strip(" {}'")))
                      for a, b in (element.split(':')
                                   for element in x.split(', '))
                                   if a.strip(" {}'") in what)
        ret.append(dict((_col, x[_col]) if _col in x else (_col, 0) for _col in what))
    return ret


def filter_csv(csv_file):

    # ogni cella di questo dataframe è una stringa che somiglia a un dizionario
    # ma alcune chiavi sono PetriNet('blabla') quindi non si può convertire automaticamente
    df = pd.read_csv(os.path.join(os.getcwd(), csv_file), index_col=[0])
    # df = df.dropna(axis=1, how='all')
    # filtro solo le colonne che mi interessano, partendo da un prodotto cartesiano
    _cols = [color + str(j) + "_" + str(k) for color in ["red_", "green_", "blue_"] for j in [1, 2, 3, 4, 5] for k in [1, 2, 3, 4, 5]]
    # droppo i nomi di colonne che non esistono nel dataframe
    _cols = [_col for _col in _cols if _col in df.columns]
    del df['grey_0_0']
    # print(_cols)
    # qui _col è il nome di un posto. a me interessano solo quelli con token colorati (i.e. le cellule R G o B)
    for _col in _cols:
        _res = mangle_dict_value(df[_col], ['BFP_protein', 'mCherry_protein', 'GFP_protein'])
        df[_col] = _res
    return df


if __name__ == '__main__':
    df = filter_csv(r"results/marking_rgb_Toda_net .csv")
    # print(df.head())
    # df.to_csv("pippo")
    green_coords = OrderedDict({'green_3_3': (3, 3)})
    red_coords = OrderedDict(("red_" + str(i) + "_" + str(j), (i, j)) for i in [2, 3, 4] for j in [2, 3, 4] if "red_" + str(i) + "_" + str(j) in df.columns)
    blue_coords = OrderedDict(("blue_" + str(i) + "_" + str(j), (i, j)) for i in [1, 2, 3, 4, 5] for j in [1, 2, 3, 4, 5] if "blue_" + str(i) + "_" + str(j) in df.columns)
    all_coords = OrderedDict()
    for d in [green_coords, red_coords, blue_coords]:
        all_coords.update(d)
     # print(df.loc[[0]])

    _colors = ['mCherry_protein', 'GFP_protein', 'BFP_protein']
    datapoints = OrderedDict()
    # per ogni riga (step)
    for i in range(0, len(df)):
        i_df = df.loc[[i]]
        datapoints[i] = OrderedDict()
        # per ogni posto
        for col in i_df.columns:
            val_dict = i_df[col].array[0]
            tot = sum(val_dict.values())
            rgb = tuple([round(val_dict[_color] / tot, 2) if tot > 0 else 0 for _color in _colors])
            datapoints[i][col] = rgb
            pass

    X, Y = list(map(list, zip(*[all_coords[_k] for _k in sorted(all_coords.keys())])))
    # scatter data a little bit
    # X = list(map(add, X, (0.8 * np.random.rand(len(X)))**2))
    # Y = list(map(add, Y, (0.8 * np.random.rand(len(Y)))**2))
    X = list(map(add, X, [0.1 * randrange(-1, 1) for _ in range(len(X))]))
    Y = list(map(add, Y, [0.1 * randrange(-1, 1) for _ in range(len(Y))]))
    # S = 1500
    S = list(map(add, [1500 for _ in range(len(X))], [randrange(-400, 400) for _ in range(len(X))]))  # list(1500 * 0.9 * np.random.rand(len(X))**2)
    for _t in range(0, len(datapoints), 1):
        fig, ax = plt.subplots()

        C = list(datapoints[_t].values())

        ax.scatter(X, Y, c=C, s=S, alpha=0.5)

        ax.set_xlabel(r'$x$', fontsize=15)
        ax.set_ylabel(r'$y$', fontsize=15)
        ax.set_title(f"t = {_t}")
        ax.margins(0.2, 0.2)

        # fig.tight_layout()

        plt.savefig(f"img_{_t}.png")
        plt.close()
