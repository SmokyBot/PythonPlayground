import networkx as nx

original_graph = nx.Graph()
#Initialize your graph here

# Define method which runs a single iteration
def run_iteration(name, graph):
    pass #Do whatever you want to do within the iteration here

# Run iterations in multithreaded processing mode to utilize all cpu cores.
threads = []
for index in range(0, 1000):
    # For all n 1...iterations create a new "thread" to execute the iteration with a copy of the original_graph
    thread = threading.Thread(target=run_iteration, args=("Iteration: " + str((index + 1)), original_graph.copy()))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # "Join" all threads - means we wait for all the threads to finish before continuing processing next line
