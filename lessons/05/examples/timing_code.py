from timeit import default_timer as timer

start = timer()

its = 100000000
while its > 0:
    a = 1

end = timer()

print(f"Finished in {end - start:.10f} seconds")
