from pymtl import * 
from pclib.rtl.regs import Reg, RegRst

class version2 (Model):
  def __init__(s,nbits=8):
    s.in_ = InPort(nbits)
    s.out = OutPort(nbits)
    s.Reg1 = Reg(nbits)
    s.connect(s.in_,s.Reg1.in_)
    s.connect(s.Reg1.out,s.out)