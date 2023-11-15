import cmath

def structure_factor(h, k, l):
    
    term1 = cmath.exp(cmath.pi * 1j * (h + k))
    term2 = cmath.exp(cmath.pi * 1j * (h + l))
    term3 = cmath.exp(cmath.pi * 1j * (k + l))
    
    return (1 + term1 + term2 + term3)

if __name__ == "__main__":
    # Edit the values in this list to change h, k, and l
    hkl_values = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (0,0,0), (2,2,2)]
    
    for h, k, l in hkl_values:
        S_hkl = structure_factor(h, k, l)
        print(f"S({h}{k}{l}) = {S_hkl.real:.2f} + {S_hkl.imag:.2f}i")
