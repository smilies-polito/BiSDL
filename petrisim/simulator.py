import errno
import os
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# TODO controlli!
class Simulator:
    def __init__(self, m, steps=None, firing_prob=0.6, output_path=".", draw_nets=False):
        self._module = m
        self._steps = steps
        self._curr_step = 0
        # self._stimuli = self._read_stimuli(stimuli)
        self._firing_prob = firing_prob
        self._output_path = output_path
        self._draw_nets = draw_nets
        self._markings = {}
        if not os.path.exists(self._output_path):
            os.mkdir(self._output_path)

    # TODO sistemare il marking iniziale
    # TODO livello di output (quiet, verbose, debug), tipi di output (csv e/o img)
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
                    for tk, n in m[step][net][place].items():
                        d[net][place][str(tk)][step] = n
                        if str(tk) not in custom_cmap:
                            custom_cmap[str(tk)] = None

        tk_count = len(custom_cmap)
        cmap = plt.cm.get_cmap('viridis')
        colors = cmap(np.linspace(0, 1, tk_count))
        for i, tk in enumerate(sorted(custom_cmap.keys())):
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
                plt.xlabel("simulation step")
                plt.ylabel("# tokens")
                title = "place " + place + " (" + net + ")"
                plt.title(title)


                for i, token in enumerate(d[net][place]):
                    if not "_net" in token:
                        X = d[net][place][token].keys()
                        Y = d[net][place][token].values()
                        ax.plot(X, Y, label=token.lstrip("_"), color=custom_cmap[token])


                plt.xlim(xmin=0)
                plt.ylim(ymin=0, ymax=ymax+1)
                ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
                ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
                ax.xaxis.set_ticks(np.arange(0, self._curr_step + 1, int(self._curr_step / 10) if self._curr_step >= 100 else self._curr_step))
                ax.yaxis.set_ticks(np.arange(0, ymax + np.ceil(ymax / 10),
                                             1 if ymax <= 10 else 5 if ymax <= 50 else 10 if ymax <= 100 else 50))

                #ax.yaxis.set_ticks(np.arange(0, 16,
                                              #1 if ymax <= 10 else 5 if ymax <= 50 else 10 if ymax <= 100 else 50))

                # plt.show()
                fig.legend(bbox_to_anchor=(1.2 , 0.3))
                plt.savefig(os.path.join(self._output_path, title), bbox_inches="tight")
                plt.close()
        print(f"Simulation results saved to {self._output_path}")
