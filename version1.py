from pymtl import * 
from pclib.rtl.regs import Reg, RegRst

class version1 (Model):
  def __init__(s,nbits=8):
    s.in_ = InPort(nbits)
    s.out = OutPort(nbits)
    s.connect(s.in_,s.out)