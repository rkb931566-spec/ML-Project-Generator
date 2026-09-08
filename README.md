# ML Project Generator

🚀 A command-line tool to generate structured ML project templates with documentation and best practices.

## ✨ Features

- 🚀 Quick project setup with predefined templates
- 📚 Comprehensive documentation templates
- 🔧 Multiple ML project templates:
  - Basic ML
  - Deep Learning
  - NLP
  - Computer Vision
- 📝 Automatic docstring generation
- 📊 Example notebooks for each template
- 🧪 Pre-configured testing setup
- 🔄 Version management system
- 🚀 Automated publishing via GitHub Actions

## 📥 Installation

```bash
pip install ml-project-generator
```

## 🚀 Usage

```bash
# Create a new ML project
ml-gen my_project

# Create with a specific template
ml-gen my_project --template deep_learning

# Create with virtual environment
ml-gen my_project --venv
```

## 📁 Project Structure

```
project_root/
├── data/               # Data directory
│   ├── raw/           # Original data files
│   ├── processed/     # Processed data files
│   └── external/      # External data sources
├── models/            # Model directory
│   ├── saved/        # Saved model files
│   └── logs/         # Training logs
├── notebooks/         # Jupyter notebooks
├── src/              # Source code
│   ├── data/         # Data processing scripts
│   ├── models/       # Model implementations
│   └── utils/        # Utility functions
├── tests/            # Test files
├── config/           # Configuration files
└── docs/             # Documentation
```

## 🛠 Development

### 🔄 Version Management

The project includes a version management system to handle version updates:

```bash
# Check if versions match across files
python manage_version.py check

# Bump patch version (2.0.2 -> 2.0.3)
python manage_version.py bump-patch

# Bump minor version (2.0.3 -> 2.1.0)
python manage_version.py bump-minor

# Bump major version (2.1.0 -> 3.0.0)
python manage_version.py bump-major
```

### 🔧 CI/CD

The project uses GitHub Actions for automated publishing:

1. Create a new release tag:

   ```bash
   git tag v2.0.2  # Use the new version number
   git push origin v2.0.2
   ```

2. The workflow will automatically:
   - Check version consistency
   - Build the package
   - Run package checks
   - Publish to PyPI and TestPyPI

### ⚙️ Setup Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/AarambhaAnta/ml-project-generator.git
   cd ml-project-generator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate     # On Windows
   ```

3. Install development dependencies:

   ```bash
   pip install -e ".[dev]"
   ```

4. Run tests:
   ```bash
   python -m pytest
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Generated using [ml-project-generator](https://github.com/AarambhaAnta/ml-project-generator)
- Inspired by best practices in ML project organization

---

Made with ❤️ by [@AarambhaAnta](https://github.com/AarambhaAnta)
