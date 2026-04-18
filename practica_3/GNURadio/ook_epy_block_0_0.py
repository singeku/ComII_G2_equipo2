import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is an EC VCO and works as following: It generates the complex envelope equivalent of the modulated signal. 
    - Top input: Determines the magnitude of the complex envelope. 
    - Bottom input: Determines the phase of the complex envelope. 
    - Output: The baseband complex signal, represented by its In-phase (I) and Quadrature (Q) components. 
    Recommendation: Useful for computationally efficient simulations since it doesn't require simulating the high-frequency carrier."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])

