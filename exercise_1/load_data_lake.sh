#!/bin/bash

if [ ! -f data.zip ];
then
	echo "Downloading files"
	wget -O "data.zip" "https://data.medicare.gov/views/bg9k-emty/files/Nqcy71p9Ss2RSBWDmP77H1DQXcyacr2khotGbDHHW_s?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"
	
	echo "Unzipping"
	unzip data.zip -d data

	echo "Renaming files"
	mkdir data/base
	mv "data/Hospital General Information.csv" data/base/hospitals.csv
	mv "data/Timely and Effective Care - Hospital.csv" data/base/effective_care.csv
	mv "data/Readmissions and Deaths - Hospital.csv" data/base/readmissions.csv
	mv "data/Measure Dates.csv" data/base/measures.csv
	mv "data/hvbp_hcahps_05_28_2015.csv" data/base/survey_responses.csv

	echo "Removing header rows"
	
	for f in data/*.csv
	do
		mv "$f" "$f"_OLD
		tail -n +2 "$f"_OLD > "$f"
		rm "$f"_OLD
	done

	for f in data/base/*.csv
	do
		mv "$f" "$f"_OLD
		tail -n +2 "$f"_OLD > "$f"
		rm "$f"_OLD
	done
fi

cd data/base

hdfs dfs -mkdir /user/w205/hospital_compare

for f in *.csv
do
	hdfs dfs -put $f /user/w205/hospital_compare
done

