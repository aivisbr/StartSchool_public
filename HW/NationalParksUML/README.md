# Park Management System - UML Class Diagram

## Project Files

- **`uml_description.md`** - Detailed description of the UML class diagram, including all classes, attributes, methods, and relationships
- **`park_management_system.png`** - Visual UML class diagram image
- **`uml_example.py`** - Python source code containing all class definitions
- **`README.md`** - This file

## About This Project

This project contains a UML class diagram for a Park Management System. The diagram was automatically generated from the Python code in `uml_example.py` using the `pyreverse` tool.

The system models:
- Multiple parks with lodges and rangers
- User hierarchy (Visitors and Rangers)
- Entry permits (Tickets and Annual Passes)
- Relationships between all entities

## How to Generate the UML Diagram

Follow these steps to regenerate the UML class diagram from the Python code:

### Step 1: Install Python Packages
```bash
pip install pylint graphviz
```

**Note:** The `graphviz` Python package is just a wrapper - you still need to install the actual Graphviz software (see Step 2).

### Step 2: Install Graphviz Software

1. Download Graphviz from: https://graphviz.org/download/
2. Download the ZIP file for your operating system
3. Extract the ZIP file to a location on your computer (e.g., `C:\Program Files\Graphviz`)

### Step 3: Add Graphviz to System PATH

#### Windows:
1. Locate where you extracted Graphviz (e.g., `C:\Program Files\Graphviz`)
2. Find the `bin` folder inside (e.g., `C:\Program Files\Graphviz\bin`)
3. Add to PATH:
   - Press `Win + X` → **System**
   - Click **Advanced system settings**
   - Click **Environment Variables**
   - Under **System variables**, find and select **Path**
   - Click **Edit**
   - Click **New**
   - Add the path to Graphviz `bin` folder: `C:\Program Files\Graphviz\bin`
   - Click **OK** on all dialogs
4. **Restart your terminal/command prompt** for changes to take effect

#### macOS:
```bash
# Using Homebrew
brew install graphviz
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt-get install graphviz
```

### Step 4: Verify Graphviz Installation
```bash
dot -V
```

You should see output like: `dot - graphviz version X.XX.X`

### Step 5: Generate the UML Diagram

Navigate to the directory containing `uml_example.py` and run:
```bash
pyreverse -o png uml_example.py
```

This will generate:
- `classes.png` - Class diagram showing all classes and their relationships
- `packages.png` - Package diagram (if applicable)

You can rename `classes.png` to `park_management_system.png` if desired.

## Other Output Formats

You can generate the diagram in different formats:
```bash
# PNG format (default)
pyreverse -o png uml_example.py

# PDF format
pyreverse -o pdf uml_example.py

# SVG format
pyreverse -o svg uml_example.py

# DOT format (text-based)
pyreverse -o dot uml_example.py

# PlantUML format (text-based)
pyreverse -o puml uml_example.py
```

## Understanding the Diagram

For a complete explanation of the UML class diagram, including:
- Class descriptions
- Attribute definitions
- Method signatures
- Relationship types
- Design patterns used

Please refer to **`uml_description.md`**.

### Additional resources
- [UML Class Diagram](https://www.geeksforgeeks.org/system-design/unified-modeling-language-uml-class-diagrams/) by *Geeks for Geeks* (accessed: 2026-01-06)
- [UML Class Diagram Tutorial](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) by *Visual Paradigm* (accessed: 2026-01-06)
