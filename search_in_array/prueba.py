import data_generator

def take_times(size, samples_by_size):
    samples = []
    targets = []
    for _ in range(samples_by_size):
        samples.append(data_generator.random_list(size))
        #agregar condicion para que el target esté dentro del array generado
        targets.append(data_generator.gen_target(samples[-1]))
    return targets            

print(take_times(1000, 5))
                    