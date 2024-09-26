import pickle;
from pathlib import Path
import streamlit_authenticator as stauth;

names = ["Yuvraj", "Kanishq"];
email = ['yuvraj@gmail.com', 'kanishq@gmail.com'];
password = ['Yuvraj123', 'Kanishq123'];

hashed_passwords = stauth.Hasher(password).generate();

file_path = Path(__file__).parent/'hashed_pass.pkl';

with file_path.open('wb') as file:
  pickle.dump(hashed_passwords, file);


