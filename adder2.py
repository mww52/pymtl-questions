from pymtl import * 

class adder2(Model):

  def __init__(s,nbits):
    s.in1 = InPort(nbits)
    s.in2 = InPort(nbits)
    s.out = OutPort(nbits)
    #s.C = OutPort(1)
    #s.V = OutPort(1)

    @s.combinational
    def block1():
      s.out.value= s.in1 + s.in2 
    

