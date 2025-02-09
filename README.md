# ML Project Template

This repository provides a standardized template for structuring machine learning projects, covering data pipelines, model training, deployment, and version control. It includes a configurable YAML file (`project_config.yaml`) for defining project components, Python scripts for automated project generation, and best practices for reproducibility.

## Getting Started

`Two sample yaml file have been ran to create the examples below:
1. [gcp_data_processing](gcp_data_processing)
2. [MyMLProject](MyMLProject)
`

### Installation

1. **Clone the repository:**
   ```Bash
   git clone [https://github.com/BodieCoding/ml-project-template.git](https://github.com/BodieCoding/ml-project-template.git)
   cd ml-project-template
   ```
3. **Run the setup script:**
   ```Bash
   setup_and_create.bat  # On Windows
   ./setup_and_create.sh   # On Linux/macOS (create this script if needed)
   ```

## This script automates the following:
  
* Virtual environment creation (if it doesn't exist).
* Installation of required Python packages for the template generator.
* Project structure generation based on project_config.yaml using create_project.py.
* Configuration (project_config.yaml)
* The project_config.yaml file is the central configuration file for this template. It allows customization of project structure and dependencies.  The settings in this file directly influence the generated project structure and its capabilities.

``` YAML

name: MyMLProject  # The name of your project (used for directory creation)
version: 0.1.0      # The initial version of your project

components:
  data:             # Define the 'data' component
    subfolders: ["raw", "processed", "interim"] # Subdirectories within 'data'
    dependencies: ["pandas", "numpy"]          # Python packages for 'data'
    schema: "v1.0"                             # Version of the data schema
  training:         # Define the 'training' component
    subfolders: ["models", "metrics", "logs"]   # Subdirectories within 'training'
    dependencies: ["scikit-learn", "tensorflow"] # Python packages for 'training'
    model_version: "v1.0"                      # Initial model version
    docker_image: "your-registry/training-image:v1.0" # Docker image for training
  # ... other components (evaluation, src, tests, scripts, notebooks, etc.)
  .dockerignore:   # Files to exclude from Docker builds
    files: [".git", "__pycache__", "*.pyc"]
  .gitignore:      # Files to exclude from Git version control
    files: [".git", "__pycache__", "*.pyc", "data/*"]  # Example: exclude the entire data directory

metadata_store: "project_metadata.json"  # Name of the file to store metadata
```

**Configuration Options and Their Effects:**

*   `name`: Determines the name of the root project directory.
*   `version`: Specifies the initial project version (tracked in `project_metadata.json`).
*   `components`: Defines the core components of the project.
    *   `subfolders`: Creates subdirectories within components.  *(Indentation is essential here)*
    *   `dependencies`: Lists required Python packages (added to `requirements.txt`). *(Indentation is essential here)*
    *   Component-specific metadata (e.g., `schema`, `model_version`, `docker_image`): Allows associating metadata with components (stored in `project_metadata.json`). *(Indentation is essential here)*
*   `.dockerignore` and `.gitignore`: Lists files/directories to exclude from Docker builds and Git.
*   `metadata_store`: Defines the name of the project metadata file.

## Project Structure
After running the setup script, the generated project directory will mirror the structure defined in project_config.yaml.  For the example configuration above, the structure will be:
```
MyMLProject/             # Main project directory (named after config)
├── data/
│   ├── raw/
│   ├── processed/
│   └── interim/
├── training/
│   ├── models/
│   ├── metrics/
│   └── logs/
├── evaluation/
├── src/
├── tests/
├── scripts/
├── notebooks/
├── .dockerignore
├── .gitignore
├── requirements.txt      # Project dependencies
└── project_metadata.json # Project metadata (versions, etc.)
```

## Usage
### Customize project_config.yaml:  
Modify the configuration file to reflect your project's specific requirements.

### Regenerate the project (if needed): 
If you make changes to project_config.yaml after the initial setup, rerun the setup script to update the project structure accordingly.

### Develop your ML project: 
Begin development within the organized project structure.

## Updating Metadata:
The update_metadata.py script (or its integrated functionality) can be used to update the project metadata (e.g., model versions) programmatically after training or evaluation.

``` Python

# Example: Update the model version in your training script
from create_project import update_metadata

update_metadata("MyMLProject", "training", "model_version", "v1.1")
```
---
# [Governance Docs](Docs/governance.md)
# [Security Policy](Docs/SECURITY.md)
