# adhoc testing case

from pymtl import * 
from version2 import version2 
from pclib.rtl.regs import Reg, RegRst

def test_basic():
	model = version2()
	model.elaborate()
	sim = SimulationTool(model)
	sim.reset()
	
	def t(in_,out):
		model.in_ = in_
		sim.eval_combinational()
		sim.print_line_trace()
		if ((out!='?')):
			assert model.out==out
		sim.cycle()
	t(0x04,0x04)
	t(0x05,0x05)


