from fileinput import filename
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python klein.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    preprocessorReturnCode = preprocess(filename)  
    sys.exit(preprocessorReturnCode)
    
def preprocess(filename):
    return subprocess.run(["gcc", "-E", "-P", filename, "-o", f"{filename}.i"], check=True).returncode

if __name__ == "__main__":
    main()
