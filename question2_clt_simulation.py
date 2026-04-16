import random
import matplotlib.pyplot as plt

def get_single_sample_mean(n):
    total_sum = 0
    for _ in range(n):
        roll = random.randint(1, 6)
        total_sum += roll
    sample_mean = total_sum / n
    return sample_mean

def simulate_clt_experiment(sample_size_n, num_samples, position_in_grid, graph_title):
    collection_of_means = []
    
    for _ in range(num_samples):
        current_mean = get_single_sample_mean(sample_size_n)
        collection_of_means.append(current_mean)
        
    plt.subplot(position_in_grid)
    plt.hist(collection_of_means, bins=30, color='mediumpurple', edgecolor='black', density=True)
    plt.title(graph_title)
    plt.xlabel(f'Sample Mean (Avg of {sample_size_n} rolls)')
    plt.ylabel('Frequency Density')

def main():
    n = 10 
    plt.figure(figsize=(15, 5))
    
    simulate_clt_experiment(n, 50, 131, '50 Samples')
    simulate_clt_experiment(n, 500, 132, '500 Samples')
    simulate_clt_experiment(n, 5000, 133, '5000 Samples')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
