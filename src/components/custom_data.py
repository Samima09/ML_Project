import pandas as pd

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education,
                 lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            data = {
                 'gender': [self.gender],
               'race/ethnicity': [self.race_ethnicity],
               'parental level of education': [self.parental_level_of_education],
               'lunch': [self.lunch],
               'test preparation course': [self.test_preparation_course],
               'reading score': [self.reading_score],
               'writing score': [self.writing_score],
            }
            return pd.DataFrame(data)
        except Exception as e:
            raise Exception(f"Error in get_data_as_dataframe: {e}")

