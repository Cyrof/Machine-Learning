# NLP Topic Modelling Assignment
### Overview
This project focuses on Natural Language Processing (NLP) for topic modelling. It uses various Python libraries and tools to analyse and model topics from a dataset. The project is structured into several Jupyter Notebooks, each focusing on different stagess of the workflow: data exploration, preprocessing, and modelling using BERT.

### Created With 
- Python 3.12.4
- Visual Studio Code 1.91.1
- Jupyter Notebook

### Setup Instructions
1. Create a virtual environment: 
   ```bash 
   python -m venv name-of-venv
   ```

2. Activate the virtual environment: 
   - On Windows:
        ```bash
        name-of-venv\Scripts\activate
        ```
   - On macOS and Linux:
        ```bash
        source name-of-venv/bin/activate
        ```

3. Install the required pacakges: 
   ```bash
   pip install -r requirements.txt
   ```

### Important Notes
**GCC Compatibility for `hdbscan`:**
The `hdbscan` library currently does not support GCC 14 and requires GCC 13 to work properly. This is an ongoing issue documented in the [hdbscan issues](https://github.com/scikit-learn-contrib/hdbscan/issues/634) on GitHub. Ensure that your system has GCC 13 installed to avoid compatibility issues. You can check your GCC version using: 
```bash
gcc --version
```
If you havve GCC 14 installed, you may need to downgrade to GCC 13.

### File Structure
``` sh
    .
    ├── Assignment 2 Final Report.docx
    ├── dataset
    ├── jupyter-files
    ├── README.md
    └── requirements.txt
```

### Usage Guide 
1. Data Exploration: 
   - Navigate to the `jupter-files` directory.
   - Open `data_exploration.ipynb`
   - Run all cells to explore and visualise the dataset.
    ``` bash
    cd jupyter-files
    jupyter notebook data_exploration.ipynb
    ```

2. Preprocessing:
   - Open `preprocessing.ipynb`.
   - Run all cells to preprocess the data, preparing it for modelling.
    ```bash
    jupyter notebook preprocessing.ipynb
    ```

3. BERT Model: 
   - Open `bert_model.ipynb`.
   - Run all cells to perform topic modelling using the BERT model.
    ``` bash
    jupyter notebook bert_model.ipynb
    ```
