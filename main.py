import os
import traceback
from siteforge.config import load_config
from siteforge.generator import generate_site

def main():
    try:
        config = load_config()
        generate_site(config)
        print("Site generated successfully!")
    except Exception as e:
        print(f"An error occurred while generating the site: {str(e)}")
        print("Traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    main()