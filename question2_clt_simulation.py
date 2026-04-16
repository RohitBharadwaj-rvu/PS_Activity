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
    # Using dynamic bins depending on sample size makes the shape clearer
    plt.hist(collection_of_means, bins=30, color='mediumpurple', edgecolor='black', density=True)
    plt.title(graph_title)
    plt.xlabel(f'Sample Mean (Avg of {sample_size_n} rolls)')
    plt.ylabel('Frequency Density')

def main():
    # Keep the number of experiments high and constant so we get a smooth picture
    num_experiments = 5000 
    plt.figure(figsize=(15, 5))
    
    # We change 'n' (Sample Size) to correctly demonstrate the Central Limit Theorem
    simulate_clt_experiment(1, num_experiments, 131, 'Sample Size (n) = 1')
    simulate_clt_experiment(5, num_experiments, 132, 'Sample Size (n) = 5')
    simulate_clt_experiment(50, num_experiments, 133, 'Sample Size (n) = 50')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
