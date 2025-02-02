# QRNG

This project implements a Quantum Random Number Generator (QRNG) using Qiskit and IBM’s QASM Simulator. The randomness is derived from quantum superposition, ensuring a truly unpredictable sequence of numbers.

How It Works
	1.	A quantum circuit is created with a given number of qubits.
	2.	Hadamard gates are applied to each qubit, putting them into a superposition state.
	3.	The qubits are then measured, collapsing them into a random binary string.
	4.	The binary string is converted into a decimal number.
	5.	The number is then modulo 1,000,000, ensuring a six-digit random number.
	6.	If the number is less than six digits, it is padded with leading zeros.

Code Explanation

1. Quantum Circuit Creation
	•	A quantum circuit with bits qubits and classical bits is created.
	•	Each qubit is initialized into a superposition state using Hadamard (H) gates.

2. Measurement and Simulation
	•	The qubits are measured, producing a random binary string.
	•	The QASM Simulator is used to execute the quantum circuit.
	•	The measurement result with the highest count is selected as the output.

3. Random Number Generation
	•	The binary string is converted to a decimal number.
	•	The result is taken modulo 1,000,000 to ensure a six-digit number.
	•	Leading zeros are added if the number has fewer than six digits.

Dependencies

To run this project, you need:
	•	Python 3
	•	Qiskit (pip install qiskit)
	•	NumPy (pip install numpy)

Usage

Run the script to generate a truly random six-digit number:

random_number = out()
print("Quantum Random Number:", random_number)


Future Improvements
	•	Implement real hardware execution on IBM Quantum devices.
	•	Extend support for larger random number generation.
	•	Enhance performance with optimized circuit transpilation.