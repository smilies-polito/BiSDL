import errno
import os
from collections import defaultdict
from collections import OrderedDict

from operator import add
from random import randrange

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


matplotlib.rcParams.update({'font.size': 12})

class Simulator:
    def __init__(self, m, steps=None, firing_prob=0.6, output_path=".", draw_nets=False, mode='exploration'):
        self._module = m
        self._steps = steps
        self._curr_step = 0
        # self._stimuli = self._read_stimuli(stimuli)
        self._firing_prob = firing_prob
        self._output_path = output_path
        self._draw_nets = draw_nets
        self._mode= mode
        self._markings = {}
        if not os.path.exists(self._output_path):
            os.makedirs(self._output_path)

    def execute(self, nstep=None, initial_marking=None, stimuli=None):
        assert not(self._steps is None and nstep is None), f"Number of steps is None."
        if initial_marking is not None:
            self._module.set_marking(initial_marking)
        self._markings[self._curr_step] = self._module.get_marking_count()
        if self._draw_nets:
            self._module.draw(os.path.join(self._output_path, "0_" + self._module.name + "_"))
        s = nstep if nstep else self._steps
        for i in range(s):
            self.step(initial_marking if i == 0 else None, stimuli[i] if stimuli else None)

    def set_initial_marking(self, initial_marking):
        self._module.set_marking(initial_marking)

    def step(self, init_marking=None, stimuli=None):
        if init_marking is not None:
            self._module.set_marking(init_marking)
        if stimuli is not None:
            self._administer(stimuli)
        if self._curr_step == 0:
            self._module.print_marking_count(0, output_path=self._output_path)
        self._module.fire(self._curr_step, prob=self._firing_prob)
        if self._draw_nets:
            self._module.draw(os.path.join(self._output_path, str(self._curr_step + 1) + "_" + self._module.name + "_"))
        if self._output_path:
            self._module.print_marking_count(self._curr_step + 1, output_path=self._output_path)
        self._markings[self._curr_step + 1] = self._module.get_marking_count()
        self._curr_step += 1

    def draw_nets(self, path='.'):
        if not os.path.exists(path):
            os.mkdir(path)
        self._module.draw(os.path.join(path, self._module.name + "_"))


    def _administer(self, stimulus):
        self._module.add_marking(stimulus)

    def _read_stimuli(self, filename):
        if filename is None:
            self._stimuli = None
            return
        if not os.path.exists(self._output_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
        self._stimuli = pd.read_csv(filename)
        print(self._stimuli.head())
        return


    # given a dataframe column and a list of keys to hold,
    # for each cell in the column (containing a dictionary-like) I recreate a key entry: value
    # with default to 0 if the key is not there (i.e. there were zero tokens of that type)
    def mangle_dict_value(self, cell_data, what):
        ret = []
        for x in cell_data:
            x = dict((a.strip(" {}'"), int(b.strip(" {}'")))
                     for a, b in (element.split(':')
                                  for element in x.split(', '))
                     if a.strip(" {}'") in what)
            ret.append(dict((_col, x[_col]) if _col in x else (_col, 0) for _col in what))
        return ret

    def filter_csv(self, csv_file):

        # each cell in this dataframe is a string that looks like a dictionary.
        # but some keys are PetriNet('blabla') so you can't convert automatically
        df = pd.read_csv(csv_file, index_col=[0])#os.path.join(os.getcwd(), csv_file), index_col=[0])

        # filter only the columns I'm interested in, starting with a Cartesian product
        _cols = [color + str(j) + "_" + str(k) for color in ["red_", "green_", "blue_"] for j in [1, 2, 3, 4, 5] for k
                 in [1, 2, 3, 4, 5]]
        # dropping column names that do not exist in the dataframe
        _cols = [_col for _col in _cols if _col in df.columns]
        del df['grey_0_0']

        # here _col is a place name. i am only interested in those with colored tokens (i.e. R G or B cells)
        for _col in _cols:
            _res = self.mangle_dict_value(df[_col], ['BFP_protein', 'mCherry_protein', 'GFP_protein'])
            df[_col] = _res
        return df

    # plot the cells in the x y plane and their marker levels along time for the rgb example
    def make_spatial_charts(self):

        marking_file_path = os.path.join(self._output_path, "marking_rgb_net.csv")
        df = self.filter_csv(marking_file_path)

        green_coords = OrderedDict({'green_3_3': (3, 3)})
        red_coords = OrderedDict(("red_" + str(i) + "_" + str(j), (i, j)) for i in [2, 3, 4] for j in [2, 3, 4] if
                                 "red_" + str(i) + "_" + str(j) in df.columns)
        blue_coords = OrderedDict(
            ("blue_" + str(i) + "_" + str(j), (i, j)) for i in [1, 2, 3, 4, 5] for j in [1, 2, 3, 4, 5] if
            "blue_" + str(i) + "_" + str(j) in df.columns)
        all_coords = OrderedDict()
        for d in [green_coords, red_coords, blue_coords]:
            all_coords.update(d)

        _colors = ['mCherry_protein', 'GFP_protein', 'BFP_protein']
        datapoints = OrderedDict()
        # for each line (step)
        for i in range(0, len(df)):
            i_df = df.loc[[i]]
            datapoints[i] = OrderedDict()
            # for each place
            for col in i_df.columns:
                val_dict = i_df[col].array[0]
                tot = sum(val_dict.values())
                rgb = tuple([round(val_dict[_color] / tot, 2) if tot > 0 else 0 for _color in _colors])
                datapoints[i][col] = rgb

        X, Y = list(map(list, zip(*[all_coords[_k] for _k in sorted(all_coords.keys())])))
        S = 1700
        for _t in range(0, len(datapoints), 1):
            fig, ax = plt.subplots()
            C = list(datapoints[_t].values())

            ax.scatter(X, Y, c=C, s=S, alpha=0.5)
            ax.set_xlabel(r'$x$', fontsize=15)
            ax.set_ylabel(r'$y$', fontsize=15)
            ax.set_title(f"t = {_t}")
            ax.margins(0.2, 0.2)

            if not os.path.isdir(os.path.join(self._output_path, "spatial_charts")):
                os.makedirs(os.path.join(self._output_path, "spatial_charts"))

            spatial_charts_path = os.path.join(self._output_path, "spatial_charts", f"img_{_t}.png")
            plt.savefig(spatial_charts_path)
            plt.close()

    def make_charts(self, exclude=[]):
        custom_cmap = defaultdict()

        tree = lambda: defaultdict(tree)
        d = tree()
        m = self._markings

        for step in list(m.keys()):
            print(step)
            print(m[step])
            for net in m[step].keys():
                for place in m[step][net].keys():
                    if len(m[step][net][place].items()) == 0:
                        d[net][place][str(tk)][step] = 0
                    else:
                        for tk, n in m[step][net][place].items():
                            d[net][place][str(tk)][step] = n
                    if str(tk) not in custom_cmap:
                        custom_cmap[str(tk)] = None

        tk_count = len(custom_cmap)
        cmap = plt.cm.get_cmap('tab20')
        colors = cmap(np.linspace(0, 1, tk_count))
        for i, tk in enumerate(custom_cmap.keys()):
            custom_cmap[tk] = colors[i]

        # setting ymax
        ymax = 0
        for net in d:
            for place in d[net]:
                for i, token in enumerate(d[net][place]):
                    if not "_net" in token:
                        Y = d[net][place][token].values()
                        if max(Y) > ymax:
                            ymax = max(Y)

        for net in d:

            for place in d[net]:
                if any(e in place for e in exclude):
                    continue
                fig, ax = plt.subplots()
                plt.subplots_adjust(right=0.75)
                plt.xlabel("Simulation steps")
                plt.ylabel("Marking (black tokens)")

                ax.xaxis.set_label_position('top')
                ax.set_xlabel("(" + net + ")")
                ax.set_title("place " + place)

                for i, token in enumerate(d[net][place]):
                    if not "_net" in token:
                        X = d[net][place][token].keys()
                        Y = d[net][place][token].values()
                        ax.plot(X, Y, label=token.lstrip("_"), color=custom_cmap[token], linewidth=3)

                if self._mode == 'exploration':

                    for i, token in enumerate(d[net][place]):
                        if not "_net" in token:
                            X = d[net][place][token].keys()
                            Y = d[net][place][token].values()
                            ax.plot(X, Y, label=token.lstrip("_"), color=custom_cmap[token], linewidth=3)

                    plt.xlim(xmin=0)
                    plt.ylim(ymin=0, ymax=ymax+1)
                    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
                    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
                    ax.xaxis.set_ticks(np.arange(0, self._curr_step + 1, int(self._curr_step / 10) if self._curr_step >= 100 else self._curr_step))
                    ax.yaxis.set_ticks(np.arange(0, ymax + np.ceil(ymax / 10),
                                             1 if ymax <= 10 else 5 if ymax <= 50 else 10 if ymax <= 100 else 50))

                    fig.legend(bbox_to_anchor=(1.3, 0.3))
                    title = "place " + place + " (" + net + ")"
                    plt.savefig(os.path.join(self._output_path, title), bbox_inches="tight")
                    plt.close()

                if self._mode == 'paperFigures':

                    for i, token in enumerate(d[net][place]):
                        if not "_net" in token:
                            X = d[net][place][token].keys()
                            Y = d[net][place][token].values()
                            ax.plot(X, Y, label=token.lstrip("_"), color='g', linewidth=5)

                    plt.xlim(xmin=0)
                    plt.ylim(ymin=0, ymax=50)
                    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
                    ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
                    ax.xaxis.set_ticks(np.arange(0, self._curr_step + 1,
                                                 int(self._curr_step / 10) if self._curr_step >= 100 else self._curr_step))
                    ax.yaxis.set_ticks(np.arange(0, 50, 10))

                    fig.legend(bbox_to_anchor=(1.3, 0.3))
                    title = "place " + place + " (" + net + ")"
                    plt.savefig(os.path.join(self._output_path, title))
                    plt.close()


        print(f"Simulation results saved to {self._output_path}")
