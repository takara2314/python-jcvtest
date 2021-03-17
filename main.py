import subprocess

def get_lines():
    cp = subprocess.Popen(
        "JCVtest.exe",
        shell=True,
        stdout=subprocess.PIPE
    )

    result_output = False

    while True:
        output = cp.stdout.readline()
        line = output.decode("utf-8")

        if line.startswith("-----"):
            result_output = not result_output
            continue

        if line and result_output:
            yield line.replace("\n", "")
        if not line and cp.poll() is not None:
            break

for line in get_lines():
    if line.startswith("face->faceAttribute.age:"):
        print("あなたの推定年齢は{}歳です！".format(line[25:27]))