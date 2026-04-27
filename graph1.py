import matplotlib.pyplot as plt

# AES throughput data (in KB/s from openssl speed output)
block_sizes = [16, 64, 256, 1024, 8192]

aes128_throughput = [248982.36, 234904.52, 239103.59, 238349.41, 237946.72]
aes192_throughput = [222036.35, 202883.05, 204949.68, 205786.72, 205876.51]
aes256_throughput = [187859.45, 175475.59, 175035.27, 175181.54, 178096.09]

# Convert to MB/s for readability
aes128_throughput = [x / 1024 for x in aes128_throughput]
aes192_throughput = [x / 1024 for x in aes192_throughput]
aes256_throughput = [x / 1024 for x in aes256_throughput]

# Graph 1: AES throughput vs block size
plt.figure(figsize=(10, 6))
plt.plot(block_sizes, aes128_throughput, marker='o', linewidth=2, label='AES-128-CBC')
plt.plot(block_sizes, aes192_throughput, marker='s', linewidth=2, label='AES-192-CBC')
plt.plot(block_sizes, aes256_throughput, marker='^', linewidth=2, label='AES-256-CBC')

plt.xlabel('Block Size (bytes)', fontsize=12)
plt.ylabel('Throughput (MB/s)', fontsize=12)
plt.title('AES Throughput vs Block Size', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xscale('log')

plt.tight_layout()
plt.savefig('aes_throughput.png', dpi=300)
print("AES graph saved as 'aes_throughput.png'")
plt.show()