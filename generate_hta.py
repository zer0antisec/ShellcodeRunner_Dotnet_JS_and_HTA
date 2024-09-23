import sys

def create_hta_file(jscript_content, output_file):
    hta_template = f"""<!DOCTYPE html>
<html>
<head>
    <title>Shellcode Runner</title>
    <hta:application id="shellcodeRunner" border="thin" borderstyle="normal" sysmenu="yes" caption="yes" />
    <script language="JScript">
        {jscript_content}
    </script>
</head>
<body>
</body>
</html>
"""
    with open(output_file, 'w') as f:
        f.write(hta_template)

def main(jscript_file, output_hta):
    with open(jscript_file, 'r') as f:
        jscript_content = f.read()

    create_hta_file(jscript_content, output_hta)
    print(f"Generated {output_hta} from {jscript_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.js> <output.hta>")
        sys.exit(1)

    jscript_file = sys.argv[1]
    output_hta = sys.argv[2]

    main(jscript_file, output_hta)
