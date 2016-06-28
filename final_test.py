from pymtl import * 
from final import final

def test_basic():
	model = final()
	model.elaborate()

	sim = SimulationTool(model)
	sim.reset()

	def t(in1,in2,out):
		model.in2 = in1
		model.in2 = in2
		sim.eval_combinational()
		sim.print_line_trace()
		if (out!='?'):
			assert model.out==out
		sim.cycle()
	t(0x03,0x05,'?')
	t(0x01,0x02,0x08)
	t(0x02,0x03,0x03)




