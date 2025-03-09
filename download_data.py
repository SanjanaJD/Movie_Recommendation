import os
import kaggle

# Function to download dataset from Kaggle
def download_kaggle_dataset(dataset_name, output_dir_name):
    try:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_dir_name)
        os.makedirs(output_dir, exist_ok=True)

        # Download dataset
        kaggle.api.dataset_download_files(dataset_name, path=output_dir, unzip=True)
        print(f"Dataset downloaded and extracted to: {output_dir}")

    except Exception as e:
        print(f"Error downloading dataset: {e}")
        raise

# Main function
def main():
    dataset_name = "ahsanaseer/top-rated-tmdb-movies-10k"  # Dataset name from Kaggle
    output_path = "Data"
    download_kaggle_dataset(dataset_name, output_path)

if __name__ == "__main__":
    main()
