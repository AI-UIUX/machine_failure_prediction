from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))

# Define the repo details
repo_id = "KunalGera/Machine-Failure-Prediction"
repo_type = "space"  # Could be "dataset", "model", or "space"
space_sdk = "docker"  # Replace this with your chosen SDK ('gradio', 'streamlit', 'docker', 'static')

# Check if the repo exists
try:
    # Try to get the repo info (this will raise an exception if it doesn't exist)
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Repository '{repo_id}' already exists.")
except:
    # Create the repo if it doesn't exist
    print(f"Repository '{repo_id}' does not exist. Creating it...")
    api.create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        space_sdk=space_sdk,  # Specify the space_sdk for "space" type repos
        exist_ok=True  # Allow creation even if the repo exists (it will just do nothing if exists)
    )

# Upload the folder to the repository
api.upload_folder(
    folder_path="week_2_mls/deployment",  # the local folder containing your files
    repo_id=repo_id,                     # the target repo
    repo_type=repo_type,                  # dataset, model, or space
    path_in_repo="",                      # optional: subfolder path inside the repo
)
