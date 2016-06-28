from pymtl import * 
from pclib.rtl.regs import Reg, RegRst
from adder2 import adder2 

class final(Model):
  def __init__(s,nbits=8):
    s.in1 = InPort(nbits)
    s.in2 = InPort(nbits)

    s.out = OutPort(nbits)
    
    s.reg1 = Reg(nbits)
    s.reg2 = Reg(nbits)


    s.connect(s.in1,s.reg1.in_)

    s.connect(s.in2,s.reg2.in_)

    s.adder10 = adder2(nbits)

    s.connect(s.adder10.in1,s.reg1.out)
    s.connect(s.adder10.in2,s.reg2.out)

    s.connect(s.adder10.out,s.out)
