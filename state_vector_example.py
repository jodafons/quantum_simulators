
from state_vector.simulator import Qstate


# constructing an EPR pair
s = Qstate(2) # create a 2-qubit state
#s.hadamard(0) # hadamard on first qubit
s.cnot(0) # CNOT the two qubits


print(s.state)

