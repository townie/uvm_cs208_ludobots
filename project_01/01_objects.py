import sys
sys.path.insert(0, '../..')
import pyrosim

sim = pyrosim.Simulator(eval_time=300, play_paused=True)

whiteObject = sim.send_cylinder( x=0 , y=0 , z=0.6 , length=1.0 , radius=0.1 )

#2e
# redObject = sim.send_cylinder( x= -0.2, y=0 , z=0.6,  r=1, g=0, b=0, r1=0, r2=1, r3=0 )


#2f
redObject = sim.send_cylinder( x=0, y=0.5 , z=1.1,  r=1, g=0, b=0, r1=0, r2=1, r3=0 )



sim.start()


sim.wait_to_finish()
