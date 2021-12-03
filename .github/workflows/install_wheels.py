name: install wheels

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      VERSION: "0.9.1"
      USER: cms-l1-globaltrigger
    strategy:
      matrix:
        python-version: ["3.6", "3.7", "3.8", "3.9"]
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Install wheels
      run: |
        python -m pip install git+https://github.com/${{ env.USER }}/tm-python.git@${{ env.VERSION }}
    - name: Verify packages
      run: |
        python -c "from tmTable import __version__; assert __version__ == '${{ env.VERSION }}'"
        python -c "from tmGrammar import __version__; assert __version__ == '${{ env.VERSION }}'"
        python -c "from tmEventSetup import __version__; assert __version__ == '${{ env.VERSION }}'"
