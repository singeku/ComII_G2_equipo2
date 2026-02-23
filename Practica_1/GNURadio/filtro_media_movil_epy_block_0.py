"""
Embedded Python Blocks
Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, N=10):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='filtro de media movil',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.N = N
        self.buffer = np.zeros(N)

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        in_sig = input_items[0]
        out_sig = output_items[0]

        for i in range(len(in_sig)):
            self.buffer = np.roll(self.buffer, -1)
            self.buffer[-1] = in_sig[i]

            out_sig[i] = np.mean(self.buffer)

        return len(output_items[0])
