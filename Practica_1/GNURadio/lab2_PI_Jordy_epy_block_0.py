import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Acumulador_memoria',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

        # Memoria: permite continuidad entre llamadas a work()
        # (Patrón del libro: acum_anterior + cumsum y guardar el último valor)
        self.acum_anterior = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]      # entrada
        y0 = output_items[0]    # salida
        N = len(x)

        acumulado = self.acum_anterior + np.cumsum(x)
        self.acum_anterior = acumulado[N - 1]
        y0[:] = acumulado

        return len(x)
