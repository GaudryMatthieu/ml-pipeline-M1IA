import yaml, subprocess, sys

def run_pipeline(yaml_file):
    with open(yaml_file, 'r') as file:
        pipeline = yaml.safe_load(file)

    for step in pipeline['steps']:
        print(f"[ {step['name'].upper()} ] ...", end=" ", flush=True)
        result = subprocess.run(step['run'], shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("OK")
        else:
            print("FAILED")
            print(result.stderr)
            sys.exit(1)
    print("[ PIPELINE ] SUCCESS")

if __name__ == "__main__":
    run_pipeline('pipeline.yml')