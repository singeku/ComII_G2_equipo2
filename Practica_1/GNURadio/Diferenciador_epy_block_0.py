import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Diferenciador discreto: y[n] = x[n] - x[n-1]"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='diferenciador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.x_prev = np.float32(0.0)

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]

        # Diferenciación discreta
        # y[0] usa el valor anterior almacenado
        y[0] = x[0] - self.x_prev

        # Para el resto de muestras:
        y[1:] = x[1:] - x[:-1]

        # Actualiza memoria para la próxima llamada
        self.x_prev = x[-1]

        return len(y)
