import os
import yaml
import shutil
import json
import argparse
from datetime import datetime

def create_project(config_file, project_name=None):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    if project_name is None:
        project_name = config['name']
    project_dir = os.path.join(os.getcwd(), project_name)

    if os.path.exists(project_dir):
        print(f"Project '{project_name}' already exists!")
        return

    os.makedirs(project_dir)

    metadata = {
        "name": config['name'],
        "version": config['version'],
        "created_at": datetime.now().isoformat(),
        "components": {}
    }

    for component, details in config['components'].items():
        component_dir = os.path.join(project_dir, component)
        os.makedirs(component_dir)

        metadata["components"][component] = {}

        if 'subfolders' in details:
            for subfolder in details['subfolders']:
                os.makedirs(os.path.join(component_dir, subfolder))

        if 'files' in details:
            for file in details['files']:
                file_path = os.path.join(component_dir, file)
                open(file_path, 'w').close()

        if 'dependencies' in details:
            req_file_path = os.path.join(project_dir, 'requirements.txt')
            with open(req_file_path, 'a') as req_file:
                for dep in details['dependencies']:
                    req_file.write(f"{dep}\n")

        # Dynamically add metadata
        for key, value in details.items():
            if value is not None:
                metadata["components"][component][key] = value

    # Create .dockerignore and .gitignore
    for file_name in ['.dockerignore', '.gitignore']:
        if file_name in config['components']:
            file_path = os.path.join(project_dir, file_name)
            with open(file_path, 'w') as f:
                for file in config['components'][file_name]['files']:
                    f.write(f"{file}\n")

    # Save Metadata
    metadata_file = os.path.join(project_dir, config['metadata_store'])
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)

    print(f"Project '{project_name}' created successfully in '{project_dir}'!")


def update_metadata(project_dir, component, key, value):
    metadata_file = os.path.join(project_dir, "project_metadata.json")
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)

    metadata["components"][component][key] = value

    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create ML project template.")
    parser.add_argument("-c", "--config", default="project_config.yaml", help="Path to YAML config file.")
    parser.add_argument("-n", "--name", help="Project name (optional).")
    args = parser.parse_args()

    create_project(args.config, args.name)

    # Example: Update model version after training (in your training script)
    # update_metadata("MyMLProject", "training", "model_version", "v1.3")