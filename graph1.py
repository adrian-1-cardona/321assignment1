import matplotlib.pyplot as plt

# AES-128 modes throughput data (in KB/s from openssl speed -evp output)
block_sizes = [16, 64, 256, 1024, 8192]

aes_ecb = [256699.50, 294207.74, 294589.36, 297132.91, 306740.92]
aes_cfb = [240274.26, 242859.65, 243443.24, 242640.33, 242334.86]
aes_ofb = [254785.45, 253319.12, 253191.83, 253853.47, 253905.87]
aes_ctr = [272991.96, 289798.95, 293148.44, 294976.22, 295912.86]
aes_cbc = [246618.64, 240186.86, 243505.76, 242802.61, 243982.14]

# Convert KB/s to MB/s
aes_ecb = [x / 1024 for x in aes_ecb]
aes_cfb = [x / 1024 for x in aes_cfb]
aes_ofb = [x / 1024 for x in aes_ofb]
aes_ctr = [x / 1024 for x in aes_ctr]
aes_cbc = [x / 1024 for x in aes_cbc]

# Graph
plt.figure(figsize=(12, 7))
plt.plot(block_sizes, aes_ecb, marker='o', linewidth=2.5, markersize=7, label='AES-128-ECB')
plt.plot(block_sizes, aes_ctr, marker='s', linewidth=2.5, markersize=7, label='AES-128-CTR')
plt.plot(block_sizes, aes_ofb, marker='^', linewidth=2.5, markersize=7, label='AES-128-OFB')
plt.plot(block_sizes, aes_cbc, marker='d', linewidth=2.5, markersize=7, label='AES-128-CBC')
plt.plot(block_sizes, aes_cfb, marker='x', linewidth=2.5, markersize=7, label='AES-128-CFB')

plt.xlabel('Block Size (bytes)', fontsize=12, fontweight='bold')
plt.ylabel('Throughput (MB/s)', fontsize=12, fontweight='bold')
plt.title('AES-128 Throughput: Block Size vs Mode', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='best')
plt.grid(True, alpha=0.3)
plt.xscale('log')

plt.tight_layout()
plt.savefig('aes_throughput.png', dpi=300)
print("AES graph saved as 'aes_throughput.png'")
plt.show()