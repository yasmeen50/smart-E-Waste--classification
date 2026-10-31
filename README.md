# Smart E-Waste Classification

## 1. Project Overview
Smart E-Waste Classification is a machine-learning-based application designed to identify and classify electronic waste. It helps users understand e-waste categories and encourages proper recycling and disposal.

## 2. Technologies Used
- Python
- Streamlit
- Machine Learning
- NumPy
- RAG (Retrieval-Augmented Generation)

## 3. Project Structure
- `app.py` – Main application.
- `train_model.py` – Model training.
- `rag_agent.py` – RAG functionality.
- `ewaste_info.txt` – E-waste information.
- `labels.npy` – Classification labels.
- `requirements.txt` – Required libraries.

## 4. Installation
1. Install Python.
2. Download or clone the GitHub repository.
3. Open the project folder in the terminal.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

## 5. Run Frontend
Run the Streamlit application using:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## 6. Backend
The Python backend handles application logic, classification operations, and e-waste information retrieval.

## 7. Operational Scenarios
- Launch the application.
- Provide the required input.
- Process the input through the classification system.
- Display the classification result and relevant information.

## 8. Machine Learning
Machine learning is used to identify and classify electronic waste. The training functionality is provided in `train_model.py`, and classification labels are stored in `labels.npy`.

## 9. System Workflow
1. User opens the application.
2. User provides input.
3. System processes the input.
4. Classification is performed.
5. Results are displayed to the user.

## 10. Important Note
- Developed for academic purposes.
- Requires Python and the listed dependencies.
- Runs locally using Streamlit.
- Classification results depend on the trained model and input data.
- Promotes responsible e-waste management and recycling.
