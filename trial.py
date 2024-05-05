import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
def count_digits(number):
   
    number_str = str(number)
    
    
    return len(number_str)




def quantum_random_number(bits):
    
    circuit = QuantumCircuit(bits, bits)
    
   
    for i in range(bits):
        circuit.h(i)
    

    circuit.measure(range(bits), range(bits))
    
   
    simulator = Aer.get_backend('qasm_simulator')
    

    transpiled_circuit = transpile(circuit, simulator)
    
   
    qobj = assemble(transpiled_circuit)
    

    result = simulator.run(qobj).result()
    

    counts = result.get_counts(circuit)
    
    binary_string = max(counts, key=counts.get)
    
    random_number = int(binary_string, 2)
    
    return random_number%1000000

def out():
    random_number = quantum_random_number(20)
    out_number=str(random_number)
    while len(out_number)<6:
        out_number='0'+out_number
    return out_number
