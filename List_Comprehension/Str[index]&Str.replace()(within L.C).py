# List of elements stored in to years
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# if the year string is equal to the substring "2023" then replace the "2023" substring with the substring "2024". Else the "Year" element included
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years) 
