import matplotlib.pyplot as plt

# RSA key sizes and operations per second from openssl speed output
rsa_keysizes = [1024, 2048, 4096]

# Sign operations per second
rsa_sign_ops = [1738.3, 418.5, 77.9]

# Verify operations per second
rsa_verify_ops = [101227.1, 32258.9, 8486.4]

# Graph
plt.figure(figsize=(10, 6))
plt.plot(rsa_keysizes, rsa_sign_ops, marker='o', linewidth=2.5, markersize=8, label='RSA Sign')
plt.plot(rsa_keysizes, rsa_verify_ops, marker='s', linewidth=2.5, markersize=8, label='RSA Verify')

plt.xlabel('RSA Key Size (bits)', fontsize=12, fontweight='bold')
plt.ylabel('Operations per Second', fontsize=12, fontweight='bold')
plt.title('RSA Performance vs Key Size', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.yscale('log')

plt.tight_layout()
plt.savefig('rsa_throughput.png', dpi=300)
print("RSA graph saved as 'rsa_throughput.png'")
plt.show()
