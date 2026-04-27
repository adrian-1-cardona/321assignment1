import matplotlib.pyplot as plt

# RSA performance data (operations per second from openssl speed output)
rsa_keysizes = [2048, 4096]

# Sign operations per second
rsa_sign_ops = [418.5, 77.8]

# Verify operations per second
rsa_verify_ops = [32277.0, 8483.6]

# Graph 2: RSA operations per second vs key size
plt.figure(figsize=(10, 6))
plt.plot(rsa_keysizes, rsa_sign_ops, marker='o', linewidth=2, markersize=8, label='RSA Sign')
plt.plot(rsa_keysizes, rsa_verify_ops, marker='s', linewidth=2, markersize=8, label='RSA Verify')

plt.xlabel('RSA Key Size (bits)', fontsize=12)
plt.ylabel('Operations per Second', fontsize=12)
plt.title('RSA Performance vs Key Size', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.yscale('log')

plt.tight_layout()
plt.savefig('rsa_throughput.png', dpi=300)
print("RSA graph saved as 'rsa_throughput.png'")
plt.show()
