import os
import yaml
import argparse
from functional_tester import FunctionalWebTester

def load_config(config_file: str) -> dict:
    """Load configuration from a YAML file."""
    with open(config_file, "r") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(
        description="Functional Web Testing with Dependency Injection using Python"
    )
    parser.add_argument(
        "--config",
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")),
        help="Path to the YAML configuration file"
    )
    args = parser.parse_args()

    config = load_config(args.config)
    url = config.get("url", "https://www.google.com") 
    query = config.get("query", "OpenAI")

    tester = FunctionalWebTester(url=url)  
    test_passed = tester.run(query)
    
    if test_passed:
        print("Test passed: Search results found.")
    else:
        print("Test failed: No search results found.")

if __name__ == "__main__":
    main()
