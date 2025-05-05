import json

def parse_and_print_json(file_path):
    try:
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Print header
        print("="*80)
        print(f"Loaded {len(data)} Verilog modules with analysis")
        print("="*80)
        
        # Iterate through each module
        for i, module in enumerate(data, 1):
            print(f"\nModule {i}:")
            print("-"*40)
            
            # Print the question (Verilog code)
            print("Verilog Code:")
            print(module['question'])
            
            # Print the answer (analysis) in the new format
            print("\nAnalysis:")
            answer = module['answer']
            print(f"Performance: {answer.get('Performance', 'N/A')}")
            print(f"Power: {answer.get('Power', 'N/A')}")
            print(f"Area: {answer.get('Area', 'N/A')}")
            
            print("-"*40)
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace with your actual JSON file path
    json_file_path = "verilog1_10.json"
    parse_and_print_json(json_file_path)