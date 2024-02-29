from qiskit import *
qr= QuantumRegister(2)
cr=ClassicalRegister(2)
circuit=QuantumCircuit(qr,cr)
circuit.draw()
circuit.h(gr[0])
 circuit.draw(output='mpl') #SHOWS GRAPHICAL OUTPUT 
circuit.measure(qr,cr)
### To Simulate on local device we use "Aer Simulator"
simulator= Aer.get_backend('qasm_simulator')## QUANTUM ASSEMBLY LANGUAGE
### To execute the simulator
execute(circuit,backend=simulator)
result= execute(circuit,backend=simulator).result()
### To view 
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))

### TO USE A REAL QUANTUM RUN_TIME
IBMQ.load_account()
provider=IBMQ.get_provider('ibm-q')
qcomp=provider.get_backend('')
job= execute(circuit,backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
result= job.result()
plot_histogram(result.get_counts(circuit))
