from scipy.constants import physical_constants as pc

if __name__ == '__main__':
    for key, value in pc.items():
        print(f"{key} -> {value}")
