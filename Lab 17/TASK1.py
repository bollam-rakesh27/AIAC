import pandas as pd
import re
import os

# ===============================
# 1. Load CSV file
# ===============================
local_path = "social_media.csv"
abs_path = r"C:\Users\Rakesh\OneDrive\Desktop\Attachments\AIAC\Lab 17\social_media.csv"

if not os.path.exists(abs_path):
    raise FileNotFoundError(
        f"CSV file not found at '{abs_path}'.\n"
        f"Current working directory: {os.getcwd()}"
    )

df = pd.read_csv(abs_path, encoding="utf-8", encoding_errors="ignore")

print(f"Loaded CSV from: {abs_path}")
print("Initial dataset shape:", df.shape)

# ===============================
# 2. Handle missing values in likes and shares
# ===============================
if "likes" in df.columns and "shares" in df.columns:
    print("Missing before:", df[['likes', 'shares']].isna().sum().to_dict())

    df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
    df['shares'] = pd.to_numeric(df['shares'], errors='coerce')

    likes_median = df['likes'].median(skipna=True)
    shares_median = df['shares'].median(skipna=True)

    df['likes'] = df['likes'].fillna(likes_median).clip(lower=0).astype(int)
    df['shares'] = df['shares'].fillna(shares_median).clip(lower=0).astype(int)

    print("Missing after:", df[['likes', 'shares']].isna().sum().to_dict())

# ===============================
# 3. Clean text: remove stopwords, punctuation, symbols
# ===============================

STOPWORDS = {
    'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to', 'in', 'for', 'of', 'with', 'by', 'from',
    'it', 'this', 'that', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did',
    'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'shall', 'i', 'you', 'he', 'she',
    'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'our', 'their'
}

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'<[^>]+>', '', text)                  # remove HTML tags
    text = re.sub(r'http[s]?://\S+', '', text)           # remove URLs
    text = re.sub(r'[^a-z0-9\s]', ' ', text)             # keep only alphanumerics
    text = re.sub(r'\s+', ' ', text).strip()
    words = [w for w in text.split() if w not in STOPWORDS and len(w) > 1]
    return ' '.join(words)

if "post_text" in df.columns:
    df['post_text_clean'] = df['post_text'].apply(clean_text)
else:
    df['post_text_clean'] = ""

# ===============================
# 4. Convert timestamp to datetime and extract features
# ===============================

if "timestamp" in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['hour'] = df['timestamp'].dt.hour
    df['weekday'] = df['timestamp'].dt.day_name()
else:
    df['timestamp'] = pd.NaT
    df['hour'] = None
    df['weekday'] = None

# ===============================
# 5. Detect and remove spam
# ===============================

def is_spam(text):
    if pd.isna(text) or len(str(text)) < 5:
        return True
    words = str(text).split()
    if len(words) > 0 and (len(set(words)) / len(words)) < 0.3:  # too repetitive
        return True
    if len(text) > 500:  # too long
        return True
    return False

df['is_spam'] = df['post_text_clean'].apply(is_spam)
spam_count = int(df['is_spam'].sum())
df = df[~df['is_spam']].drop(columns=['is_spam']).reset_index(drop=True)

# ===============================
# 6. Remove duplicate posts
# ===============================
duplicate_mask = df.duplicated(subset=['post_text_clean'], keep='first')
duplicate_count = int(duplicate_mask.sum())

df = df[~duplicate_mask].reset_index(drop=True)

# ===============================
# 7. Preview results
# ===============================

print({
    'spam_removed': spam_count,
    'duplicates_removed': duplicate_count,
    'rows_remaining': len(df)
})

print("\nSample cleaned data:")
print(df[['post_text', 'post_text_clean', 'timestamp', 'hour', 'weekday']].head().to_string())

# ===============================
# 8. Save cleaned dataset
# ===============================

output_file = r"C:\Users\Rakesh\OneDrive\Desktop\Attachments\AIAC\Lab 17\social_media_cleaned.csv"
df.to_csv(output_file, index=False)

print({
    'csv_created': output_file,
    'rows': len(df),
    'cols': len(df.columns)
})
