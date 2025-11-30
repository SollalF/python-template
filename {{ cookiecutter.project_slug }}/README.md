# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Usage

This is a Cookiecutter template. To use it:

1. Install cookiecutter:
   ```bash
   pip install cookiecutter
   ```

2. Generate a new project from this template:
   ```bash
   cookiecutter <path-to-this-template>
   ```

   Or if this template is in a git repository:
   ```bash
   cookiecutter <git-repo-url>
   ```

3. Follow the prompts to customize your project:
   - `project_name`: Human-readable project name
   - `package_name`: Python package name (should match project_name with hyphens/spaces replaced by underscores, e.g., "my-project" → "my_project")
   - `description`: Project description
   - `version`: Initial version
  - `author_name`: Author name
  - `author_email`: Author email
  - `python_version`: Python version (default: 3.12, minimum: 3.12)

## Development

After generating your project:

1. Initialize the project:
   ```bash
   just init
   ```

2. Run checks:
   ```bash
   just check
   ```

3. Run tests:
   ```bash
   just test
   ```

## Project Structure

```
{{ cookiecutter.project_name }}/
├── src/
│   └── {{ cookiecutter.package_name }}/
│       ├── __init__.py
│       ├── main.py
│       └── settings.py
├── tests/
│   └── test_settings.py
├── pyproject.toml
├── justfile
└── README.md
```

