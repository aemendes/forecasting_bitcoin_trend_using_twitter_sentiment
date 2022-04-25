from contextlib import nullcontext
import pandas as pd
import json
import glob
from datetime import datetime
from pathlib import Path


src = "data/"

date = datetime.now()
data = []

files_per_day = glob.glob('data/*/*/*', recursive=True)
# files = glob.glob('data/year_2022/month_1/day_01/*.json', recursive=True)

def main():
	for file_per_day in files_per_day:
		print("loading file ./{}".format(file_per_day))

		all_day_files = glob.glob('{}/**/*.json'.format(file_per_day), recursive=True)

		result_data = pd.DataFrame()

		for day_file in all_day_files:
			data = json.load(open("./{}".format(day_file)))

			df = pd.DataFrame(data["data"])

			result_data = result_data.append(df, ignore_index=True)
		
		output_dir = Path('result/{}'.format(file_per_day))
		output_dir.mkdir(parents=True, exist_ok=True)

		print("Start saving....")
		result_data = result_data.drop(["in_reply_to_user_id", "withheld"], axis=1, errors='ignore')
		result_data.to_csv("./result/{}/data.csv".format(file_per_day), index=None)
		print("Data saved!")
	

if __name__ == "__main__":
    main()