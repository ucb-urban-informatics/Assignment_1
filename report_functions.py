import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from pathlib import Path

# Write a function that takes in a csv and generates a histogram of the most common 
COLUMNS = ['ride_id', 'rideable_type', 'started_at', 'ended_at',
           'start_station_name', 'start_station_id', 'end_station_name',
           'end_station_id', 'start_lat', 'start_lng', 'end_lat', 'end_lng',
           'member_casual']


def rides_histogram(input_path: str | Path, save_path: str | Path, display=False) -> None:
    # load the dataframe from the file_paths
    try:
        temp = pd.read_csv(input_path)
        if set(temp.columns) != set(COLUMNS):
            raise ValueError("Columns don't match expected column set!")
    except Exception as e:
        print(f'File {input_path} failed: {e}')
        return

    if temp.shape[0] == 0:
        title_x = "No Data Found"
    elif temp['start_station_name'].value_counts().shape[0] != 1:
        raise ValueError(f'More than 1 `start_station_name` found in file: {input_path}')
    else:
        title_x = temp['start_station_name'].head(1).values[0]

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.histplot(pd.to_datetime(temp['started_at']), ax=ax)
    ax.set(xlabel='Date', ylabel='Trips', title=title_x)
    ax.tick_params(axis='x', labelrotation=30)
    if display:
        plt.show()
    plt.savefig(save_path)
    plt.close()


def generate_pdf_report(image_path: str | Path, save_path: str | Path, n_rides: int, station_code: int, title: str):
    if not isinstance(image_path, Path):
        img_path = Path(image_path)
    else:
        img_path = image_path

    if not img_path.exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Define PDF output path
    # pdf_path = img_path.with_suffix(".pdf")

    # Create PDF
    c = canvas.Canvas(str(save_path), pagesize=letter)
    width, height = letter

    # title and summary
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, title)

    c.setFont("Helvetica", 12)
    summary_text = f"Station {station_code} had {n_rides} rides for the month of January 2025"
    c.drawString(100, height - 80, summary_text)

    # our png image
    image = ImageReader(str(img_path))
    img_width, img_height = _scale_image(image, width, height)

    img_x = (width - img_width) / 2
    img_y = height - img_height - 150
    c.drawImage(image, img_x, img_y, width=img_width, height=img_height)

    # Save PDF
    c.save()
    return str(save_path)


def _scale_image(image: ImageReader, width: float, height: float):
    img_width, img_height = image.getSize()
    aspect = img_height / img_width
    # 150 & 200: arbitrary values just to avoid having image being
    # placed too high or close to margins - adjust if needed
    img_max_width = width - 150
    img_max_height = height - 200
    if img_width > img_max_width:
        img_width = img_max_width
        img_height = img_width * aspect
    if img_height > img_max_height:
        img_height = img_max_height
        img_width = img_height / aspect
    return img_width, img_height
