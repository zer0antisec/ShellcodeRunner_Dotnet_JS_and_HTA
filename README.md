# DotNetToJScript HTA Shellcode Runner Generator

This toolchain generates an HTA file that executes shellcode by leveraging a series of steps, including XOR encryption, creating a C# shellcode runner, and compiling it into a `.dll` with DotNetToJScript. The final `.hta` file contains the necessary code to run the shellcode through a browser or local HTML environment.

## 🔑 Key Features:
- 🔐 **XOR Shellcode Encryption**: Encrypts your shellcode using XOR with a randomly generated key.
- ⚙️ **C# Shellcode Runner Generation**: Generates a C# class that decrypts and runs the shellcode in memory.
- 💻 **DotNetToJScript Compilation**: Uses `DotNetToJScript` to compile the C# file into a JScript file for execution.
- 🌐 **HTA File Generation**: Automatically creates an `.hta` file containing the JScript needed to run the shellcode.

## 📝 Workflow

### Step 1: Generate the C# Shellcode Runner
This step reads a raw `.bin` shellcode file, encrypts it with XOR, and generates a C# shellcode runner in the file `ExampleAssembly.cs`.

#### Usage:
```bash
python3 dotnetshellcode_generator.py <shellcode.bin>
```
Example:
``` bash
python3 dotnetshellcode_generator.py shellcode.bin
```
This will generate the ExampleAssembly.cs file, which contains the XOR-encrypted shellcode and the decryption logic in C#.

### Step 2: Compile to JScript
Compile the generated C# file into a JScript file using DotNetToJScript.

### Usage:
```bash
DotNetToJScript.exe ExampleAssembly.dll --lang=Jscript --ver=v4 -c TestClass -o shellcoderunner.js
```
This command compiles ExampleAssembly.dll into shellcoderunner.js, which can be used as part of the next step.

### Step 3: Generate the HTA File
The final step involves generating the HTA file that contains the JScript code. The .hta file will execute the shellcode on the target machine.

Usage:
```bash
python3 generate_hta.py <input.js> <output.hta>
```
Example:
```bash
python3 generate_hta.py shellcoderunner.js shellcoderunner.hta
```
This will generate shellcoderunner.hta, which can be run to execute the encrypted shellcode through JScript in a browser or local environment.

⚠️ Disclaimer
This project is intended for educational and research purposes only. Use responsibly and only in environments where you have explicit permission to test or assess.
