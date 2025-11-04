#!/bin/bash

# Build Symbolic Documentation
echo "Building Symbolic documentation..."

# Build HTML documentation
sphinx-build -b html docs docs/_build/html

echo "Build complete. Open docs/_build/html/index.html in your browser."

cd docs/_build/html/
python -m http.server